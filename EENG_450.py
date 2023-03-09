# EENG 450 Python
import cmath
import math

##############################################################
#
# Name:
#
def printMagPhase(var, z):
    print(var + f' = {abs(z):.4f}...{cmath.phase(z)*180/3.1415926:.4f} degrees')

##############################################################
#
# Name:
#
def pblm_09_07():
    print(f'Sample Problems Power Flow Example 9.7\n')
 
    Ir = complex(116.6*math.cos(-25.8*math.pi/180), 116.6*math.sin(-25.8*math.pi/180))
    print(f'Ir = {abs(Ir):.4f} ... {cmath.phase(Ir)*180/3.1415926:.4f}')

    z = complex(35,140)
    print(f'Z = {z}')

    y = complex(0, 930e-6)
    print(f'Y = {y}')

    A = z*y/2 + 1
    print(f'A = D = {abs(A):.4f} ... {cmath.phase(A)*180/3.1415926:.4f}')

    B = z
    print(f'B = {B:.4f}')
    print(f'B = {abs(B):.4f} ... {cmath.phase(B)*180/3.1415926:.4f}')

    C = y*(z*y/4 + 1)
    print(f'C = {abs(C):.4f} ... {cmath.phase(C)*180/3.1415926:.4f}')

    D = A

    Vr_ln = complex(220000/math.sqrt(3), 0.0)

    Vs_ln = A*Vr_ln + B*Ir
    printMagPhase("Vs_ln", Vs_ln)

    Is = C*Vr_ln + D*Ir
    printMagPhase("Is", Is)

##############################################################
#
# Name:
#
def pblm_09_08():
    print(f'Sample Problems Power Flow Example 9.8\n')

    Ir = complex(116.6*math.cos(-25.8*math.pi/180), 116.6*math.sin(-25.8*math.pi/180))/131.2
    printMagPhase("Ir", Ir)

    z = complex(35,140)/968
    print(f'\nZ = {z:.4f}')
    printMagPhase("Z", z)
    #
    y = complex(0, 930e-6)/1033e-6
    print(f'Y = {y:.4f}')
    printMagPhase("Y", y)
    #
    A = z*y/2 + 1
    printMagPhase("\nA", A)
    #
    B = z
    print(f'B = {B:.4f}')
    printMagPhase("B", B)
    #
    C = y*(z*y/4 + 1)
    printMagPhase("C", C)
    #
    D = A
    #
    Vr_ln = complex(1.0, 0.0)

    Vs_ln = A*Vr_ln + B*Ir
    printMagPhase("\nVs_ln", Vs_ln)

    Is = C*Vr_ln + D*Ir
    printMagPhase("Is", Is)

##############################################################
#
# Name:
#
def pblm_09_13():
    print(f'Sample Problems Power Flow Example 9.13\n')
    z = complex(35,140)

    Pr = 40e06
    pf = 0.9

    Sbase = 100e06
    print(f'Sbase = {Sbase}')

    Vbase_ll = 220e03
    print(f'Vbase_ll = {Vbase_ll}')

    Vbase_ln = 220e03/math.sqrt(3)
    printMagPhase("Vbase_ln", Vbase_ln)

    Ibase = Sbase/(math.sqrt(3)*Vbase_ll)
    printMagPhase("Ibase", Ibase)

    Zbase = Vbase_ll/(math.sqrt(3)*Ibase)
    print(f'Zbase = {Zbase}')

    q_amp = Pr/pf
    q_phase = 0 + math.acos(0.9)
    Sr = complex(q_amp*math.cos(q_phase), q_amp*math.sin(q_phase))
    printMagPhase("Sr", Sr)

    Sr_pu = Sr/Sbase
    printMagPhase("Sr_pu", Sr_pu)

    Ir_pu = Sr.conjugate()/(math.sqrt(3)*Vbase_ll*Ibase)
    printMagPhase("Ir_pu", Ir_pu)

    Z_pu = z/Zbase
    printMagPhase("Z", z)
    printMagPhase("Zbase", Zbase)
    printMagPhase("Z_pu", Z_pu)


    Vr_ln = complex(1.0, 0.0)
    #
    Vs_ln = Vr_ln + Z_pu*Ir_pu
    printMagPhase("Vs_ln", Vs_ln)

    Is = Ir_pu*Ibase
    printMagPhase("Is", Is)

##############################################################
#
# Name:
#
def pblm_10_03():
    print(f'Sample Problems Power Flow Example 10.3\n')

    # Power Specs
    SD3 = complex(0.40, 0.30)
    print(SD3)
    SD4 = complex(0.80, 0.60)
    print(SD4)

    P2 = complex(0.75, 0.00)

    # Voltage Flat Start

    V1_0 = cmath.rect(1.00, 0.0)
    V2_0 = cmath.rect(1.02, 0.0)
    V3_0 = cmath.rect(1.00, 0.0)
    V4_0 = cmath.rect(1.00, 0.0)

    # Grid Transmission lines, etc.

    Z12 = complex(0.01, 0.05)
    Y1 = complex(0.0, 0.30)

    Z23 = complex(0.03, 0.15)
    Y2 = complex(0.0, 0.90)

    Xt = complex(0.0, 0.10)

    # Admittance matrix elements

    Y12 = Y21 = -1/Z12
    Y13 = Y31 = Y14 = Y41 = Y24 = Y42 = complex(0.0, 0.0)
    Y23 = Y32 = -1/Z23
    Y34 = -1/Xt
    Y11 = -Y12 + Y1/2
    Y22 = -Y21 - Y23 + Y1/2 + Y2/2
    Y33 = -Y23 + Y2/2 - Y34
    Y44 = - Y34

    printMagPhase("V1_0", V1_0)
    printMagPhase("V2_0", V2_0)
    printMagPhase("V3_0", V3_0)
    printMagPhase("V4_0", V4_0)
    print('')

    printMagPhase("Y21", Y21)
    printMagPhase("Y22", Y22)
    printMagPhase("Y23", Y23)
    printMagPhase("Y24", Y24)
    print('')

    SP2_c = V2_0.conjugate()*(Y21*V1_0 +Y22*V2_0 + Y23*V3_0 + Y24*V4_0)
    printMagPhase("SP2_conj", SP2_c)
    print(SP2_c)
    Q2 = -SP2_c.imag
    print(f'Q2 = {Q2:.4f}')

    V1_1 = V1_0
    V2_1 = (1/Y22)*((P2-Q2)/(V2_0.conjugate()) - Y21*V1_1 - Y23*V3_0 - Y24*V4_0)
    printMagPhase("V2_1", V2_1)
    #V3_2 = cmath.rect(1.00, 0.0)
    #V4_3 = cmath.rect(1.00, 0.0)


##############################################################
#
# Name:
#
def main():

    print("EENG 450: POWER SYSTEMS\n")
    #pblm_09_07()
    #pblm_09_08()
    pblm_09_13()
    #pblm_10_03()

if __name__ == "__main__":
    main()
