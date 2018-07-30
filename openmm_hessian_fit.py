#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import classical
import parmed
from functools import partial
from scipy import optimize

class openmmFullHessianFit:
    def __init__(self, path_to_fchk, path_to_topology):
        """
        Class to fit forcefields parameters to a molecular cartesian Hessian.
        
        Input : path_to_fchk, the path to the fchk-file
                path_to_topology, the path of a parmed readable topology file
        Indexing starts from 0 and not 1.
        """
        self.topology = parmed.load_file(path_to_topology)
        fchk_file = open(path_to_fchk,'r').readlines()
        self._coordinate_list = []
        self._hessian_list    = []
        
        # Load in all needed stuff from fchk file
        for i in range(0, len(fchk_file)):
            if "Number of atoms" in fchk_file[i]:
                self.number_atoms = int(fchk_file[i].split("I")[1])
            if "Current cartesian coordinates" in fchk_file[i]:
                for j in range(i+1, len(fchk_file)):
                    if fchk_file[j][0:1] != " ":
                        # Hope this stop condition always works
                        break
                    self._coordinate_list = self._coordinate_list + fchk_file[j].split()
            if "Cartesian Force Constants" in fchk_file[i]:
                for j in range(i+1, len(fchk_file)):
                    if fchk_file[j][0:1] != " ":
                        # Hope this stop condition always works
                        break
                    self._hessian_list = self._hessian_list + fchk_file[j].split()
        self.coordinates = np.zeros((self.number_atoms, 3))
        self.target_hessian = np.zeros((self.number_atoms*3, self.number_atoms*3))
        
        # Transform coordinate vector to array
        i, j = -1, 0
        for idx in range(0, len(self._coordinate_list)):
            if idx%3 == 0:
                i += 1
                j = 0
            self.coordinates[i,j] = self._coordinate_list[idx]
            j += 1
        
        # Transform hessian vector to array
        i, j = 0, 0
        for idx in range(0, len(self._hessian_list)):
            if j > i:
                i += 1
                j = 0
            self.target_hessian[i,j] = self._hessian_list[idx]
            if i != j:
                self.target_hessian[j,i] = self._hessian_list[idx]
            j += 1


    def fit_parameters(self, method='slsqp',
            fit_bonds_k=True, 
            fit_bonds_req=False, 
            fit_angles_k=True,
            fit_angles_theteq=False,
            fit_dihedrals_phi_k=True,
            fit_dihedrals_phase=False):
        #the openmm part works in (nanometer, kJ/mol) units
        evaluator = classical.Evaluator(self.topology, self.coordinates * parmed.unit.bohr.conversion_factor_to(parmed.unit.nanometer))
        guess_vector_keys = []
        x0 = []
        loc = 0
        for index in range(len(evaluator.top.bond_types)):
            if fit_bonds_k:
                guess_vector_keys.append(("bond_k", index, loc))
                loc +=1
                x0.append(evaluator.top.bond_types[index].k)
            if fit_bonds_req:
                guess_vector_keys.append(("bond_req", index, loc))
                loc +=1
                x0.append(evaluator.top.bond_types[index].req)
        for index in range(len(evaluator.top.angle_types)):
            if fit_angles_k:
                guess_vector_keys.append(("angle_k", index, loc))
                loc +=1
                x0.append(evaluator.top.angle_types[index].k)
            if fit_angles_theteq:
                guess_vector_keys.append(("angle_theteq", index, loc))
                loc +=1
                x0.append(evaluator.top.angle_types[index].theteq)
        for index in range(len(evaluator.top.dihedral_types)):
            if fit_dihedrals_phi_k:
                guess_vector_keys.append(("dihedral_phi_k", index, loc))
                loc +=1
                x0.append(evaluator.top.dihedral_types[index].phi_k)
            if fit_dihedrals_phase:
                guess_vector_keys.append(("dihedral_phase", index, loc))
                loc +=1
                x0.append(evaluator.top.dihedral_types[index].phase)
        
        def cost_function(guess_vector, guess_vector_keys, evaluator, target_hessian):
            #unpack guess vector into top
            for i, key in enumerate(guess_vector_keys):
                if key[0] == "bond_k":
                    evaluator.top.bond_types[key[1]].k = guess_vector[key[2]]
                elif key[0] == "bond_req":
                    evaluator.top.bond_types[key[1]].req = guess_vector[key[2]]
                elif key[0] == "angle_k":
                    evaluator.top.angle_types[key[1]].k = guess_vector[key[2]]
                elif key[0] == "angle_theteq":
                    evaluator.top.angle_types[key[1]].theteq = guess_vector[key[2]]
                elif key[0] == "dihedral_phi_k":
                    evaluator.top.dihedral_types[key[1]].phi_k = guess_vector[key[2]]
                elif key[0] == "dihedral_phase":
                    evaluator.top.dihedral_types[key[1]].phase = guess_vector[key[2]]
            evaluator.update_topology()
            evaluator.set_coordinates(self.coordinates*parmed.unit.bohr.conversion_factor_to(parmed.unit.nanometer))

            #calculate hessian with openmm
            hessian = evaluator.get_hessian()
            #evaluate RMSD         hartree / bohr**2
            conversion_factor =  2625.5002 / (parmed.unit.bohr.conversion_factor_to(parmed.unit.nanometer))**2
            res = np.sqrt(np.average((target_hessian*conversion_factor-hessian)**2))
            print(res)
            return res

        fun = partial(cost_function, guess_vector_keys=guess_vector_keys, evaluator=evaluator, target_hessian=self.target_hessian) 
        self.res = optimize.minimize(fun, x0=x0, method=method) 


