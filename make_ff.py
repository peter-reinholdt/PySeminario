#!/usr/bin/env python

import argparse
import numpy as np
from seminario import SeminarioMethod

parser = argparse.ArgumentParser(description='Generate force constants based on projections of the Hessian')
parser.add_argument('-i', '--itp', dest='itp', type=str, help='Name of input .itp file', required=True)
parser.add_argument('--fchk', dest='fchk', type=str, default='mol.fchk', help='Name of formatted checkpoint file to put into output .itp')
parser.add_argument('--output-parms',  type=str, dest="output_parms", nargs="+", default=["bonds", "angles", "dihedrals"], 
                    help='Which parameters to calculate from the hessian.')

args = parser.parse_args()

with open(args.itp, "r") as f:
    itp = f.readlines()


Seminario = SeminarioMethod(args.fchk)
Seminario.set_energy_unit('kj/mol')
Seminario.set_length_unit('nm')
Seminario.set_angle_unit('degree')

#parse itp and insert new stuff
for line in itp:
    #what section are we in?
    split = line.split()
    if line[0] == ";":
        print(line, end='')
    elif split == []:
        print(line, end='')
    elif split[0] == "[" and split[2] == "]":
        #new section
        section_name  = split[1]
        print(line, end='')
    #print extracted parameters
    elif section_name == "bonds" and "bonds" in args.output_parms:
        ai = int(split[0]) - 1
        aj = int(split[1]) - 1
        function_type = int(split[2])
        if function_type == 1:
            bond_length = Seminario.get_bond_length(ai, aj)
            bond_constant = Seminario.get_bond_constant(ai, aj)
        else:
            raise NotImplementedError('Only works with harmonic bond type')
        print("{}   {}  {}  {}  {}".format(ai + 1, aj + 1, function_type, bond_length, bond_constant))
    elif section_name == "angles" and "angles" in args.output_parms:
        ai = int(split[0]) - 1
        aj = int(split[1]) - 1
        ak = int(split[2]) - 1
        function_type = int(split[3])
        if function_type == 1:
            Seminario.set_angle_unit('degree')
            angle = Seminario.get_angle(ai,aj,ak)
            Seminario.set_angle_unit('radian')
            angle_constant = Seminario.get_angle_constant(ai, aj, ak)
        else:
            raise NotImplementedError('Only works with harmonic angle type')
        print("{}   {}  {}  {}  {}  {}".format(ai + 1, aj + 1, ak + 1, function_type, angle, angle_constant))
    elif section_name == "dihedrals" and "dihedrals" in args.output_parms:
        ai = int(split[0]) - 1
        aj = int(split[1]) - 1
        ak = int(split[2]) - 1
        al = int(split[3]) - 1
        function_type = int(split[4])
        multiplicity  = int(split[7])
        if function_type == 1:
            Seminario.set_angle_unit('degree')
            dihedral = 999
            Seminario.set_angle_unit('degree')
            dihedral_constant = Seminario.get_dihedral_constant(ai, aj, ak, al)
        elif function_type == 4:
            Seminario.set_angle_unit('degree')
            dihedral = 999
            Seminario.set_angle_unit('degree')
            dihedral_constant = Seminario.get_improper_constant(ai, aj, ak, al)
        else:
            raise NotImplementedError('Only works diheral type 1 or 4')
        print("{}   {}  {}  {}  {}  {}  {}  {}".format(ai + 1, aj + 1, ak + 1, al + 1, 
                                                        function_type, dihedral, dihedral_constant, multiplicity))
    else:
        print(line, end='')
