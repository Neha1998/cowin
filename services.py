"""
COWIN

- user registration(phone)
- otpservice
- slotbooking(location, age-group)
	LIST (all centers)
	GET (specific center details)
	POST (customer_details= {} , ) Book the slot
	DELETE
	GET_BOOKED_SLOTS (list of all the slots booked) { secret code }
- VACCINE_STATUS
	GET - user's vaccine_ids (0, 1, 2)
	POST - update user's status ("one dosed", "double dosed")

- VACCINE (Covaxin, Covishield)

"""

class UserService():

    def get(self):
        OTPservice()
        pass

    def post(self):
        User.save()

    def delete(self):
        pass

    def update(self):
        pass

class OTPservice():
    def generate(self):
        otp = ""
        return otp
    def validation(self):
        pass

class SlotBooking(object):

    def list(self, location="122001", age-group=18, vaccine="covishield"):
        return Center.filter(location, age-group, vaccine)

    def get(self, center_id):
        return Center.objects(id=center_id)

    def post(self, center_id, customer_details):
        """
        check for the center's occupancy
        update occupnacy

        :param self:
        :param center_id:
        :param customer_details:
        :return:
        """
        pass


