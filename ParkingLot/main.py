from parkingLot.parking_lot import ParkingLot
from parkingLot.motorcycle_spot import MotorcycleSpot
from parkingLot.compact_spot import CompactSpot
from parkingLot.compactCar import CompactCar
from parkingLot.electricCar import ElectricCar
from parkingLot.motocycle import Motorcycle
from parkingLot.kiosk import EntranceKiosk, ExitKiosk
from parkingLot.parking_ticket import ParkingTicket
from parkingLot.parking_ticket import ParkingTicket
from parkingLot.parking_floor import ParkingFloor

def main():
    # Create Parking Lot
    parking_lot = ParkingLot.getInstance()

    # Create Parking Floors
    floor1 = ParkingFloor(floorId=1)
    parking_lot.addParkingFloor(floor1)

    #Available floors
    available_floors = parking_lot.getParkingFloors()
    print("Available Floors in My Parking Lot are:- ")
    for floor in available_floors:
        print(f"FloorID: {floor.getFloorID()}")


    # Create Parking Spots
    compact_spot = CompactSpot(spotNumber="C01", isHandicappedSpot=False, parkingFloor=floor1)
    motorcycle_spot = MotorcycleSpot(spotNumber="M01", isHandicappedSpot=False, parkingFloor=floor1)

    # Add Parking Spots to Parking Floor
    floor1.addParkingSpot(compact_spot)
    floor1.addParkingSpot(motorcycle_spot)

    #Available spots in particular floor
    print("Available spots in My Parking Lot are:- ")
    floor1.getAllParkingSpots()

    # Create Vehicles
    compact_car = CompactCar(licenseNumber="ABC123", isHandicapped=False)
    motorcycle = Motorcycle(licenseNumber="XYZ789", isHandicapped=True)
    motorcycle1 = Motorcycle(licenseNumber="XYZ780", isHandicapped=False)
    electric_car =  ElectricCar(licenseNumber="XYZ789", isHandicapped=False)

    # Create Entrance and Exit Kiosks
    entrance_kiosk = EntranceKiosk(kioskId=1)
    exit_kiosk = ExitKiosk(kioskId=2)

    # Add Kiosks to Parking Lot
    parking_lot.addNewEntrance(entrance_kiosk)
    parking_lot.addNewExit(exit_kiosk)

    # Simulate Vehicle Entry and Ticket Issuance
    entrance_kiosk.issueTicket(vehicle=compact_car)

    # park vehicle
    floor1.parkVehicle(compact_car)
    floor1.parkVehicle(motorcycle)

    # check if parkingLot is full
    if parking_lot.isFull():
        print("My Parking Lot is Fulll!!")
    else:
        print("Spots available, please check available spots.")
    #Available spots in particular floor
    print("Available spots in My Parking Lot are:- ")
    floor1.getAllParkingSpots()

    # Simulate Vehicle Exit and Payment Processing
    parking_ticket = ParkingTicket(barcode="TICKET123")
    floor1.freeSpot(compact_spot)
    exit_kiosk.processPayment(ticket=parking_ticket,customerCreditCard =None)
    print("Available spots in My Parking Lot are:- ")
    floor1.getAllParkingSpots()

if __name__ == "__main__":
    main()