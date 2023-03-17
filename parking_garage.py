class ParkingGarage():
    """
        this class contains information about a user and how many parking passes 
        they hold and how much it costs to purchase more passes
    """

    def __init__(self, tickets = 10, spaces = 10):
        self.tickets = list(range(tickets))
        self.parking_spaces = list(range(spaces))
        self.current_ticket = {'paid': False}

    def take_ticket(self):
        self.tickets.pop()
        self.parking_spaces.pop()

    def pay_for_parking(self):
        self.payment = input("Please pay for parking  ")
        if int(self.payment) >= 10:
            self.current_ticket['paid'] = True
            print("The ticket has been paid. You have 15 minutes to leave")

    def leave_garage(self):
        while True:
            if self.current_ticket['paid']:
                print("Thank you, have a nice day")
                self.tickets.append(1)
                self.parking_spaces.append(1)
                break

            else:
                ParkingGarage.pay_for_parking(self)

my_garage = ParkingGarage()

my_garage.take_ticket()
my_garage.pay_for_parking()
my_garage.leave_garage()