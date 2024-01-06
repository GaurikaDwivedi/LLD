from car_rental_system.CarRentalsystem import CarRentalsystem
from car_rental_system.carRentalLocation import CarRentalLocation
from car_rental_system.driverLicense import DriverLicense
from car_rental_system.customer import Customer
from car_rental_system.carType import EconomyCar
from car_rental_system.payment import Payment, PaymentStatus
from car_rental_system.reservation import Reservation
from car_rental_system.rentalInsurance import RentalInsurance, InsuranceCoverageType
from car_rental_system.admin import Administrator

def main():
    # Initialize the car rental system
    car_rental_system = CarRentalsystem()

    # Create a few locations
    location1 = CarRentalLocation(locationId=1, locationName="Location A", streetAddress="123 Main St", city="City1", state="State1", zipCode="12345", country="Country1")
    location2 = CarRentalLocation(locationId=2, locationName="Location B", streetAddress="456 Oak St", city="City2", state="State2", zipCode="67890", country="Country2")

    # Add locations to the system
    car_rental_system.addNewLocation(location1)
    car_rental_system.addNewLocation(location2)

    # Create an administrator
    admin_employee_id = "A123"
    admin_name = "Admin Name"
    admin_email = "admin@example.com"
    admin_phone = "987-654-3210"

    administrator = Administrator(employeeId=admin_employee_id, name=admin_name, email=admin_email, phone=admin_phone)
    result = administrator.addNewLocation(car_rental_system, location=location2)
    print(result)

    # Create a customer
    customer_license = DriverLicense(licenceNumber="123456", stateWhichIssuedLicense="State1", driverName="John Doe", dateIssued="2022-01-01", validTill="2023-01-01")
    customer = Customer(driverLicense=customer_license, name="John Doe", email="john@example.com", phone="123-456-7890")

    # Create a vehicle
    vehicle0 = EconomyCar(licensePlateNumber="ABC123", vin="123456789", passengerCapacity=4, model="ModelX", make="Tesla", color="Black", manufacturingYear=2022)
    vehicle1 = EconomyCar(licensePlateNumber="ABC125", vin="123456780", passengerCapacity=4, model="ModelX", make="Tesla", color="White", manufacturingYear=2022)
    vehicle2 = EconomyCar(licensePlateNumber="XYZ456", vin="987654321", passengerCapacity=5, model="Civic", make="Honda", color="Red", manufacturingYear=2022)
    vehicle3 = EconomyCar(licensePlateNumber="123XYZ", vin="456789012", passengerCapacity=5, model="Camry", make="Toyota", color="Blue", manufacturingYear=2022)

    car_rental_system.addVehicle(vehicle0)
    car_rental_system.addVehicle(vehicle1)
    car_rental_system.addVehicle(vehicle2)
    car_rental_system.addVehicle(vehicle3)
    # Customer searches for available vehicles
    available_vehicles = car_rental_system.getAvailableVehicles()
    search_results = customer.searchVehicle(available_vehicles, query="Tesla", vehiclePickupDateTime="2022-01-10", vehicleDropOffDateTime="2022-01-15")

    print("Matching Vehicles:")
    for i, result in enumerate(search_results, start=1):
        print(f"{i}. Model: {result.getModel()}, Make: {result.getMake()}, Color: {result.getColor()}")
    
    if search_results:
        # Customer selects a vehicle to reserve
        selected_vehicle_index = int(input("Enter the serial of vehicle you want to reserve: "))
        selected_vehicle = search_results[selected_vehicle_index - 1]

    # Create a reservation
    reservation = Reservation(reservationNumber="R123", returnDate="2022-02-01", primaryDriver=customer, pickupLocation=location1, dropOffLocation=location2, vehicle=selected_vehicle)

    # Complete the reservation
    customer.completeReservation(reservation)

    # Make a payment
    payment = Payment(transactionId="P456")
    payment.setPaymentStatus(PaymentStatus.COMPLETED)

    # Update the reservation with payment information
    reservation.changeInsurance(RentalInsurance(insuranceId="I789", issuingInsuranceCompany="InsuranceCo", startDate="2022-01-01", endDate="2022-02-01", coverageType=InsuranceCoverageType.REGULAR, ratePerDay=20))
    reservation.getInsurance().setEndDate("2022-02-01")
    reservation.getInsurance().setRatePerDay(25)
    reservation.getInsurance().setCoverageType(InsuranceCoverageType.ADVANCED)

    # Print reservation details
    print(f"Reservation Details: {reservation.getReservationNumber()}")
    print(f"Pickup Location: {reservation.getPickupLocation().getLocationName()}")
    print(f"Drop-off Location: {reservation.getDropOffLocation().getLocationName()}")
    print(f"Primary Driver: {reservation.getPrimaryDriver().getName()}")
    print(f"Vehicle: {reservation.getVehicle().getModel()} {reservation.getVehicle().getMake()}")

    # Insurance details
    insurance_details = reservation.getInsurance()
    print(f"\nInsurance Details:")
    print(f"Insurance ID: {insurance_details.getInsuranceId()}")
    print(f"Issuing Insurance Company: {insurance_details.getIssuingInsuranceCompany()}")
    print(f"Start Date: {insurance_details.getStartDate()}, End Date: {insurance_details.getEndDate()}")
    print(f"Coverage Type: {insurance_details.getCoverageType().name}")
    print(f"Rate Per Day: {insurance_details.getRatePerDay()}")

    # Vehicle details
    vehicle_details = reservation.getVehicle()
    print(f"\nVehicle Details:")
    print(f"Vehicle: Model {vehicle_details.getModel()}, Make {vehicle_details.getMake()}, Color {vehicle_details.getColor()}")
    print(f"License Plate: {vehicle_details.getLicenseNumber()}, VIN: {vehicle_details.getVin()}")
    print(f"Passenger Capacity: {vehicle_details.getPassengerCapacity()}, Manufacturing Year: {vehicle_details.getManufacturingYear()}")

if __name__ == "__main__":
    main()