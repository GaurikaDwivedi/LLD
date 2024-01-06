from car_rental_system.employee import Employee

class Administrator(Employee):
    def __init__(self, employeeId, name, email, phone):
        super().__init__(employeeId, name, email, phone)

    def addNewLocation(self, car_rental_system, location):
        if car_rental_system.addNewLocation(location):
            return f"Location '{location.getLocationName()}' added successfully."
        else:
            return f"Location '{location.getLocationName()}' already exists."

    def removeLocation(self, car_rental_system, location):
        if car_rental_system.removeLocation(location):
            return f"Location '{location.getLocationName()}' removed successfully."
        else:
            return f"Location '{location.getLocationName()}' not found."

    def addVehicleToFleet(self, car_rental_system, newVehicle):
        if car_rental_system.addVehicle(newVehicle):
            return f"Vehicle '{newVehicle.getModel()} {newVehicle.getMake()}' added to the fleet successfully."
        else:
            return f"Vehicle '{newVehicle.getModel()} {newVehicle.getMake()}' already exists in the fleet."

    def removeVehicle(self, car_rental_system, vehicle):
        if car_rental_system.removeVehicle(vehicle):
            return f"Vehicle '{vehicle.getModel()} {vehicle.getMake()}' removed from the fleet successfully."
        else:
            return f"Vehicle '{vehicle.getModel()} {vehicle.getMake()}' not found in the fleet."
