
print("Welcome to Rauw Alejandro Concert")
print("The cost of each seat is a follow: VIP= 200$, Arena/Nivel Principal = 95$, Club Seat = 85$")

VIP = int(input("How many tickets sold for VIP?"))

ArenaNivelPrincipal = int(input("How many tickets sold for Arena/Nivel Principal?"))

ClubSeats = int(input("How many tickets sold for Club Seat?"))



def TicketsSold(VIP, ArenaNivelPrincipal, ClubSeats):
    print(f"The cost of all of the VIP tickets sold were: {int(VIP) * 200}")
    print(f"The cost of all of the Arena/Nivel Principal tickets sold were: {int(ArenaNivelPrincipal) * 95}")
    print(f"The cost of all of the Clubs Seat tickets sold  were: {int(ClubSeats) * 85}")



TicketsSold(VIP, ArenaNivelPrincipal , ClubSeats)
sold_VIP = VIP * 183
sold_ANP = ArenaNivelPrincipal * 160
sold_CL = ClubSeats * 150


def TicketsTotal(sold_VIP, sold_ANP, sold_CL):
    print(f"The total of tickets sales is: {int(sold_VIP) + int(sold_ANP) + int(sold_CL)}")

    
TicketsTotal(sold_VIP, sold_ANP, sold_CL)