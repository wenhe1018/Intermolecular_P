def calc_u(l1, l2):
    # input: l1 rz in angstrom
    #        l2 qi in e
    # return: list[ux,uy,uz]
    rx = 0.0
    ry = 0.0
    ux = 0
    uy = 0
    uz = 0
    angstrom = 1e-10
    e = 1.60217657e-19
    d = 3.33564e-30
    for i in range(len(l1)):
        ux += l2[i]*e*rx/d
        uy += l2[i]*e*ry/d
        uz += l2[i]*e*l1[i]*angstrom/d
    potential = [ux, uy, uz]
    return potential


def calc_quadrupole(l1, l2):
    theta_zz = 0.0
    angstrom = 1e-10
    e = 1.60217657e-19
    d = 3.33564e-30
    for i in range(len(l1)):
        theta_zz += l2[i]*e*l1[i]*angstrom*l1[i]/d
    return theta_zz


if __name__ == "__main__":
    # l1: rz in angstrom
    # l2: qi in e
    HCN_l1 = [-1.625, -0.557, 0.594]
    HCN_l2 = [0.130, 0.062, -0.192]
    HCNpositive_l2 = [0.247, 0.489, 0.264]
    COO_l1 = [0.000,  1.165, -1.165]
    COO_l2 = [0.330, -0.165, -0.165]
    # (a)
    print(str(calc_u(HCN_l1, HCN_l2)))
    print(str(calc_u(HCN_l1, HCNpositive_l2)))
    print(str(calc_u(COO_l1, COO_l2)))
    # shift +0.5 angstrom
    HCN_l1_shift = [HCN_l1[0]+0.5, HCN_l1[1]+0.5, HCN_l1[2]+0.5]
    COO_l1_shift = [COO_l1[0]+0.5, COO_l1[1]+0.5, COO_l1[2]+0.5]
    # (b)
    print(str(calc_u(HCN_l1_shift, HCN_l2)))
    print(str(calc_u(HCN_l1_shift, HCNpositive_l2)))
    print(str(calc_u(COO_l1_shift, COO_l2)))
    # (c)
    # (d)
    print(str(calc_quadrupole(HCN_l1, HCN_l2)))
    print(str(calc_quadrupole(HCN_l1, HCNpositive_l2)))
    print(str(calc_quadrupole(COO_l1, COO_l2)))
    print(str(calc_quadrupole(HCN_l1_shift, HCN_l2)))
    print(str(calc_quadrupole(HCN_l1_shift, HCNpositive_l2)))
    print(str(calc_quadrupole(COO_l1_shift, COO_l2)))
