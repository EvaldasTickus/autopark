from datetime import datetime, timedelta
import math

fuel_price = 1.5

class Vehicle:
    def __init__(self, number, fuel_type, costs, km_year, fuel_100km, mot, insurance, driver_license):
        self.number = number
        self.fuel_type = fuel_type
        self.costs = costs
        self.km_year = km_year
        self.fuel_100km = fuel_100km
        self.mot = datetime.strptime(mot, "%Y-%m-%d")
        self.insurance = datetime.strptime(insurance, "%Y-%m-%d")
        self.driver_license = driver_license

    def if_need_mot_insurance(self):
        today_date = datetime.today()
        next_month = today_date + timedelta(days=30)

        need_insurance = self.insurance <= next_month
        need_mot = self.mot <= next_month

        if need_mot and need_insurance:
            return "Need MOT and insurance"
        elif need_mot:
            return "Need MOT"
        elif need_insurance:
            return "Need insurance"
        return "Neither one is needed"

    def count_costs(self, km):
        regular_costs = (self.fuel_100km / 100) * fuel_price * km
        other_costs = (self.costs / self.km_year) * km
        total = regular_costs + other_costs
        return round(total)

class Auto(Vehicle):
    def __init__(self, km_year, number, fuel_type, costs, mot, driver_license, fuel_100km, insurance,):
        super().__init__(number, fuel_type, costs, km_year, fuel_100km, mot, insurance, driver_license)

class Truck(Vehicle):
    def __init__(self, km_year, max_weight, trailer, trailer_weight, number, fuel_type, costs, mot, driver_license, fuel_100km, insurance):
        super().__init__(number, fuel_type, costs, km_year, fuel_100km, mot, insurance, driver_license)
        self.max_weight = max_weight
        self.trailer = trailer
        self.trailer_weight = trailer_weight

    def calculate_trips(self, weight):
        truck_capacity = self.max_weight
        trailer_capacity = self.trailer_weight
        full_capacity = truck_capacity + trailer_capacity


        if weight <= truck_capacity:
            return math.ceil(weight / truck_capacity), 0


        full_trips = weight // full_capacity
        remaining_load = weight % full_capacity

        truck_only_trips = 0
        if remaining_load > 0:
            if remaining_load <= truck_capacity:
                truck_only_trips = 1
            else:
                full_trips += 1

        truck_only_trips_with_no_trailer = math.ceil(weight / truck_capacity)

        if truck_only_trips_with_no_trailer <= (full_trips + truck_only_trips):
            return truck_only_trips_with_no_trailer, 0

        return truck_only_trips, full_trips

    def if_can_use_trailer(self):
        if self.driver_license == "E":
            return "Can use trailer"
        return "Cant use trailer"


class Bus(Vehicle):
    def __init__(self, number, fuel_type, passenger_seats, costs, fuel_100km, driver_license, mot, insurance, km_year):
        super().__init__(number, fuel_type, costs, km_year, fuel_100km, mot, insurance, driver_license)
        self.passenger_seats = passenger_seats

    def how_many_busses(self, passengers):
        return math.ceil(passengers / self.passenger_seats)

    def averages(self, passengers, km):
        bus_count = self.how_many_busses(passengers)
        total_price = bus_count * self.count_costs(km)
        return total_price


class Driver:
    def __init__(self, holiday_start, holiday_end, license_category, payment_per_km):
        self.holiday_start = datetime.strptime(holiday_start, "%Y-%m-%d")
        self.holiday_end = datetime.strptime(holiday_end, "%Y-%m-%d")
        self.license_category = license_category
        self.payment_per_km = payment_per_km

    def is_on_holiday(self, check_this_date):
        check_this_date = datetime.strptime(check_this_date, "%Y-%m-%d")
        if  self.holiday_start <= check_this_date <= self.holiday_end:
            return "On Holiday"
        return "Not on Holiday"

car = Auto(
    number="EVA777",
    fuel_type="Petrol",
    km_year=10000,
    costs=300,
    driver_license="B",
    fuel_100km=10,
    insurance="2026-02-20",
    mot="2025-02-20",
)

bus = Bus(
    number="EDG858",
    fuel_type="Diesel",
    passenger_seats=50,
    costs=1000,
    fuel_100km=15,
    driver_license="C",
    mot="2025-08-15",
    insurance="2025-08-20",
    km_year=50000
)

truck = Truck(
    km_year=50000,
    max_weight=12,
    trailer=True,
    trailer_weight=5,
    number="ADE123",
    fuel_type="diesel",
    costs=3000,
    mot="2025-02-15",
    driver_license="E",
    fuel_100km=20,
    insurance="2025-02-20"
)

driver = Driver(
    holiday_start="2025-07-01",
    holiday_end="2025-07-15",
    license_category="E",
    payment_per_km=0.5
)

print(car.if_need_mot_insurance())
print(f"Costs for 200km: {car.count_costs(200)} EUR")
print("-----------------------------------------------------------------------------")
print(bus.if_need_mot_insurance())
print(f"Costs for 200 km: {bus.count_costs(200)} EUR")
print(f"Total bus count: {bus.how_many_busses(50)}")
print(f"Total costs will be: {bus.averages(120, 200)} EUR")
print("-----------------------------------------------------------------------------")
print(truck.if_need_mot_insurance())
print(f"Costs for the 500 km: {truck.count_costs(500)}")
print(truck.calculate_trips(25))
print(truck.if_can_use_trailer())
print("-----------------------------------------------------------------------------")
check_this_date = "2025-07-10"
print(driver.is_on_holiday(check_this_date))