import numpy as np

class InternalHessian:
    def __init__(self, path_to_fchk):
        """
        Class to exctract force constants for Force Field parameters
        as the diagonal part of the Internal Coordinate Hessian.
        As input this class needs a fchk file that includes the Internal Coordinate Hessian.
        """
        self._energy_unit = 1.0 # baseline is au
        self._length_unit = 1.0 # baseline is au
        self._angle_unit = 1.0 # baseline is radians
        fchk_file = open(path_to_fchk,'r').readlines()
        self._internal_coordinate_indicies_list = []
        self._internal_coordinate_list = []
        self._hessian_list    = []
        # Load in all needed stuff from fchk file
        for i in range(0, len(fchk_file)):
            if "Redundant internal coordinates" in fchk_file[i]:
                self.number_internal_coordinates = int(fchk_file[i].split("=")[1])
                for j in range(i+1, len(fchk_file)):
                    if fchk_file[j][0:1] != " ":
                        # Hope this stop condition always works
                        break
                    self._internal_coordinate_list = self._internal_coordinate_list + fchk_file[j].split()
            if "Redundant internal coordinate indices" in fchk_file[i]:
                for j in range(i+1, len(fchk_file)):
                    if fchk_file[j][0:1] != " ":
                        # Hope this stop condition always works
                        break
                    self._internal_coordinate_indicies_list = self._internal_coordinate_indicies_list + fchk_file[j].split()
            if "Internal Force Constants" in fchk_file[i]:
                for j in range(i+1, len(fchk_file)):
                    if fchk_file[j][0:1] != " ":
                        # Hope this stop condition always works
                        break
                    self._hessian_list = self._hessian_list + fchk_file[j].split()
                    
        self.coordinates = np.array(self._internal_coordinate_list, dtype=float)
        self.hessian = np.zeros((self.number_internal_coordinates, self.number_internal_coordinates))
        
        # Transform internal coordinates indices to array
        bond_list = []
        angle_list = []
        dihedral_list = []
        idx = 0
        for i in range(0, len(self._internal_coordinate_indicies_list), 4):
            a,b,c,d = self._internal_coordinate_indicies_list[i:i+4]
            if c == "0" and d == "0":
                bond_list.append([idx, a, b])
            elif d == "0":
                angle_list.append([idx, a, b ,c])
            else:
                dihedral_list.append([idx, a, b, c, d])
            idx += 1
        self.bond_list = np.array(bond_list, dtype=int)
        self.angle_list = np.array(angle_list, dtype=int)
        self.dihedral_list = np.array(dihedral_list, dtype=int)
        
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
         
        
    def get_bond_constants(self):
        force_constants = []
        for i in range(0, len(self.bond_list)):
            idx = self.bond_list[i,0]
            force_constants.append(self.hessian[idx,idx])
        return np.array(force_constants)*self._energy_unit/(self._length_unit**2)
    
    
    def get_angle_constants(self):
        force_constants = []
        for i in range(0, len(self.angle_list)):
            idx = self.angle_list[i,0]
            force_constants.append(self.hessian[idx,idx])
        return np.array(force_constants)*self._energy_unit/(self._angle_unit**2)
    
    
    def get_dihedral_constants(self):
        force_constants = []
        for i in range(0, len(self.dihedral_list)):
            idx = self.dihedral_list[i,0]
            force_constants.append(self.hessian[idx,idx])
        return np.array(force_constants)*self._energy_unit/(self._angle_unit**2)
    
    
    def get_equilibrium_bond(self):
        equilibrium_value = []
        for i in range(0, len(self.bond_list)):
            idx = self.bond_list[i,0]
            equilibrium_value.append(self.coordinates[idx])
        return np.array(equilibrium_value)*self._length_unit
    
    
    def get_equilibrium_angle(self):
        equilibrium_value = []
        for i in range(0, len(self.angle_list)):
            idx = self.angle_list[i,0]
            equilibrium_value.append(self.coordinates[idx])
        return np.array(equilibrium_value)*self._angle_unit
    
    
    def get_equilibrium_dihedral(self):
        equilibrium_value = []
        for i in range(0, len(self.dihedral_list)):
            idx = self.dihedral_list[i,0]
            equilibrium_value.append(self.coordinates[idx])
        return np.array(equilibrium_value)*self._angle_unit

    
    def get_bond_indicies(self):
        indicies = []
        for i in range(0, len(self.bond_list)):
            indicies.append(self.bond_list[i,1:])
        return np.array(indicies)
    
    
    def get_angle_indicies(self):
        indicies = []
        for i in range(0, len(self.angle_list)):
            indicies.append(self.angle_list[i,1:])
        return np.array(indicies)

    
    def get_dihedral_indicies(self):
        indicies = []
        for i in range(0, len(self.dihedral_list)):
            indicies.append(self.dihedral_list[i,1:])
        return np.array(indicies)