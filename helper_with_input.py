from mailmerge import MailMerge


def get_values_mixte():
    template = MailMerge("moulage_temp.docx")
    name = str(input("Nom et prénom du patient: "))
    age = str(input("Age du patient: "))
    overjet = float(input("Overjet: "))
    overbite = float(input("Overbite: "))

    ######################  Superieure
    _11 = float(input("diam MD de la 11: "))
    _12 = float(input("diam MD de la 12: "))
    _21 = float(input("diam MD de la 21: "))
    _22 = float(input("diam MD de la 22: "))
    _16 = float(input("diam MD de la 16: "))
    l_sup_m = float(input("longueur d'arcade supérieure: "))
    d4g4_sup_m = float(input("D4G4 supérieure: "))
    d6g6_sup_m = float(input("D6G6 supérieure: "))
    l_base = float(input("Longeur de base maxillaire: "))
    ED_sup = float(input("Espace disponible supérieure: ")) - 1.8

    #######################  Inferieure
    _31 = float(input("diam MD de la 31: "))
    _32 = float(input("diam MD de la 32: "))
    _41 = float(input("diam MD de la 41: "))
    _42 = float(input("diam MD de la 42: "))
    l_inf_m = float(input("longueur d'arcade inférieure: "))
    d4g4_inf_m = float(input("D4G4 inférieure: "))
    d6g6_inf_m = float(input("D6G6 inférieure: "))
    ED_inf = float(input("Espace disponible inférieure: ")) - 3.4

    #######################  Calcules
    EN_inf_TJ = 2 * (_31 + _32 + _41 + _42) + 21
    EN_sup_TJ = (_11 + _12 + _21 + _22) + (_31 + _32 + _41 + _42) + 22
    p10 = (_11 + _16) * 3.85
    p14 = (_11 + _16) * 5.95

    l_sup_t = round((p10 / 2.58), 2)
    l_inf_t = round((p10 / 3.10), 2)
    d4g4_sup_t = round((p14 * 0.32), 2)
    d6g6_sup_t = round((p14 * 0.4), 2)
    d4g4_inf_t = round((p10 / 2.32), 2)
    d6g6_inf_t = round((p10 / 1.76), 2)

    ddm_sup = ED_sup - EN_sup_TJ
    ddm_inf = ED_inf - EN_inf_TJ

    #######################  Merge
    template.merge(name=name, age=age, overbite=str(overbite), overjet=str(overjet),
                   p10=str(p10), p14=str(p14), d4g4_sup_m=str(d4g4_sup_m), d4g4_sup_t=str(d4g4_sup_t),
                   d6g6_sup_m=str(d6g6_sup_m), d6g6_sup_t=str(d6g6_sup_t), l_sup_m=str(l_sup_m),
                   l_sup_t=str(l_sup_t), l_base=str(l_base), ddm_sup=str(ddm_sup))
    template.merge(d4g4_inf_m=str(d4g4_inf_m), d4g4_inf_t=str(d4g4_inf_t),
                   d6g6_inf_m=str(d6g6_inf_m), d6g6_inf_t=str(d6g6_inf_t), l_inf_m=str(l_inf_m),
                   l_inf_t=str(l_inf_t), ddm_inf=str(ddm_inf))
    template.write("{}.docx".format(name))


