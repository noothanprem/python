"""

Name     : Harmonic.py
Date     : 26/08/2019
Purpose  :  Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N

"""

from Utility import utility

while True:
    try:
        #Taking the input value from the user
        n=int(input("Enter the harmonic value : "))
        harm=0.0
        #calling the function in the BL file
        harm=utility.harmonic(n)
        print("Harmonic value : ",harm)
        break
    except ValueError:
        print("Please enter number only")

