#!/usr/bin/env python


import parmed


def get_indices(itp_name):
    itp = parmed.load_file(itp_name)
    #indices
    bond_indices = []
    angle_indices = []
    dihedral_indices = []
    improper_indices = []
    #equivalent parameters
    bond_symmetries = []
    angle_symmetries = []
    dihedral_symmetries = []
    #periodicities
    dihedral_multiplicities = []
    for bond in itp.bonds:
        if bond.funct == 1:
            bond_indices.append([bond.atom1.idx, bond.atom2.idx])
        else:
            raise NotImplementedError('Unknown bond function type')
    for angle in itp.angles:
        if angle.funct == 1:
            angle_indices.append([angle.atom1.idx, angle.atom2.idx, angle.atom3.idx])
        else:
            raise NotImplementedError('Unknown angle function type')
    for dihedral in itp.dihedrals:
        if dihedral.funct == 1:
            dihedral_indices.append([dihedral.atom1.idx, dihedral.atom2.idx, dihedral.atom3.idx])
            dihedral_multiplicities.append([dihedral.type.per])
        elif dihedral.funct == 4:
            improper_indices.append([dihedral.atom1.idx, dihedral.atom2.idx, dihedral.atom3.idx])
        else:
            raise NotImplementedError('Unknown dihedral function type')
    
    for bond_type in itp.bond_types:
        symmetry = []
        for index, bond in enumerate(itp.bonds):
            if bond.type == bond_type:
                symmetry.append(index)
        bond_symmetries.append(symmetry)

    for angle_type in itp.angle_types:
        symmetry = []
        for index, angle in enumerate(itp.angles):
            if angle.type == angle_type:
                symmetry.append(index)
        angle_symmetries.append(symmetry)

    for dihedral_type in itp.dihedral_types:
        symmetry = []
        for index, dihedral in enumerate(itp.dihedrals):
            if dihedral.type == dihedral_type:
                symmetry.append(index)
        dihedral_symmetries.append(symmetry)
    return bond_indices, angle_indices, dihedral_indices, improper_indices, dihedral_multiplicities, bond_symmetries, angle_symmetries, dihedral_symmetries