def get_values_adolecente():
    template = MailMerge("moulage_temp.docx")
    name = str(input("Nom et prénom du patient: "))
    age = str(input("Age du patient: "))
    overjet = float(input("Overjet: "))
    overbite = float(input("Overbite: "))

    ######################  Superieure
    _11 = float(input("diam MD de la 11: "))
    _12 = float(input("diam MD de la 12: "))
    _13 = float(input("diam MD de la 13: "))
    _14 = float(input("diam MD de la 14: "))
    _15 = float(input("diam MD de la 15: "))
    _21 = float(input("diam MD de la 21: "))
    _22 = float(input("diam MD de la 22: "))
    _23 = float(input("diam MD de la 23: "))
    _24 = float(input("diam MD de la 24: "))
    _25 = float(input("diam MD de la 25: "))
    _16 = float(input("diam MD de la 16: "))
    l_sup_m = float(input("longueur d'arcade supérieure: "))
    d4g4_sup_m = float(input("D4G4 supérieure: "))
    d6g6_sup_m = float(input("D6G6 supérieure: "))
    l_base = float(input("Longeur de base maxillaire: "))
    if (_14 + _15 + _24 + _25 == 0):
        ED_sup = float(input("Espace disponible supérieure: ")) - 1.8
    if (_14 + _15 == 0) and (_24 + _25 != 0):
        ED_sup = float(input("Espace disponible supérieure: ")) - 0.9
    if (_14 + _15 != 0) and (_24 + _25 != 0):
        ED_sup = float(input("Espace disponible supérieure: "))

    #######################  Inferieure
    _31 = float(input("diam MD de la 31: "))
    _32 = float(input("diam MD de la 32: "))
    _33 = float(input("diam MD de la 33: "))
    _34 = float(input("diam MD de la 34: "))
    _35 = float(input("diam MD de la 35: "))
    _41 = float(input("diam MD de la 41: "))
    _42 = float(input("diam MD de la 42: "))
    _43 = float(input("diam MD de la 43: "))
    _44 = float(input("diam MD de la 44: "))
    _45 = float(input("diam MD de la 45: "))
    l_inf_m = float(input("longueur d'arcade inférieure: "))
    d4g4_inf_m = float(input("D4G4 inférieure: "))
    d6g6_inf_m = float(input("D6G6 inférieure: "))
    if (_34 + _35 + _44 + _45 == 0):
        ED_inf = float(input("Espace disponible supérieure: ")) - 3.4
    if (_34 + _35 == 0) and (_44 + _45 != 0):
        ED_inf = float(input("Espace disponible supérieure: ")) - 1.7
    if (_34 + _35 != 0) and (_44 + _45 != 0):
        ED_inf = float(input("Espace disponible supérieure: "))

    #######################  Calcules
    if _13 == 0 and _23 !=0:
        _13 == _23
    if _23 == 0 and _13 != 0:
        _23 == _13

    if _14 == 0 and _24 !=0:
        _14 == _24
    if _24 == 0 and _14 != 0:
        _24 == _14

    if _15 == 0 and _25 !=0:
        _15 == _25
    if _25 == 0 and _15 != 0:
        _25 == _15

    EN_inf_TJ = _31 + _32 + _33 + _34 + _35 + _41 + _42 + _43 + _44 + _45
    EN_sup_TJ = _11 + _12 + _13 + _14 + _15 + _21 + _22 + _23 + _24 + _25
    p10 = (_11 + _14 + _16) * 2.84
    p14 = (_11 + _14 + _16) * 4.4
    l_sup_t = round((p10 / 2.58), 2)
    l_inf_t = round((p10 / 3.10), 2)
    d4g4_sup_t = round((p14 * 0.32), 2)
    d6g6_sup_t = round((p14 * 0.4), 2)
    d4g4_inf_t = round((p10 / 2.32), 2)
    d6g6_inf_t = round((p10 / 1.76), 2)
    ddm_sup = round((ED_sup - EN_sup_TJ), 2)
    ddm_inf = round((ED_inf - EN_inf_TJ), 2)

    #######################  Merge
    template.merge(name=name, age=age, overbite=str(overbite), overjet=str(overjet),
                   p10=str(p10), p14=str(p14), d4g4_sup_m=str(d4g4_sup_m), d4g4_sup_t=str(d4g4_sup_t),
                   d6g6_sup_m=str(d6g6_sup_m), d6g6_sup_t=str(d6g6_sup_t), l_sup_m=str(l_sup_m),
                   l_sup_t=str(l_sup_t), l_base=str(l_base), ddm_sup=str(ddm_sup))
    template.merge(d4g4_inf_m=str(d4g4_inf_m), d4g4_inf_t=str(d4g4_inf_t),
                   d6ag6_inf_m=str(d6g6_inf_m), d6g6_inf_t=str(d6g6_inf_t), l_inf_m=str(l_inf_m),
                   l_inf_t=str(l_inf_t), ddm_inf=str(ddm_inf))
    template.write("{}.docx".format(name))


if __name__ == '__main__':
    denture = input("mixte (m), adolecente (a), permanente (p): ")
    if str(denture) == "m":
        get_values_mixte()
    if str(denture) == "a":
        get_values_adolecente()
