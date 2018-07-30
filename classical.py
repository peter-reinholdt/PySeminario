from simtk.openmm import app
import simtk.openmm as mm
from simtk import unit
from sys import stdout
import parmed
import numpy as np


class Evaluator(object):
    def __init__(self, topology, coordinates):
        self.top = topology
        self.update_topology()
        self.set_coordinates(coordinates)

    def set_coordinates(self, coordinates):
        self.simulation.context.setPositions(coordinates)

    def update_topology(self):
        self.system = self.top.createSystem(nonbondedMethod=app.NoCutoff, nonbondedCutoff=99.9*unit.nanometers, constraints=None, rigidWater=False)
        self.integrator = mm.VerletIntegrator(0.001*unit.picoseconds)
        self.platform = mm.Platform.getPlatformByName('CPU')
        self.properties = {}
        self.simulation = app.Simulation(self.top.topology, self.system, self.integrator, self.platform, self.properties)
    
    def get_energy(self):
        state = self.simulation.context.getState(getEnergy=True)
        energy = state.getPotentialEnergy().value_in_unit(unit.kilojoule_per_mole)
        return energy

    def get_force(self):
        state = self.simulation.context.getState(getForces=True)
        force = state.getForces(asNumpy=True).value_in_unit(unit.kilojoule_per_mole/unit.nanometer)
        return force

    def get_hessian(self):
        DELTA = 0.01
        state = self.simulation.context.getState(getPositions=True)
        coordinates = state.getPositions(asNumpy=True).value_in_unit(unit.nanometer)
        new_coordinates = np.copy(coordinates)
        num_atoms = coordinates.shape[0]
        hessian = np.zeros((coordinates.shape[0]*coordinates.shape[1], coordinates.shape[0]*coordinates.shape[1])) # (3N,3N)
        for i_atom in range(num_atoms):
            for i_cart in range(3):
                new_coordinates[i_atom, i_cart] = coordinates[i_atom, i_cart] + DELTA
                self.set_coordinates(new_coordinates)
                state = self.simulation.context.getState(getForces=True)
                force_plus = state.getForces(asNumpy=True).value_in_unit(unit.kilojoule_per_mole/unit.nanometer)

                new_coordinates[i_atom, i_cart] = coordinates[i_atom, i_cart] - DELTA
                self.set_coordinates(new_coordinates)
                state = self.simulation.context.getState(getForces=True)
                force_minus = state.getForces(asNumpy=True).value_in_unit(unit.kilojoule_per_mole/unit.nanometer)
                new_coordinates[i_atom, i_cart] = coordinates[i_atom, i_cart]
                hessian[i_atom*3+i_cart] = ((force_plus - force_minus) / (2*DELTA)).flat[:]
        #hessian is second derivative of energy; force is *negative* of first derivative of energy...
        #adjust sign accordingly
        self.set_coordinates(coordinates)
        return -hessian


def get_mass_weighted_hessian(hessian, top):
    M = np.zeros(hessian.shape)
    for atom in top.atoms:
        for i in range(3):
            M[atom.idx*3+i, atom.idx*3+i] = 1.0/np.sqrt(atom.mass)
    return M @ hessian @ M
