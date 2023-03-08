# EENG 450 Python
import cmath
import math



def printMagPhase(var, z):
    print(var + f' = {abs(z):.4f}...{cmath.phase(z)*180/3.1415926:.4f} degrees')

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


def main():

    print("EENG 450: POWER SYSTEMS\n")
    pblm_10_03()

if __name__ == "__main__":
    main()
