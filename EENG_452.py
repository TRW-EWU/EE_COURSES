import numpy as np
import matplotlib.pyplot as plt

###############################################################
# EENG 452
# Name: Thomas R. Walsh
# Date: 12/18/2020
#

###################################################
# Procedures, Functions, Methods, ...
#



 ##################################################
# Main program starts here
#
def main():
    print("EENG 452 Python Programs")
    z = 1 + 1j
    print(z)
    print(np.real(z))
    print(np.imag(z))
    print(np.angle(z))
    print(np.angle(z)*180/3.1415926)

if __name__ == "__main__":
    main()

