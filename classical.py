from simtk.openmm import app
import simtk.openmm as mm
from simtk import unit
from sys import stdout
import parmed
import numpy as np

class classical(object):
    def __init__(self, topology_file):
        self.top = parmed.load_file(topology_file)
        self.system = self.top.createSystem(nonbondedMethod=app.NoCutoff, nonbondedCutoff=99.9*unit.nanometers, constraints=None, rigidWater=False)
        self.integrator = mm.VerletIntegrator(0.002*unit.picoseconds)
        self.platform = mm.Platform.getPlatformByName('CPU')
        self.properties = {}
        self.simulation = app.Simulation(self.top.topology, self.system, self.integrator, self.platform, self.properties)

    def set_coordinates(self, coordinates):
        self.simulation.context.setPositions(coordinates)
    
    def get_energy(self):
        yystate = self.simulation.context.getState(getEnergy=True)
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
        return hessian

    def get_mass_weighted_hessian(self):
        hessian = self.get_hessian()
        M = np.zeros(hessian.shape)
        for atom in self.top.atoms:
            for i in range(3):
                M[atom.idx*3+i, atom.idx*3+i] = 1.0/np.sqrt(atom.mass)
        return M @ hessian @ M
