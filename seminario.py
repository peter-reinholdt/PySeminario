import numpy as np

class SeminarioMethod:
    def __init__(self, path_to_fchk):
        """
        Class to make bonded force field parameters based on a Gaussian
        geometry optmization and frequency calculation.
        
        This class needs the path to the fchk file to get the needed information.
        
        Equations are from: 
        Calculation of Intramolecular Force Fields from Second-Derivative Tensors
        J. M. Seminario
        https://doi.org/10.1002/(SICI)1097-461X(1996)60:7<1271::AID-QUA8>3.0.CO;2-W
        """
        self._energy_unit = 1.0 # baseline is au
        self._length_unit = 1.0 # baseline is au
        self._angle_unit = 1.0 # baseline is radians
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
        self.hessian = np.zeros((self.number_atoms*3, self.number_atoms*3))
        
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
            self.hessian[i,j] = self._hessian_list[idx]
            if i != j:
                self.hessian[j,i] = self._hessian_list[idx]
            j += 1
     
            
    def set_energy_unit(self, unit):
        if unit.lower() == "kj/mol":
            self._energy_unit = 2625.5002
        elif unit.lower() == "kcal/mol":
            self._energy_unit = 627.509608030593
        else:
            print("Given unit not recognized")
            
    def set_length_unit(self, unit):
        if unit.lower() == "nm":
            self._length_unit = 0.0529177249
        elif unit.lower() == "angstrom" or unit.lower() == "å":
            self._length_unit = 0.529177249
        else:
            print("Given unit not recognized")
            
    def set_angle_unit(self, unit):
        if unit.lower() == "degrees" or unit.lower() == "degree":
            self._angle_unit = 57.2957795
        else:
            print("Given unit not recognized")
            
    def _calc_normal_distance_vector(self, atom_idx_A, atom_idx_B):
        return (self.coordinates[atom_idx_A,:]-self.coordinates[atom_idx_B,:])/np.linalg.norm(self.coordinates[atom_idx_A,:]-self.coordinates[atom_idx_B,:])
    
    def _calc_distance_vector(self, atom_idx_A, atom_idx_B):
        return (self.coordinates[atom_idx_A,:]-self.coordinates[atom_idx_B,:])
    
    def _calc_point_plane_distance(self, atom_idx_A, atom_idx_B, atom_idx_C, atom_idx_D):
        vec_AB = self._calc_distance_vector(atom_idx_A, atom_idx_B)
        vec_AC = self._calc_distance_vector(atom_idx_A, atom_idx_C)
        vec_n = np.cross(vec_AB, vec_AC)
        a, b, c = vec_n[:]
        x0, y0, z0 = self.coordinates[atom_idx_A,:]
        d = -1.0*(a*x0 + b*y0 + c*z0)
        x0, y0, z0 = self.coordinates[atom_idx_D,:]
        distance = abs(a*x0 + b*y0 + c*z0 + d)/(a**2+b**2+c**2)**0.5
        return distance
    
    def _calc_bond_constant(self, atom_idx_A, atom_idx_B):
        hessian_block = -1.0*self.hessian[3*atom_idx_A:3*atom_idx_A+3,3*atom_idx_B:3*atom_idx_B+3]
        eigvals, eigvecs = np.linalg.eig(hessian_block)
        unit_bond_vector = self._calc_normal_distance_vector(atom_idx_A, atom_idx_B)
        force_constant = 0
        for i in range(0, 3):
            force_constant += eigvals[i]*np.abs(np.dot(unit_bond_vector, eigvecs[i]))
        return force_constant
    
    def _calc_angle_constant(self, atom_idx_A, atom_idx_B, atom_idx_C):
        hessian_block_AB = -1.0*self.hessian[3*atom_idx_A:3*atom_idx_A+3,3*atom_idx_B:3*atom_idx_B+3]
        hessian_block_CB = -1.0*self.hessian[3*atom_idx_C:3*atom_idx_C+3,3*atom_idx_B:3*atom_idx_B+3]
        u_AB = self._calc_normal_distance_vector(atom_idx_A, atom_idx_B)
        u_CB = self._calc_normal_distance_vector(atom_idx_C, atom_idx_B)
        u_N = np.cross(u_CB, u_AB)/np.linalg.norm(np.cross(u_CB, u_AB))
        u_PA = np.cross(u_N, u_AB)
        u_PC = np.cross(u_N, u_CB)
        R_AB = self._calc_distance_vector(atom_idx_A, atom_idx_B)
        R_CB = self._calc_distance_vector(atom_idx_C, atom_idx_B)
        eigvals_AB, eigvecs_AB = np.linalg.eig(hessian_block_AB)
        eigvals_CB, eigvecs_CB = np.linalg.eig(hessian_block_CB)
        contribution_AB = 0.0
        contribution_CB = 0.0
        for i in range(0, 3):
            contribution_AB += eigvals_AB[i]*np.abs(np.dot(u_PA,eigvecs_AB[i]))
            # In equation in paper, there is no eigvals_CB (lambda^CB).
            #  I haven't done the maths, but it might be a mistake?
            #    equation (14)
            contribution_CB += eigvals_CB[i]*np.abs(np.dot(u_PC,eigvecs_CB[i]))
        contribution_AB *= np.dot(R_AB, R_AB)
        contribution_CB *= np.dot(R_CB, R_CB)
        force_constant = 1.0/(1.0/contribution_AB + 1.0/contribution_CB)
        return force_constant
    
    def _calc_dihedral_constant(self, atom_idx_A, atom_idx_B, atom_idx_C, atom_idx_D):
        hessian_block_AB = -1.0*self.hessian[3*atom_idx_A:3*atom_idx_A+3,3*atom_idx_B:3*atom_idx_B+3]
        hessian_block_DC = -1.0*self.hessian[3*atom_idx_D:3*atom_idx_D+3,3*atom_idx_C:3*atom_idx_C+3]
        u_AB = self._calc_normal_distance_vector(atom_idx_A, atom_idx_B)
        u_CB = self._calc_normal_distance_vector(atom_idx_C, atom_idx_B)
        u_DC = self._calc_normal_distance_vector(atom_idx_D, atom_idx_C)
        u_BC = self._calc_normal_distance_vector(atom_idx_B, atom_idx_C)
        R_BA = self._calc_distance_vector(atom_idx_B, atom_idx_A)
        R_CD = self._calc_distance_vector(atom_idx_C, atom_idx_D)
        u_NABC = np.cross(u_CB, U_AB)/np.linalg.norm(np.cross(u_CB, U_AB))
        u_NBCD = np.cross(u_DC, u_BC)/np.linalg.norm(np.cross(u_DC, u_BC))
        eigvals_AB, eigvecs_AB = np.linalg.eig(hessian_block_AB)
        eigvals_DC, eigvecs_DC = np.linalg.eig(hessian_block_DC)
        contribution_ABC = 0.0
        contribution_BCD = 0.0
        for i in range(0, 3):
            contribution_ABC += eigvals_AB[i]*np.abs(np.dot(u_NABC,eigvecs_AB[i]))
            contribution_BCD += eigvals_DC[i]*np.abs(np.dot(u_NBCD,eigvecs_DC[i]))
        contribution_ABC *= np.dot(R_BA, R_BA)*np.linalg.norm(np.cross(u_AB,u_BC))**2
        # I have used u_DC, but in eq (17) it is u_CD. I think this should be the same,
        #  for the line below.
        contribution_BCD *= np.dot(R_CD, R_CD)*np.linalg.norm(np.cross(u_BC,u_DC))**2
        force_constant = 1.0/(1.0/contribution_ABC + 1.0/contribution_BCD)
        return force_constant
    
    def _calc_improper_constant(self, atom_idx_A, atom_idx_B, atom_idx_C, atom_idx_D):
        hessian_block_AB = -1.0*self.hessian[3*atom_idx_A:3*atom_idx_A+3,3*atom_idx_B:3*atom_idx_B+3]
        hessian_block_AC = -1.0*self.hessian[3*atom_idx_A:3*atom_idx_A+3,3*atom_idx_C:3*atom_idx_C+3]
        hessian_block_AD = -1.0*self.hessian[3*atom_idx_A:3*atom_idx_A+3,3*atom_idx_D:3*atom_idx_D+3]
        u_BC = self._calc_normal_distance_vector(atom_idx_B, atom_idx_C)
        u_DC = self._calc_normal_distance_vector(atom_idx_D, atom_idx_C)
        u_N = np.cross(u_DC, u_BC)/np.linalg.norm(np.cross(u_DC, u_BC))
        eigvals_AB, eigvecs_AB = np.linalg.eig(hessian_block_AB)
        eigvals_AC, eigvecs_AC = np.linalg.eig(hessian_block_AC)
        eigvals_AD, eigvecs_AD = np.linalg.eig(hessian_block_AD)
        k_AN = 0.0
        for i in range(0, 3):
            k_AN += eigvals_AB[i]*np.abs(np.dot(u_N,eigvecs_AB[i]))
            k_AN += eigvals_AC[i]*np.abs(np.dot(u_N,eigvecs_AC[i]))
            k_AN += eigvals_AD[i]*np.abs(np.dot(u_N,eigvecs_AD[i]))
        force_constant = k_AN*self._calc_point_plane_distance(atom_idx_A, atom_idx_B, atom_idx_C, atom_idx_D)**2
        return force_constant
        
    def get_bond_constant(self, atom_idx_A, atom_idx_B):
        """Atom_idx starts counting from zero."""
        return self._calc_bond_constant(atom_idx_A, atom_idx_B)*self._energy_unit/(self._length_unit**2)
    
    def get_angle_constant(self, atom_idx_A, atom_idx_B, atom_idx_C):
        """Atom_idx starts counting from zero."""
        return self._calc_angle_constant(atom_idx_A, atom_idx_B, atom_idx_C)*self._energy_unit/(self._angle_unit**2)
    
    def get_dihedral_constant(self, atom_idx_A, atom_idx_B, atom_idx_C, atom_idx_D):
        """Atom_idx starts counting from zero."""
        return self._calc_dihedral_constant(atom_idx_A, atom_idx_B, atom_idx_C, atom_idx_D)*self._energy_unit/(self._angle_unit**2)
    
    def get_improper_constant(self, atom_idx_A, atom_idx_B, atom_idx_C, atom_idx_D):
        """Atom_idx starts counting from zero.
        B, C, D are all connected to A. I.e. A is the central atom."""
        return self._calc_improrper_constant(atom_idx_A, atom_idx_B, atom_idx_C, atom_idx_D)*self._energy_unit/(self._angle_unit**2)
    
    def get_bond_length(self, atom_idx_A, atom_idx_B):
        """Atom_idx starts counting from zero."""
        return np.linalg.norm(self._calc_distance_vector(atom_idx_A, atom_idx_B)) * self._length_unit
