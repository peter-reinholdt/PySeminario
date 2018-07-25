#!/usr/bin/env python


def parse_itp(itp_name):
    with open(itp_name, "r") as f:
        itp = f.readlines()
    #parse itp and build of lists of bonds, angles, dihedrals and impropers
    bonds = []
    angles = []
    dihedrals = []
    dihedral_multiplicities = []
    impropers = []
    for line in itp:
        #what section are we in?
        split = line.split()
        if line[0] == ";":
            pass
        elif split == []:
            pass
        elif split[0] == "[" and split[2] == "]":
            #new section
            section_name  = split[1]
        elif section_name == "bonds":
            #itp is 1-indexed, but we are 0-indexed
            ai = int(split[0]) - 1
            aj = int(split[1]) - 1
            function_type = int(split[2])
            if function_type == 1:
                bonds.append([ai, aj])
            else:
                raise NotImplementedError('Only works with harmonic bond type')
        elif section_name == "angles":
            ai = int(split[0]) - 1
            aj = int(split[1]) - 1
            ak = int(split[2]) - 1
            function_type = int(split[3])
            if function_type == 1:
                angles.append([ai,aj,ak])
            else:
                raise NotImplementedError('Only works with harmonic angle type')
        elif section_name == "dihedrals":
            ai = int(split[0]) - 1
            aj = int(split[1]) - 1
            ak = int(split[2]) - 1
            al = int(split[3]) - 1
            function_type = int(split[4])
            multiplicity  = int(split[7])
            if function_type == 1:
                dihedrals.append([ai,aj,ak,al])
                dihedral_multiplicities.append(multiplicity)
            elif function_type == 4:
                impropers.append([ai,aj,ak,al])
            else:
                raise NotImplementedError('Only works diheral type 1 or 4')
        else:
            pass
    return bonds, angles, dihedrals, dihedral_multiplicities, impropers
