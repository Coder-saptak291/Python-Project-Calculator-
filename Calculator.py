N1=float(input("Enter 1st number="))
Op=input("Enter the opeation(+,-,X,/)=")
N2=float(input("Enter 2nd number="))
if Op=='+':
    print(N1,Op,N2,"=",(N1+N2))
elif Op=='-':
    print(N1,Op,N2,"=",(N1-N2))
elif Op=='X':
    print(N1,Op,N2,"=",(N1*N2))
elif Op=='/':
    print(N1,Op,N2,"=",(N1/N2))
