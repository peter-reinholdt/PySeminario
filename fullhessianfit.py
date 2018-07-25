import numpy as np
from scipy import optimize
from functools import partial
from fullhessian_generated import radius_first_derivative, radius_second_derivative, theta_first_derivative, theta_second_derivative, phi_first_derivative, phi_second_derivative


class FullHessianFit:
    def __init__(self, path_to_fchk, bond_idx=[], angle_idx=[], dihedral_idx=[], dihedral_n=[], improper_idx=[]):
        """
        """
        self._energy_unit = 1.0 # baseline is au
        self._length_unit = 1.0 # baseline is au
        self._angle_unit  = 1.0 # baseline is radians
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
        self.hessian_target = np.zeros((self.number_atoms*3, self.number_atoms*3))
        
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
            self.hessian_target[i,j] = self._hessian_list[idx]
            if i != j:
                self.hessian_target[j,i] = self._hessian_list[idx]
            j += 1
        
        # Initialize internal needed objects for fit
        self.bond_idx     = bond_idx
        self.angle_idx    = angle_idx
        self.dihedral_idx = dihedral_idx
        self.dihedral_n   = dihedral_n
        self.improper_idx = improper_idx
        self.mm_hessians = np.zeros((len(self.bond_idx)+len(self.angle_idx)+len(self.dihedral_idx)+len(self.improper_idx), self.number_atoms*3, self.number_atoms*3))
        self.mm_gradients = np.zeros((len(self.bond_idx)+len(self.angle_idx)+len(self.dihedral_idx)+len(self.improper_idx), self.number_atoms*3))
        
    def _build_mm_hessians(self):
        counter = 0
        for idx in self.bond_idx:
            r0 = np.linalg.norm(self._calc_distance_vector(idx[0], idx[1]))
            x1,y1,z1 = self.coordinates[idx[0],:]
            x2,y2,z2 = self.coordinates[idx[1],:]

            # d_coord_0, d_coord_0
            self.mm_hessians[counter, 3*idx[0],   3*idx[0]]   = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"x1","x1")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[0]]   = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"y1","x1")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[0]]   = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"z1","x1")
            self.mm_hessians[counter, 3*idx[0],   3*idx[0]+1] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"x1","y1")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[0]+1] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"y1","y1")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[0]+1] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"z1","y1")
            self.mm_hessians[counter, 3*idx[0],   3*idx[0]+2] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"x1","z1")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[0]+2] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"y1","z1")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[0]+2] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"z1","z1")

            # d_coord_1, d_coord_0
            self.mm_hessians[counter, 3*idx[1],   3*idx[0]]   = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"x2","x1")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[0]]   = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"y2","x1")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[0]]   = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"z2","x1")
            self.mm_hessians[counter, 3*idx[1],   3*idx[0]+1] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"x2","y1")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[0]+1] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"y2","y1")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[0]+1] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"z2","y1")
            self.mm_hessians[counter, 3*idx[1],   3*idx[0]+2] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"x2","z1")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[0]+2] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"y2","z1")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[0]+2] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"z2","z1")

            # d_coord_0, d_coord_1
            self.mm_hessians[counter, 3*idx[0],   3*idx[1]]   = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"x1","x2")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[1]]   = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"y1","x2")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[1]]   = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"z1","x2")
            self.mm_hessians[counter, 3*idx[0],   3*idx[1]+1] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"x1","y2")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[1]+1] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"y1","y2")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[1]+1] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"z1","y2")
            self.mm_hessians[counter, 3*idx[0],   3*idx[1]+2] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"x1","z2")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[1]+2] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"y1","z2")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[1]+2] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"z1","z2")

            # d_coord_1, d_coord_1
            self.mm_hessians[counter, 3*idx[1],   3*idx[1]]   = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"x2","x2")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[1]]   = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"y2","x2")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[1]]   = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"z2","x2")
            self.mm_hessians[counter, 3*idx[1],   3*idx[1]+1] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"x2","y2")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[1]+1] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"y2","y2")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[1]+1] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"z2","y2")
            self.mm_hessians[counter, 3*idx[1],   3*idx[1]+2] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"x2","z2")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[1]+2] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"y2","z2")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[1]+2] = self._bond_second_derivative(x1,y1,z1,x2,y2,z2,r0,"z2","z2")

            counter += 1

        for idx in self.angle_idx:
            theta0 = self._calc_angle(idx[0], idx[1], idx[2])
            x1,y1,z1 = self.coordinates[idx[0],:]
            x2,y2,z2 = self.coordinates[idx[1],:]
            x3,y3,z3 = self.coordinates[idx[2],:]

            # d_coord_0, d_coord_0
            self.mm_hessians[counter, 3*idx[0],   3*idx[0]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x1","x1")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[0]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y1","x1")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[0]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z1","x1")
            self.mm_hessians[counter, 3*idx[0],   3*idx[0]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x1","y1")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[0]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y1","y1")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[0]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z1","y1")
            self.mm_hessians[counter, 3*idx[0],   3*idx[0]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x1","z1")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[0]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y1","z1")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[0]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z1","z1")

            # d_coord_1, d_coord_0
            self.mm_hessians[counter, 3*idx[1],   3*idx[0]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x2","x1")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[0]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y2","x1")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[0]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z2","x1")
            self.mm_hessians[counter, 3*idx[1],   3*idx[0]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x2","y1")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[0]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y2","y1")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[0]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z2","y1")
            self.mm_hessians[counter, 3*idx[1],   3*idx[0]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x2","z1")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[0]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y2","z1")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[0]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z2","z1")

            # d_coord_0, d_coord_1
            self.mm_hessians[counter, 3*idx[0],   3*idx[1]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x1","x2")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[1]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y1","x2")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[1]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z1","x2")
            self.mm_hessians[counter, 3*idx[0],   3*idx[1]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x1","y2")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[1]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y1","y2")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[1]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z1","y2")
            self.mm_hessians[counter, 3*idx[0],   3*idx[1]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x1","z2")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[1]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y1","z2")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[1]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z1","z2")

            # d_coord_1, d_coord_1
            self.mm_hessians[counter, 3*idx[1],   3*idx[1]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x2","x2")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[1]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y2","x2")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[1]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z2","x2")
            self.mm_hessians[counter, 3*idx[1],   3*idx[1]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x2","y2")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[1]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y2","y2")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[1]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z2","y2")
            self.mm_hessians[counter, 3*idx[1],   3*idx[1]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x2","z2")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[1]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y2","z2")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[1]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z2","z2")

            # d_coord_2, d_coord_0
            self.mm_hessians[counter, 3*idx[2],   3*idx[0]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x3","x1")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[0]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y3","x1")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[0]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z3","x1")
            self.mm_hessians[counter, 3*idx[2],   3*idx[0]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x3","y1")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[0]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y3","y1")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[0]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z3","y1")
            self.mm_hessians[counter, 3*idx[2],   3*idx[0]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x3","z1")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[0]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y3","z1")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[0]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z3","z1")

            # d_coord_0, d_coord_2
            self.mm_hessians[counter, 3*idx[0],   3*idx[2]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x1","x3")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[2]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y1","x3")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[2]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z1","x3")
            self.mm_hessians[counter, 3*idx[0],   3*idx[2]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x1","y3")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[2]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y1","y3")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[2]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z1","y3")
            self.mm_hessians[counter, 3*idx[0],   3*idx[2]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x1","z3")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[2]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y1","z3")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[2]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z1","z3")

            # d_coord_2, d_coord_1
            self.mm_hessians[counter, 3*idx[2],   3*idx[1]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x3","x2")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[1]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y3","x2")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[1]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z3","x2")
            self.mm_hessians[counter, 3*idx[2],   3*idx[1]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x3","y2")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[1]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y3","y2")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[1]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z3","y2")
            self.mm_hessians[counter, 3*idx[2],   3*idx[1]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x3","z2")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[1]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y3","z2")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[1]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z3","z2")

            # d_coord_1, d_coord_2
            self.mm_hessians[counter, 3*idx[1],   3*idx[2]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x2","x3")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[2]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y2","x3")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[2]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z2","x3")
            self.mm_hessians[counter, 3*idx[1],   3*idx[2]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x2","y3")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[2]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y2","y3")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[2]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z2","y3")
            self.mm_hessians[counter, 3*idx[1],   3*idx[2]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x2","z3")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[2]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y2","z3")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[2]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z2","z3")

            # d_coord_2, d_coord_2
            self.mm_hessians[counter, 3*idx[2],   3*idx[2]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x3","x3")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[2]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y3","x3")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[2]]   = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z3","x3")
            self.mm_hessians[counter, 3*idx[2],   3*idx[2]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x3","y3")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[2]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y3","y3")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[2]+1] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z3","y3")
            self.mm_hessians[counter, 3*idx[2],   3*idx[2]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x3","z3")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[2]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y3","z3")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[2]+2] = self._angle_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z3","z3")

            counter += 1
        
        n_idx = 0
        for idx in self.dihedral_idx:
            n = self.dihedral_n[n_idx]
            n_idx += 1
            phase = self._calc_phase(idx[0], idx[1], idx[2], idx[3], n)
            x1,y1,z1 = self.coordinates[idx[0],:]
            x2,y2,z2 = self.coordinates[idx[1],:]
            x3,y3,z3 = self.coordinates[idx[2],:]
            x4,y4,z4 = self.coordinates[idx[3],:]
            
            # d_coord_0, d_coord_0
            self.mm_hessians[counter, 3*idx[0],   3*idx[0]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x1","x1")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[0]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y1","x1")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[0]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z1","x1")
            self.mm_hessians[counter, 3*idx[0],   3*idx[0]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x1","y1")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[0]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y1","y1")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[0]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z1","y1")
            self.mm_hessians[counter, 3*idx[0],   3*idx[0]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x1","z1")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[0]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y1","z1")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[0]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z1","z1")
            
            # d_coord_0, d_coord_1
            self.mm_hessians[counter, 3*idx[0],   3*idx[1]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x1","x2")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[1]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y1","x2")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[1]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z1","x2")
            self.mm_hessians[counter, 3*idx[0],   3*idx[1]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x1","y2")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[1]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y1","y2")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[1]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z1","y2")
            self.mm_hessians[counter, 3*idx[0],   3*idx[1]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x1","z2")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[1]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y1","z2")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[1]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z1","z2")
            
            # d_coord_0, d_coord_2
            self.mm_hessians[counter, 3*idx[0],   3*idx[2]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x1","x3")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[2]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y1","x3")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[2]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z1","x3")
            self.mm_hessians[counter, 3*idx[0],   3*idx[2]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x1","y3")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[2]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y1","y3")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[2]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z1","y3")
            self.mm_hessians[counter, 3*idx[0],   3*idx[2]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x1","z3")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[2]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y1","z3")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[2]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z1","z3")
            
            # d_coord_0, d_coord_3
            self.mm_hessians[counter, 3*idx[0],   3*idx[3]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x1","x4")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[3]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y1","x4")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[3]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z1","x4")
            self.mm_hessians[counter, 3*idx[0],   3*idx[3]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x1","y4")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[3]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y1","y4")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[3]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z1","y4")
            self.mm_hessians[counter, 3*idx[0],   3*idx[3]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x1","z4")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[3]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y1","z4")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[3]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z1","z4")
            
            # d_coord_1, d_coord_0
            self.mm_hessians[counter, 3*idx[1],   3*idx[0]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x2","x1")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[0]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y2","x1")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[0]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z2","x1")
            self.mm_hessians[counter, 3*idx[1],   3*idx[0]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x2","y1")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[0]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y2","y1")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[0]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z2","y1")
            self.mm_hessians[counter, 3*idx[1],   3*idx[0]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x2","z1")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[0]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y2","z1")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[0]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z2","z1")
            
            # d_coord_1, d_coord_1
            self.mm_hessians[counter, 3*idx[1],   3*idx[1]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x2","x2")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[1]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y2","x2")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[1]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z2","x2")
            self.mm_hessians[counter, 3*idx[1],   3*idx[1]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x2","y2")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[1]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y2","y2")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[1]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z2","y2")
            self.mm_hessians[counter, 3*idx[1],   3*idx[1]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x2","z2")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[1]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y2","z2")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[1]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z2","z2")
            
            # d_coord_1, d_coord_2
            self.mm_hessians[counter, 3*idx[1],   3*idx[2]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x2","x3")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[2]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y2","x3")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[2]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z2","x3")
            self.mm_hessians[counter, 3*idx[1],   3*idx[2]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x2","y3")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[2]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y2","y3")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[2]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z2","y3")
            self.mm_hessians[counter, 3*idx[1],   3*idx[2]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x2","z3")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[2]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y2","z3")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[2]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z2","z3")
            
            # d_coord_1, d_coord_3
            self.mm_hessians[counter, 3*idx[1],   3*idx[3]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x2","x4")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[3]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y2","x4")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[3]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z2","x4")
            self.mm_hessians[counter, 3*idx[1],   3*idx[3]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x2","y4")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[3]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y2","y4")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[3]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z2","y4")
            self.mm_hessians[counter, 3*idx[1],   3*idx[3]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x2","z4")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[3]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y2","z4")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[3]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z2","z4")
            
            # d_coord_2, d_coord_0
            self.mm_hessians[counter, 3*idx[2],   3*idx[0]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x3","x1")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[0]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y3","x1")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[0]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z3","x1")
            self.mm_hessians[counter, 3*idx[2],   3*idx[0]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x3","y1")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[0]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y3","y1")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[0]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z3","y1")
            self.mm_hessians[counter, 3*idx[2],   3*idx[0]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x3","z1")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[0]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y3","z1")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[0]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z3","z1")
            
            # d_coord_2, d_coord_1
            self.mm_hessians[counter, 3*idx[2],   3*idx[1]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x3","x2")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[1]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y3","x2")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[1]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z3","x2")
            self.mm_hessians[counter, 3*idx[2],   3*idx[1]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x3","y2")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[1]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y3","y2")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[1]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z3","y2")
            self.mm_hessians[counter, 3*idx[2],   3*idx[1]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x3","z2")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[1]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y3","z2")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[1]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z3","z2")
            
            # d_coord_2, d_coord_2
            self.mm_hessians[counter, 3*idx[2],   3*idx[2]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x3","x3")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[2]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y3","x3")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[2]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z3","x3")
            self.mm_hessians[counter, 3*idx[2],   3*idx[2]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x3","y3")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[2]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y3","y3")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[2]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z3","y3")
            self.mm_hessians[counter, 3*idx[2],   3*idx[2]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x3","z3")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[2]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y3","z3")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[2]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z3","z3")
            
            # d_coord_2, d_coord_3
            self.mm_hessians[counter, 3*idx[2],   3*idx[3]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x3","x4")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[3]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y3","x4")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[3]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z3","x4")
            self.mm_hessians[counter, 3*idx[2],   3*idx[3]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x3","y4")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[3]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y3","y4")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[3]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z3","y4")
            self.mm_hessians[counter, 3*idx[2],   3*idx[3]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x3","z4")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[3]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y3","z4")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[3]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z3","z4")
            
            # d_coord_3, d_coord_0
            self.mm_hessians[counter, 3*idx[3],   3*idx[0]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x4","x1")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[0]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y4","x1")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[0]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z4","x1")
            self.mm_hessians[counter, 3*idx[3],   3*idx[0]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x4","y1")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[0]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y4","y1")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[0]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z4","y1")
            self.mm_hessians[counter, 3*idx[3],   3*idx[0]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x4","z1")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[0]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y4","z1")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[0]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z4","z1")
            
            # d_coord_3, d_coord_1
            self.mm_hessians[counter, 3*idx[3],   3*idx[1]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x4","x2")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[1]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y4","x2")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[1]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z4","x2")
            self.mm_hessians[counter, 3*idx[3],   3*idx[1]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x4","y2")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[1]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y4","y2")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[1]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z4","y2")
            self.mm_hessians[counter, 3*idx[3],   3*idx[1]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x4","z2")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[1]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y4","z2")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[1]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z4","z2")
            
            # d_coord_3, d_coord_2
            self.mm_hessians[counter, 3*idx[3],   3*idx[2]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x4","x3")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[2]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y4","x3")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[2]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z4","x3")
            self.mm_hessians[counter, 3*idx[3],   3*idx[2]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x4","y3")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[2]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y4","y3")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[2]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z4","y3")
            self.mm_hessians[counter, 3*idx[3],   3*idx[2]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x4","z3")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[2]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y4","z3")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[2]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z4","z3")
            
            # d_coord_3, d_coord_3
            self.mm_hessians[counter, 3*idx[3],   3*idx[3]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x4","x4")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[3]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y4","x4")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[3]]   = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z4","x4")
            self.mm_hessians[counter, 3*idx[3],   3*idx[3]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x4","y4")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[3]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y4","y4")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[3]+1] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z4","y4")
            self.mm_hessians[counter, 3*idx[3],   3*idx[3]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x4","z4")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[3]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y4","z4")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[3]+2] = self._dihedral_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z4","z4")
    
            counter += 1
    
        for idx in self.improper_idx:
            x1,y1,z1 = self.coordinates[idx[0],:]
            x2,y2,z2 = self.coordinates[idx[1],:]
            x3,y3,z3 = self.coordinates[idx[2],:]
            x4,y4,z4 = self.coordinates[idx[3],:]
            phi0 = self._phi(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4)
    
            # d_coord_0, d_coord_0
            self.mm_hessians[counter, 3*idx[0],   3*idx[0]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x1","x1")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[0]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y1","x1")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[0]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z1","x1")
            self.mm_hessians[counter, 3*idx[0],   3*idx[0]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x1","y1")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[0]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y1","y1")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[0]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z1","y1")
            self.mm_hessians[counter, 3*idx[0],   3*idx[0]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x1","z1")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[0]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y1","z1")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[0]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z1","z1")
            
            # d_coord_0, d_coord_1
            self.mm_hessians[counter, 3*idx[0],   3*idx[1]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x1","x2")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[1]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y1","x2")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[1]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z1","x2")
            self.mm_hessians[counter, 3*idx[0],   3*idx[1]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x1","y2")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[1]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y1","y2")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[1]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z1","y2")
            self.mm_hessians[counter, 3*idx[0],   3*idx[1]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x1","z2")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[1]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y1","z2")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[1]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z1","z2")
            
            # d_coord_0, d_coord_2
            self.mm_hessians[counter, 3*idx[0],   3*idx[2]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x1","x3")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[2]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y1","x3")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[2]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z1","x3")
            self.mm_hessians[counter, 3*idx[0],   3*idx[2]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x1","y3")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[2]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y1","y3")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[2]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z1","y3")
            self.mm_hessians[counter, 3*idx[0],   3*idx[2]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x1","z3")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[2]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y1","z3")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[2]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z1","z3")
            
            # d_coord_0, d_coord_3
            self.mm_hessians[counter, 3*idx[0],   3*idx[3]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x1","x4")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[3]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y1","x4")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[3]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z1","x4")
            self.mm_hessians[counter, 3*idx[0],   3*idx[3]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x1","y4")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[3]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y1","y4")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[3]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z1","y4")
            self.mm_hessians[counter, 3*idx[0],   3*idx[3]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x1","z4")
            self.mm_hessians[counter, 3*idx[0]+1, 3*idx[3]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y1","z4")
            self.mm_hessians[counter, 3*idx[0]+2, 3*idx[3]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z1","z4")
            
            # d_coord_1, d_coord_0
            self.mm_hessians[counter, 3*idx[1],   3*idx[0]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x2","x1")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[0]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y2","x1")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[0]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z2","x1")
            self.mm_hessians[counter, 3*idx[1],   3*idx[0]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x2","y1")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[0]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y2","y1")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[0]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z2","y1")
            self.mm_hessians[counter, 3*idx[1],   3*idx[0]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x2","z1")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[0]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y2","z1")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[0]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z2","z1")
            
            # d_coord_1, d_coord_1
            self.mm_hessians[counter, 3*idx[1],   3*idx[1]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x2","x2")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[1]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y2","x2")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[1]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z2","x2")
            self.mm_hessians[counter, 3*idx[1],   3*idx[1]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x2","y2")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[1]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y2","y2")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[1]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z2","y2")
            self.mm_hessians[counter, 3*idx[1],   3*idx[1]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x2","z2")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[1]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y2","z2")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[1]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z2","z2")
            
            # d_coord_1, d_coord_2
            self.mm_hessians[counter, 3*idx[1],   3*idx[2]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x2","x3")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[2]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y2","x3")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[2]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z2","x3")
            self.mm_hessians[counter, 3*idx[1],   3*idx[2]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x2","y3")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[2]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y2","y3")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[2]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z2","y3")
            self.mm_hessians[counter, 3*idx[1],   3*idx[2]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x2","z3")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[2]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y2","z3")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[2]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z2","z3")
            
            # d_coord_1, d_coord_3
            self.mm_hessians[counter, 3*idx[1],   3*idx[3]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x2","x4")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[3]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y2","x4")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[3]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z2","x4")
            self.mm_hessians[counter, 3*idx[1],   3*idx[3]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x2","y4")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[3]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y2","y4")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[3]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z2","y4")
            self.mm_hessians[counter, 3*idx[1],   3*idx[3]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x2","z4")
            self.mm_hessians[counter, 3*idx[1]+1, 3*idx[3]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y2","z4")
            self.mm_hessians[counter, 3*idx[1]+2, 3*idx[3]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z2","z4")
            
            # d_coord_2, d_coord_0
            self.mm_hessians[counter, 3*idx[2],   3*idx[0]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x3","x1")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[0]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y3","x1")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[0]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z3","x1")
            self.mm_hessians[counter, 3*idx[2],   3*idx[0]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x3","y1")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[0]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y3","y1")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[0]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z3","y1")
            self.mm_hessians[counter, 3*idx[2],   3*idx[0]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x3","z1")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[0]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y3","z1")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[0]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z3","z1")
            
            # d_coord_2, d_coord_1
            self.mm_hessians[counter, 3*idx[2],   3*idx[1]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x3","x2")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[1]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y3","x2")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[1]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z3","x2")
            self.mm_hessians[counter, 3*idx[2],   3*idx[1]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x3","y2")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[1]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y3","y2")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[1]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z3","y2")
            self.mm_hessians[counter, 3*idx[2],   3*idx[1]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x3","z2")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[1]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y3","z2")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[1]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z3","z2")
            
            # d_coord_2, d_coord_2
            self.mm_hessians[counter, 3*idx[2],   3*idx[2]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x3","x3")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[2]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y3","x3")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[2]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z3","x3")
            self.mm_hessians[counter, 3*idx[2],   3*idx[2]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x3","y3")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[2]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y3","y3")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[2]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z3","y3")
            self.mm_hessians[counter, 3*idx[2],   3*idx[2]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x3","z3")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[2]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y3","z3")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[2]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z3","z3")
            
            # d_coord_2, d_coord_3
            self.mm_hessians[counter, 3*idx[2],   3*idx[3]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x3","x4")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[3]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y3","x4")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[3]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z3","x4")
            self.mm_hessians[counter, 3*idx[2],   3*idx[3]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x3","y4")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[3]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y3","y4")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[3]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z3","y4")
            self.mm_hessians[counter, 3*idx[2],   3*idx[3]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x3","z4")
            self.mm_hessians[counter, 3*idx[2]+1, 3*idx[3]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y3","z4")
            self.mm_hessians[counter, 3*idx[2]+2, 3*idx[3]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z3","z4")
            
            # d_coord_3, d_coord_0
            self.mm_hessians[counter, 3*idx[3],   3*idx[0]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x4","x1")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[0]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y4","x1")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[0]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z4","x1")
            self.mm_hessians[counter, 3*idx[3],   3*idx[0]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x4","y1")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[0]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y4","y1")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[0]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z4","y1")
            self.mm_hessians[counter, 3*idx[3],   3*idx[0]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x4","z1")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[0]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y4","z1")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[0]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z4","z1")
            
            # d_coord_3, d_coord_1
            self.mm_hessians[counter, 3*idx[3],   3*idx[1]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x4","x2")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[1]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y4","x2")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[1]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z4","x2")
            self.mm_hessians[counter, 3*idx[3],   3*idx[1]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x4","y2")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[1]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y4","y2")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[1]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z4","y2")
            self.mm_hessians[counter, 3*idx[3],   3*idx[1]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x4","z2")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[1]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y4","z2")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[1]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z4","z2")
            
            # d_coord_3, d_coord_2
            self.mm_hessians[counter, 3*idx[3],   3*idx[2]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x4","x3")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[2]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y4","x3")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[2]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z4","x3")
            self.mm_hessians[counter, 3*idx[3],   3*idx[2]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x4","y3")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[2]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y4","y3")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[2]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z4","y3")
            self.mm_hessians[counter, 3*idx[3],   3*idx[2]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x4","z3")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[2]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y4","z3")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[2]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z4","z3")
            
            # d_coord_3, d_coord_3
            self.mm_hessians[counter, 3*idx[3],   3*idx[3]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x4","x4")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[3]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y4","x4")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[3]]   = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z4","x4")
            self.mm_hessians[counter, 3*idx[3],   3*idx[3]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x4","y4")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[3]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y4","y4")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[3]+1] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z4","y4")
            self.mm_hessians[counter, 3*idx[3],   3*idx[3]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x4","z4")
            self.mm_hessians[counter, 3*idx[3]+1, 3*idx[3]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y4","z4")
            self.mm_hessians[counter, 3*idx[3]+2, 3*idx[3]+2] = self._improper_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z4","z4")
    
            counter += 1
        
    
    def _build_mm_gradients(self):
        # No use for this since it is zero by definition
        counter = 0
        for idx in self.bond_idx:
            r0 = np.linalg.norm(self._calc_distance_vector(idx[0], idx[1]))
            x1,y1,z1 = self.coordinates[idx[0],:]
            x2,y2,z2 = self.coordinates[idx[1],:]
            
            # d_coord_0
            self.mm_gradients[counter, 3*idx[0]]   = self._bond_first_derivative(x1,y1,z1,x2,y2,z2,r0,"x1")
            self.mm_gradients[counter, 3*idx[0]+1] = self._bond_first_derivative(x1,y1,z1,x2,y2,z2,r0,"y1")
            self.mm_gradients[counter, 3*idx[0]+2] = self._bond_first_derivative(x1,y1,z1,x2,y2,z2,r0,"z1")
            
            # d_coord_1
            self.mm_gradients[counter, 3*idx[1]]   = self._bond_first_derivative(x1,y1,z1,x2,y2,z2,r0,"x2")
            self.mm_gradients[counter, 3*idx[1]+1] = self._bond_first_derivative(x1,y1,z1,x2,y2,z2,r0,"y2")
            self.mm_gradients[counter, 3*idx[1]+2] = self._bond_first_derivative(x1,y1,z1,x2,y2,z2,r0,"z2")
            
            counter += 1
            
        for idx in self.angle_idx:
            theta0 = self._calc_angle(idx[0], idx[1], idx[2])
            x1,y1,z1 = self.coordinates[idx[0],:]
            x2,y2,z2 = self.coordinates[idx[1],:]
            x3,y3,z3 = self.coordinates[idx[2],:]
            
            # d_coord_0
            self.mm_gradients[counter, 3*idx[0]]   = self._angle_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x1")
            self.mm_gradients[counter, 3*idx[0]+1] = self._angle_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y1")
            self.mm_gradients[counter, 3*idx[0]+2] = self._angle_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z1")
            
            # d_coord_1
            self.mm_gradients[counter, 3*idx[1]]   = self._angle_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x2")
            self.mm_gradients[counter, 3*idx[1]+1] = self._angle_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y2")
            self.mm_gradients[counter, 3*idx[1]+2] = self._angle_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z2")
            
            # d_coord_2
            self.mm_gradients[counter, 3*idx[2]]   = self._angle_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"x3")
            self.mm_gradients[counter, 3*idx[2]+1] = self._angle_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"y3")
            self.mm_gradients[counter, 3*idx[2]+2] = self._angle_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,"z3")
            
            counter += 1
        
        n_idx = 0
        for idx in self.dihedral_idx:
            n = dihedral_n[n_idx]
            n_idx += 1
            phase = self._calc_phase(idx[0], idx[1], idx[2], idx[3], n)
            x1,y1,z1 = self.coordinates[idx[0],:]
            x2,y2,z2 = self.coordinates[idx[1],:]
            x3,y3,z3 = self.coordinates[idx[2],:]
            x4,y4,z4 = self.coordinates[idx[3],:]
            
            # d_coord_0
            self.mm_gradients[counter, 3*idx[0]]   = self._dihedral_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x1")
            self.mm_gradients[counter, 3*idx[0]+1] = self._dihedral_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y1")
            self.mm_gradients[counter, 3*idx[0]+2] = self._dihedral_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z1")
            
            # d_coord_1
            self.mm_gradients[counter, 3*idx[1]]   = self._dihedral_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x2")
            self.mm_gradients[counter, 3*idx[1]+1] = self._dihedral_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y2")
            self.mm_gradients[counter, 3*idx[1]+2] = self._dihedral_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z2")
            
            # d_coord_2
            self.mm_gradients[counter, 3*idx[2]]   = self._dihedral_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x3")
            self.mm_gradients[counter, 3*idx[2]+1] = self._dihedral_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y3")
            self.mm_gradients[counter, 3*idx[2]+2] = self._dihedral_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z3")
            
            # d_coord_3
            self.mm_gradients[counter, 3*idx[3]]   = self._dihedral_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"x4")
            self.mm_gradients[counter, 3*idx[3]+1] = self._dihedral_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"y4")
            self.mm_gradients[counter, 3*idx[3]+2] = self._dihedral_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,"z4")
            
            counter += 1
            
        for idx in self.dihedral_idx:
            x1,y1,z1 = self.coordinates[idx[0],:]
            x2,y2,z2 = self.coordinates[idx[1],:]
            x3,y3,z3 = self.coordinates[idx[2],:]
            x4,y4,z4 = self.coordinates[idx[3],:]
            phi0 = self._phi(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4)
            
            # d_coord_0
            self.mm_gradients[counter, 3*idx[0]]   = self._improper_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x1")
            self.mm_gradients[counter, 3*idx[0]+1] = self._improper_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y1")
            self.mm_gradients[counter, 3*idx[0]+2] = self._improper_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z1")
            
            # d_coord_1
            self.mm_gradients[counter, 3*idx[1]]   = self._improper_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x2")
            self.mm_gradients[counter, 3*idx[1]+1] = self._improper_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y2")
            self.mm_gradients[counter, 3*idx[1]+2] = self._improper_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z2")
            
            # d_coord_2
            self.mm_gradients[counter, 3*idx[2]]   = self._improper_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x3")
            self.mm_gradients[counter, 3*idx[2]+1] = self._improper_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y3")
            self.mm_gradients[counter, 3*idx[2]+2] = self._improper_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z3")
            
            # d_coord_3
            self.mm_gradients[counter, 3*idx[3]]   = self._improper_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"x4")
            self.mm_gradients[counter, 3*idx[3]+1] = self._improper_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"y4")
            self.mm_gradients[counter, 3*idx[3]+2] = self._improper_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,"z4")
            
            counter += 1
            
    
    def _calc_phase(self, atom_idx_A, atom_idx_B, atom_idx_C, atom_idx_D, n):
        x1,y1,z1 = self.coordinates[atom_idx_A,:]
        x2,y2,z2 = self.coordinates[atom_idx_B,:]
        x3,y3,z3 = self.coordinates[atom_idx_C,:]
        x4,y4,z4 = self.coordinates[atom_idx_D,:]
        return -n*self._phi(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4)

    
    def _calc_distance_vector(self, atom_idx_A, atom_idx_B):
        return (self.coordinates[atom_idx_A,:]-self.coordinates[atom_idx_B,:])
    

    def _calc_angle(self, atom_idx_A, atom_idx_B, atom_idx_C):
        AB = self._calc_distance_vector(atom_idx_A, atom_idx_B)
        BC = -  self._calc_distance_vector(atom_idx_B, atom_idx_C)
        #A · B = |A| * |B| * cos(Θ)
        angle = np.arccos(np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))
        return angle

        
    def _radius(self,x1,y1,z1,x2,y2,z2):
        return ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**0.5
    
    
    def _theta(self,x1,y1,z1,x2,y2,z2,x3,y3,z3):
        return np.arccos(((x2-x1)*(x2-x3)+(y2-y1)*(y2-y3)+(z2-z1)*(z2-z3))/(((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**0.5 * ((x2-x3)**2+(y2-y3)**2+(z2-z3)**2)**0.5))
    
    
    def _phi(self,X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
        x0 = X2 - X3
        x1 = Y2 - Y3
        x2 = Z2 - Z3
        x3 = X1 - X2
        x4 = Y1 - Y2
        x5 = -x0*x4 + x1*x3
        x6 = Z3 - Z4
        x7 = X3 - X4
        x8 = x0*x6 - x2*x7
        x9 = Z1 - Z2
        x10 = -x0*x9 + x2*x3
        x11 = Y3 - Y4
        x12 = x0*x11 - x1*x7
        x13 = x1*x6 - x11*x2
        x14 = -x1*x9 + x2*x4
        return np.atan2(-(x0*(-x10*x12 + x5*x8) + x1*(-x12*x14 + x13*x5) + x2*(x10*x13 - x14*x8))/sqrt(x0**2 + x1**2 + x2**2), x10*x8 + x12*x5 + x13*x14)
        
    
    def _bond_first_derivative(self,x1,y1,z1,x2,y2,z2,r0,d1):
        # zero per definition. LOL!
        # self._radius(x1,y1,z1,x2,y2,z2) = r0, because r0 is found as r0 = self._radius(x1,y1,z1,x2,y2,z2)
        return (self._radius(x1,y1,z1,x2,y2,z2) - r0)*radius_first_derivative(x1,y1,z1,x2,y2,z2,d1)
    
    
    def _angle_first_derivative(self,x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,d1):
        # zero per definition. LOL!
        return (self._theta(x1,y1,z1,x2,y2,z2,x3,y3,z3) - theta0)*theta_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,d1)
    
    
    def _dihedral_first_derivative(self,x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,d1):
        # zero per definition. LOL!
        return -n**phi_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,d1)*np.sin(n*self._phi(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4) + phase)
    
    
    def _improper_first_derivative(self,x1,y1,z1,x2,y2,z2,x3,y3,z3,phia0,d1):
        # zero per definition. LOL!
        return (self._phi(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4) - phi0)*phi_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,d1)
    
    
    def _bond_second_derivative(self,x1,y1,z1,x2,y2,z2,r0,d1,d2):
        output = radius_first_derivative(x1,y1,z1,x2,y2,z2,d1)*radius_first_derivative(x1,y1,z1,x2,y2,z2,d2)
        return output + (self._radius(x1,y1,z1,x2,y2,z2) - r0)*radius_second_derivative(x1,y1,z1,x2,y2,z2,d1,d2)
    
    
    def _angle_second_derivative(self,x1,y1,z1,x2,y2,z2,x3,y3,z3,theta0,d1,d2):
        output = theta_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,d1)*theta_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,d2)
        return output + (self._theta(x1,y1,z1,x2,y2,z2,x3,y3,z3) - theta0)*theta_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,d1,d2)
   

    def _dihedral_second_derivative(self,x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phase,n,d1,d2):
        output  = -n*phi_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,d1,d2)*np.sin(n*self._phi(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4) + phase)
        output += -n*n*phi_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,d1)*phi_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,d2)*np.cos(n*self._phi(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4) + phase)
        return output
        
        
    def _improper_second_derivative(self,x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,phi0,d1,d2):
        output = phi_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,d1)*phi_first_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,d2)
        return output + (self._phi(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4) - phi0)*phi_second_derivative(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,d1,d2)
        
        
    def set_energy_unit(self, unit):
        if unit.lower() == "kj/mol":
            self._energy_unit = 2625.5002
        elif unit.lower() == "kcal/mol":
            self._energy_unit = 627.509608030593
        elif unit.lower() == "hartree" or unit.lower() == "au":
            self._energy_unit = 1.0
        else:
            raise ValueError("Given unit not recognized")
      
            
    def set_length_unit(self, unit):
        if unit.lower() == "nm":
            self._length_unit = 0.0529177249
        elif unit.lower() == "angstrom" or unit.lower() == "å":
            self._length_unit = 0.529177249
        elif unit.lower() == "bohr" or unit.lower() == "au" or unit.lower() == "bohr radius":
            self._length_unit = 1.0
        else:
            raise ValueError("Given unit not recognized")
        
            
    def set_angle_unit(self, unit):
        if unit.lower() == "degrees" or unit.lower() == "degree":
            self._angle_unit = 57.2957795
        elif unit.lower() == "radians" or unit.lower() == "radian":
            self._angle_unit = 1.0
        else:
            raise ValueError("Given unit not recognized")
            
            
    def fit_parameters(self):
        def predicted_hessian(ff_constants, hessians):
            predicted_hessian = np.zeros((len(hessians[0]),len(hessians[0])))
            for i in range(0, len(hessians)):
                predicted_hessian += hessians[i]*ff_constants[i]
            return predicted_hessian
        
        def Hessian_error(ff_constants, hessians, target_hessian):
            return (np.average((target_hessian - predicted_hessian(ff_constants, hessians))**2))**0.5
        
        self._build_mm_hessians()
        #self._build_mm_gradients(), zero by definition
        baked_hessian_error = partial(Hessian_error, hessians=self.mm_hessians, target_hessian=self.hessian_target)
        initial_guess = [1]*len(self.mm_hessians)
        self.fitted_output = optimize.minimize(baked_hessian_error, initial_guess)
        
        
    def get_bond_constants(self):
        bond_constants = []
        for i in range(0, len(self.bond_idx)):
            bond_constants.append(self.fitted_output["x"][i])
        return np.array(bond_constants)*self._energy_unit/(self._length_unit**2)
    
    
    def get_angle_constants(self):
        angle_constants = []
        for i in range(len(self.bond_idx), len(self.bond_idx)+len(self.angle_idx)):
            angle_constants.append(self.fitted_output["x"][i])
        return np.array(angle_constants)*self._energy_unit/(self._angle_unit**2)
    
    
    def get_dihedral_constants(self):
        dihedral_constants = []
        for i in range(len(self.bond_idx)+len(self.angle_idx), len(self.bond_idx)+len(self.angle_idx)+len(self.dihedral_idx)):
            dihedral_constants.append(self.fitted_output["x"][i])
        return np.array(dihedral_constants)*self._energy_unit/(self._angle_unit**2)

    
    def get_improper_constants(self):
        improper_constants = []
        for i in range(len(self.bond_idx)+len(self.angle_idx)+len(self.dihedral_idx), len(self.bond_idx)+len(self.angle_idx)+len(self.dihedral_idx)+len(self.improper_idx)):
            improper_constants.append(self.fitted_output["x"][i])
        return np.array(improper_constants)*self._energy_unit/(self._angle_unit**2)
    
    
    def get_bond_length(self):
        bond_lengths = []
        for idx in self.bond_idx:
            bond_lengths.append(np.linalg.norm(self._calc_distance_vector(idx[0], idx[1])))
        return np.array(bond_lengths) * self._length_unit
    
    
    def get_angle(self):
        bond_angle = []
        for idx in self.angle_idx:
            bond_angle.append(self._calc_angle(idx[0], idx[1], idx[2]))
        return np.array(bond_angle) * self._angle_unit
    
    
    def get_dihedral(self):
        """Returns the phase factor of the dihedral angle"""
        bond_dihedral = []
        n_idx = 0
        for idx in self.dihedral_idx:
            bond_dihedral.append(self._calc_phase(idx[0], idx[1], idx[2], idx[3], self.dihedral_n[n_idx]))
            n_idx += 1
        return np.array(bond_dihedral) * self._angle_unit
    
    
    def get_improper(self):
        bond_improper = []
        for idx in self.improper_idx:
            x1,y1,z1 = self.coordinates[idx[0],:]
            x2,y2,z2 = self.coordinates[idx[1],:]
            x3,y3,z3 = self.coordinates[idx[2],:]
            x4,y4,z4 = self.coordinates[idx[3],:]
            bond_improper.append(self._phi(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4))
        return np.array(bond_improper) * self._angle_unit
