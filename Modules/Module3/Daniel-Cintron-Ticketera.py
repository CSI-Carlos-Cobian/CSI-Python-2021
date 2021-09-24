print("Miss World 2021")
print("The cost of each seat is as follow: Club Seat = $350, Nivel Principal = $350, Nivel Superior = $75")

Club_Seat = int(input("How many tickets sold for Club Seat? ="))
Nivel_Principal = int(input("How many tickets sold for Nivel Principal="))
Nivel_Superior = int(input("How many tickets sold for Nivel Superior="))

def SectionSales(Club_Seat, Nivel_Principal, Nivel_Superior):
 print(f"The cost for Club Seat Tickets is: {int(Club_Seat) * 350}")  
 print(f"The cost for Nivel Principal Tickets is: {int(Nivel_Principal) * 350}")  
 print(f"The cost for Nivel Superior Tickets is:  {int(Nivel_Superior) *75}")
 print()
SectionSales(Club_Seat, Nivel_Principal, Nivel_Superior)
Sales_CS = Club_Seat * 350
Sales_NP = Nivel_Principal * 350
Sales_NS = Nivel_Superior * 75
def TicketsTotal( Sales_CS, Sales_NP, Sales_NS): 
        print(f"The total of tickets sales is ${int(Sales_CS) + int(Sales_NP) + int(Sales_NS)}")
print()
TicketsTotal(Sales_CS, Sales_NP, Sales_NS) 