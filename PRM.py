#module1
from re import T
import string
from timeit import repeat


print("Read Me : 1.)An adult may bring upto 2 children")
print("Read Me : 2.)Family Ticket may have may have upto two adults or seniors, and three children")
print("Read Me : 3.)Groups may be of 6 or more peopel and the price is per person")
print("Read Me : C1 = Cost for 1 day" , "C2 = Cost for 2 days")

print("                                                                                                  " )

print("TicketType""| " "C1" " |" " C2")
print("One Adult"" | " "$20" "| " " $30")
print("One Child"" | " "$12" "| " " $18")
print("One Senior""| " "$16" "| " " $24")
print("One Family""| " "$60" "| " " $90")
print("Groups    ""| " "$15" "| " " $22.5")

print("                                                                                                  " )

print("ExtraAttractions" "  |  " "Cost Per Person")
print("Lion feeding"     "      |           " "$2.50")
print("Penguin feeding"     "   |           " "$2.00")
print("Evening Barbeque"     "  |           " "$5.00")
print("                                                                                                  " )
DA = int(input("How many days would you like to stay for ? : "))
print("                                                                                                  " )

if DA <= 2:
   D= int(input("Enter todays date : "))
   print ("You can book for the following day : ", D+1,D+2,D+3,D+4,D+5,D+6,D+7)
elif DA >2:
    int(input("Enter valid number of days : "))

DC= int(input("Pick a date, two consecutive days or one day : "))
if DC >D and DC <D+7:
       print("Booking available, lets proceed further")
elif DC ==D or DC <D or DC >D+7:
    int(input("Enter a Valid Date : "))


    

#module2
BN= 000
if DC <D+8 and DA <= 2:
    print("Enter the following details: ")
A = int(input("The Number of Adults :"))
C = int(input("The Number of Children :"))
if C/A <=2:
    S = int(input("Enter Number of Senior : "))
elif C/A >2:
    int(input("One adult can bring 2 children only please try again "))

if DA ==1:
    T = ( A*20 + C*12 + S*16)
    print("Ticket Cost $",T)

elif DA ==2:
    T =( A*30 + C*18 + S*24)
    print("Ticket Cost $",T)

AR = str(input("would you like any attraction, if nothing then enter NA :"))
if AR ==("Lion"):
    LF = int(input("how many tickets would you like :"))
    L = (LF*2.5)
    print("Cost of attraction", L)
    FC = L+T
    print("Final Bill is : $",FC)
    BN= BN+1
    print("Your Order Number is :", BN)

elif AR ==("Penguin"):
    PF = int(input("how many would you like :"))
    P = (PF*2)
    print("Cost of Attractions : ", P)
    FC = P+T
    print("Final Bill is : $",FC)
    BN= BN+1
    print("Your Order Number is :",BN)

elif AR ==("Barbeque") and DA ==2:
    EB = int(input("how many would you like :"))
    B = (EB*5)
    print("Cost of Attractions : ", B)
    FC = B+T
    print("Final Bill is : $",FC)
    BN= BN+1
    print("Your Order Number is :",BN)

elif AR ==("Barbeque") and DA !=2:
 print("evening barbeque not applicable")

elif AR ==("NA") and DA ==1:
    print("Final Cost $", A*20 + C*12 + S*16)
elif AR ==("NA") and DA ==2:
    print("Final Cost $", A*30 + C*18 + S*24)   

#module3  
print("To save money")
if DA==1:
    FT = 60
elif DA==2:
    FT = 90

if A >=2 or S >=2 and C >=3 and DA ==1:
    FT >FC
    FTX =FC-FT
    print("we recommend you to buy a family ticket of $60 and save : $",FTX)  
elif A >=2 or S >=2 and C >=3 and DA ==2:
    FT >FC
    FTX =FC-FT
    print("we recommend you to buy a family ticket of $90 and save : $",FTX)

    



   
   


    
