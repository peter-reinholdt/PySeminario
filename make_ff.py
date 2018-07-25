#!/usr/bin/env python

import argparse
import numpy as np
import parmed
from parsers import get_indices
from seminario import SeminarioMethod
from fullhessianfit import FullHessianFit

parser = argparse.ArgumentParser(description='Generate force constants based on projections of the Hessian')
parser.add_argument('-i', '--itp', dest='itp', type=str, 
        help='Name of input .itp file', required=True)

parser.add_argument('-o', dest='out', type=str, default='out.top',
        help='Name of output parameter file')

parser.add_argument('--fchk', dest='fchk', type=str, required=True,
        help='Name of formatted checkpoint file to put into output .itp')

parser.add_argument('--parameter-type', dest='parmtype', default="seminario", 
        help='Parameter type to use',
        choices=['seminario', 'seminario_modified', 'hessian_fit'])


args = parser.parse_args()
itp = parmed.load_file(args.itp)
bond_indices, angle_indices, dihedral_indices, improper_indices, dihedral_multiplicities, bond_symmetries, angle_symmetries, dihedral_symmetries = get_indices(args.itp)


if args.parmtype.lower() == 'seminario' or args.parmtype.lower() == "seminario_modified":
    #only the angle term is different
    Seminario = SeminarioMethod(args.fchk)
    Seminario.set_energy_unit('kcal/mol')
    Seminario.set_length_unit('angstrom')
    Seminario.set_angle_unit('degree')
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
    angles_b = []
    angles_k = []
    if args.parmtype.lower() == 'seminario':
        for angle_idx in angle_indices:
            Seminario.set_angle_unit('degree')
            angles_b.append(Seminario.get_angle(*angle_idx))
            Seminario.set_angle_unit('radian')
            angles_k.append(Seminario.get_angle_constant(*angle_idx))
    elif args.parmtype.lower() == 'seminario_modified':
        Seminario.set_angle_unit('degree')
        for angle_idx in angle_indices:
            angles_b.append(Seminario.get_angle(*angle_idx))
        Seminario.set_angle_unit('radian')
        angles_k = Seminario.get_modified_angle_constant(angle_indices)
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

elif args.parmtype.lower() == 'hessian_fit':
    HessianFit = FullHessianFit(args.fchk, bond_indices, angle_indices, dihedral_indices, dihedral_multiplicities, improper_indices)
    HessianFit.fit_parameters()
    HessianFit.set_energy_unit('kcal/mol')
    HessianFit.set_length_unit('angstrom')
    HessianFit.set_angle_unit('radian')
    bonds_k = HessianFit.get_bond_constants()
    angles_k = HessianFit.get_angle_constants()
    dihedrals_k = HessianFit.get_dihedral_constants()
    impropers_k = HessianFit.get_improper_constants()
    HessianFit.set_angle_unit('degree')
    bonds_b = HessianFit.get_bond_length()
    angles_b = HessianFit.get_angle()
    dihedrals_b = HessianFit.get_dihedral()
    impropers_b = HessianFit.get_improper()

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

itp.save(args.out, overwrite=True)
