from restaurant_reservation_system.branch import Branch
from restaurant_reservation_system.address import Address
from restaurant_reservation_system.menu import Menu
from restaurant_reservation_system.menuItem import MenuItem
from restaurant_reservation_system.chef import Chef
from restaurant_reservation_system.manager import Manager
from restaurant_reservation_system.receptionist import Receptionist
from restaurant_reservation_system.waiter import Waiter
from restaurant_reservation_system.admin import SystemAdmin
from restaurant_reservation_system.customer import Customer
from restaurant_reservation_system.reservation import Reservation
from restaurant_reservation_system.table import Table
from restaurant_reservation_system.table_seat import TableSeat
from restaurant_reservation_system.restaurant_system import RestaurantManagementSystem

# Create an instance of the RestaurantManagementSystem
restaurant_system = RestaurantManagementSystem()

# Create some sample data for the restaurant
menu_item1 = MenuItem(menuItemID=1, title="Burger", description="Delicious burger", price=100.99)
menu_item2 = MenuItem(menuItemID=2, title="Pizza", description="Margherita pizza", price=150.99)

menu1 = Menu()
menu1.addMenuItem(menu_item1)
menu1.addMenuItem(menu_item2)

print(f"Display Menu")
menu_list = menu1.getAllMenuItems()
for result in menu_list:
        print(f"{result.getMenuItemID()}. Title: {result.getTitle()}, Description: {result.getDescription()}, Price: {result.getPrice()}")

# Create a branch for the restaurant
manager1 = Manager(name="Alice Johnson", email="alice@example.com", phone="555-555-5555", employeeID=3, dateJoined="2022-03-01")
address1 = Address(streetAddress="123 Main St", city="City1", state="State1", zipCode="12345", country="Country1")
branch1 =  Branch(branchId = 1, name = 'Branch01',location=address1)

# Add the branch to the restaurant system
restaurant_system.addNewClient(branch1)

chef1 = Chef(name="John Doe", email="john@example.com", phone="123-456-7890", employeeID=1, dateJoined="2022-01-01")
receptionist1 = Receptionist(name="Bob Brown", email="bob@example.com", phone="111-222-3333", employeeID=4, dateJoined="2022-04-01")
waiter1 = Waiter(name="Eva White", email="eva@example.com", phone="444-444-4444", employeeID=5, dateJoined="2022-05-01")
admin1 = SystemAdmin(name="Admin", email="admin@example.com", phone="999-999-9999", employeeID=6, dateJoined="2022-06-01")
branch1.setMenu(menu1)
branch1.addManager(manager1)
branch1.addChef(chef1)
branch1.addReceptionist(receptionist1)
branch1.addWaiter(waiter1)

# Make a reservation
reservation = Reservation(reservationID=1)
reservation.updatePeopleCount(4)

# Create a table for the reservation
table1 = Table(tableID=1, maxCapacity=4, locationIdentifier="Table1", seats=[TableSeat(id=1), TableSeat(id=2), TableSeat(id=3), TableSeat(id=4)])

# Create a customer
customer1 = Customer(phoneNumber="555-1234", email="customer@example.com", name="John Kraus")
receptionist1.createReservation(reservation, customer1, branch1, table1, reservingTableCharge = 50)

#cancel reservation
#receptionist1.cancelReservation(reservation, branch1, table1)

# Create a table order for the reservation
order = customer1.makeTableOrder(branch1, table1, menu_item1)

#Try cancel after checking-in 
receptionist1.cancelReservation(reservation, customer1, branch1, table1)

# Create a payment for the table order
customer1.makePayment(order)