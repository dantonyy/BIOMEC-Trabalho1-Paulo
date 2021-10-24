#coding: utf-8
"""
Faculdade de Medicina de Ribeirão Preto - Universidade de São Paulo (FMRP-USP)
Fundamentos de Informática em Biomecânica
Docente: Paulo Santiago
Discentes: Dantony de Castro B. Donato (11845581)
Criado em:
"""

xc1 = [365.8,   365.8,  107]
yc1 = [211,     107,    211]
xp1 = [0,       0,      50.9]
yp1 = [133.9,   50.9,   133.9]
xc2 = [131.4,   131.4,  151.8]
yc2 = [384.8,   151.8,  384.8]
xp2 = [179.4,   179.4,  17.1]
yp2 = [0,       17.1,   0]

print("MENU")
print("1 - Prosseguir com valores pre-definidos")
print("2 - Inserir manualmente valores para calculos")
print("3 - sair")

menu_options = {
    1: 'Option 1',
    2: 'Option 2',
    3: 'Exit',
}
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )
option = int(input('Escolha uma opcao: '))
if option == 1:
    pass
elif option == 2:
    xc1[0] = float(input("xc1 - Valor 1: "))
    xc1[1] = float(input("xc1 - Valor 2: "))
    xc1[2] = float(input("xc1 - Valor 3: "))
    yc1[0] = float(input("yc1 - Valor 1: "))
    yc1[1] = float(input("yc1 - Valor 2: "))
    yc1[2] = float(input("yc1 - Valor 3: "))
    xp1[0] = float(input("xp1 - Valor 1: "))
    xp1[1] = float(input("xp1 - Valor 2: "))
    xp1[2] = float(input("xp1 - Valor 3: "))
    yp1[0] = float(input("yp1 - Valor 1: "))
    yp1[1] = float(input("yp1 - Valor 2: "))
    yp1[2] = float(input("yp1 - Valor 3: "))
    xc2[0] = float(input("xc2 - Valor 1: "))
    xc2[1] = float(input("xc2 - Valor 2: "))
    xc2[2] = float(input("xc2 - Valor 3: "))
    yc2[0] = float(input("yc2 - Valor 1: "))
    yc2[1] = float(input("yc2 - Valor 2: "))
    yc2[2] = float(input("yc2 - Valor 3: "))
    xp2[0] = float(input("xp2 - Valor 1: "))
    xp2[1] = float(input("xp2 - Valor 2: "))
    xp2[2] = float(input("xp2 - Valor 3: "))
    yp2[0] = float(input("yp2 - Valor 1: "))
    yp2[1] = float(input("yp2 - Valor 2: "))
    yp2[2] = float(input("yp2 - Valor 3: "))
    print("Valores inseridos: ")
    print(xc1)
    print(yc1)
    print(xp1)
    print(yp1)
    print(xc2)
    print(yc2)
    print(xp2)
    print(yp2)
else:
    print('Invalid option. Please enter a number between 1 and 4.')

mr1_1 = (yp1[0] - yc1[0]) / (xp1[0] - xc1[0])
mr1_2 = (yp1[1] - yc1[1]) / (xp1[1] - xc1[1])
mr1_3 = (yp1[2] - yc1[2]) / (xp1[2] - xc1[2])

mr2_1 = (yp2[0] - yc2[0]) / (xp2[0] - xc2[0])
mr2_2 = (yp2[1] - yc2[1]) / (xp2[1] - xc2[1])
mr2_3 = (yp2[2] - yc2[2]) / (xp2[2] - xc2[2])

br1_1 = -1 * (mr1_1 * xc1[0] - yc1[0])
br1_2 = -1 * (mr1_2 * xc1[1] - yc1[1])
br1_3 = -1 * (mr1_3 * xc1[2] - yc1[2])

br2_1 = -1 * (mr2_1 * xc2[0] - yc2[0])
br2_2 = -1 * (mr2_2 * xc2[1] - yc2[1])
br2_3 = -1 * (mr2_3 * xc2[2] - yc2[2])

x_1 = round((-(mr2_1 * xc2[0]) + yc2[0] + (mr1_1 * xc1[0]) - yc1[0]) / (mr1_1 - mr2_1), 3)
x_2 = round((-(mr2_2 * xc2[1]) + yc2[1] + (mr1_2 * xc1[1]) - yc1[1]) / (mr1_2 - mr2_2), 3)
x_3 = round((-(mr2_3 * xc2[2]) + yc2[2] + (mr1_3 * xc1[2]) - yc1[2]) / (mr1_3 - mr2_3), 3)

y_1 = round((mr1_1 * x_1) - (mr1_1 * xc1[0]) + yc1[0], 3)
y_2 = round((mr1_2 * x_2) - (mr1_2 * xc1[1]) + yc1[1], 3)
y_3 = round((mr1_3 * x_3) - (mr1_3 * xc1[2]) + yc1[2], 3)

tabx_1 = round((x_1 + x_2) / 2, 3)
tabx_2 = round(159.3, 3)
tabx_3 = round(tabx_2 - tabx_1, 3)
tabx_4 = abs(tabx_3)

taby_1 = round((y_1 + y_3) / 2, 3)
taby_2 = round(168.2, 3)
taby_3 = round(taby_2 - taby_1, 3)
taby_4 = abs(taby_3)

tabz_1 = round((y_2 + x_3) / 2, 3)
tabz_2 = round(74.9, 3)
tabz_3 = round(tabz_2 - tabz_1, 3)
tabz_4 = abs(tabz_3)

erro = round((tabx_4 + taby_4 + tabz_4)/3, 3)

print("X \t\t\t\t Y")
print(x_1,"\t",y_1)
print(x_2,"\t",y_2)
print(x_3,"\t\t",y_3)

print("\t\t\t\tx\t\t\ty\t\t\tz")
print("---------------------------------------------------")
print("REC3D\t\t", tabx_1, "\t", taby_1,  "\t", tabz_1)
print("Real\t\t", tabx_2, "\t\t", taby_2, "\t\t", tabz_2)
print("Erro\t\t", tabx_3, "\t\t", taby_3,  "\t\t", tabz_3)
print("Erro Abs.\t", tabx_4, "\t\t", taby_4,  "\t\t", tabz_4)
print("---------------------------------------------------")
print("Erro Total\t\t\t\t", erro)