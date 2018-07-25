#!/usr/bin/env python

import argparse
import numpy as np
import parmed
from parsers import get_indices
from seminario import SeminarioMethod

parser = argparse.ArgumentParser(description='Generate force constants based on projections of the Hessian')
parser.add_argument('-i', '--itp', dest='itp', type=str, 
        help='Name of input .itp file', required=True)

parser.add_argument('-o', dest='out', type=str, default='out.top',
        help='Name of output parameter file')

parser.add_argument('--fchk', dest='fchk', type=str, required=True,
        help='Name of formatted checkpoint file to put into output .itp')

parser.add_argument('--parameter-type', dest='parmtype', default="seminario", 
        help='Parameter type to use. Options are: seminario, seminario_modified, hessian_fit')

parser.add_argument('--output-parms',  type=str, dest="output_parms", nargs="+", default=["bonds", "angles", "dihedrals"], 
                    help='Which parameters to calculate from the hessian.')

args = parser.parse_args()
itp = parmed.load_file(args.itp)
bond_indices, angle_indices, dihedral_indices, improper_indices, dihedral_multiplicities, bond_symmetries, angle_symmetries, dihedral_symmetries = get_indices(args.itp)


if args.parmtype.lower() == 'seminario':
    Seminario = SeminarioMethod(args.fchk)
    #make sure this is appropriate
    Seminario.set_energy_unit('kcal/mol')
    Seminario.set_length_unit('angstrom')
    Seminario.set_angle_unit('degree')
    if 'bonds' in args.output_parms:
        bonds_b = []
        bonds_k = []
        for bond_idx in bond_indices:
            bonds_b.append(Seminario.get_bond_length(*bond_idx))
            bonds_k.append(Seminario.get_bond_constant(*bond_idx))
        #update itp (taking into account equivalent bond terms)
        for index, bond_type in enumerate(itp.bond_types):
           k = 0.0
           req = 0.0
           for equivalent in bond_symmetries[index]:
               k += bonds_k[equivalent]
               req += bonds_b[equivalent]
           k = k / len(bond_symmetries[index])
           req = req / len(bond_symmetries[index])
           bond_type.k = k
           bond_type.req = req
    if 'angles' in args.output_parms:
        angles_b = []
        angles_k = []
        for angle_idx in angle_indices:
            angles_b.append(Seminario.get_angle(*angle_idx))
            angles_k.append(Seminario.get_angle_constant(*angle_idx))
        #update itp (taking into account equivalent bond terms)
        for index, angle_type in enumerate(itp.angle_types):
           k = 0.0
           theteq = 0.0
           for equivalent in angle_symmetries[index]:
               k += angles_k[equivalent]
               theteq += angles_b[equivalent]
           k = k / len(angle_symmetries[index])
           theteq = theteq / len(angle_symmetries[index])
           angle_type.k = k
           angle_type.theteq = theteq
    if 'diherals' in args.output_parms:
        raise NotImplementedError('Currently, the seminario method does not support dihedral terms')

elif args.parmtype.lower() == 'seminario_modified':
    pass
elif args.parmtype.lower() == 'hessian_fit':
    pass

itp.save(args.out)
