class User(object):
    id:
    phone:
    slots = []

class UserSlot(object):
    id:
    time:
    center:
    user:
    status: ("booked", "done", "cancelled")

class Vaccine(object):
    name:
    constraint_time:

    def price(self):
        return 100

class Covishield(Vaccine):
    name = ""
    constraint_time = 100

class Cowaxin(Vaccine):
    name = ""
    constraint_time = 28

class Center(object):
    id = ""
    location = "122001"
    available_slot_ids = [availale_slot_ids]

class AvailableSlot():
    time: 301938091803
    end_time: 23332731709
    occupied:
    capacity:
    center_id:
    active:
    vaccines = [Vaccine(freepriceCalculationStrategy)]
    age_group = ""
    booked_slots = [userslot_ids]

class priceCalculationStrategy(object):
    def price(self):
        return self.price

class freepriceCalculationStrategy(priceCalculationStrategy):

    def price(self):
        return 0


class CenterVaccine(Vaccine):
    dose = 1

    def __init__(self, pricecalcstr=priceCalculationStrategy):
        self.pricecalcstr = pricecalcstr

    def price(self):
        self.pricecalcstr.price()
