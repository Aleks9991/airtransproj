from django.db import models

class Booking(models.Model):

    book_ref = models.AutoField(primary_key=True)
    book_date = models.DateField(auto_now_add=True)
    total_amount = models.FloatField(null=False)

    def __str__(self):
        return "{}".format(self.book_ref)

class Ticket(models.Model):
    ticket_no = models.AutoField(primary_key=True)
    book_ref = models.ForeignKey(Booking, on_delete=models.CASCADE)
    # passanger_id = models.CharField()
    # passanger_name = models.CharField()
    # contact_data = models.CharField()

class Airport(models.Model):
    airport_code = models.CharField(max_length=4, primary_key=True)
    airport_name = models.CharField(max_length=50)
    city = models.CharField()
    coordinates = models.CharField()
    timezone = models.CharField()

class Flight(models.Model):
    flight_id = models.PositiveIntegerField()
    arrival_airport = models.ForeignKey(Airport,
                                        related_name='arrival_airport',
                                        on_delete=models.CASCADE)
    # flight_no = models.ForeignKey()
    # scheduled_departure = models.CharField()
    # scheduled_arrival = models.CharField()
    # departure_airport = models.CharField()

    # status = models.CharField()
    # aircraft_code = models.CharField()
    # actual_departure = models.CharField()
    # actual_arrival = models.CharField()

class Ticket_flight(models.Model):
    ticket_no = models.ForeignKey(Ticket,
                                  on_delete=models.CASCADE)
    flight_id = models.ForeignKey(Flight,
                                  on_delete=models.CASCADE)
    fare_conditions = models.CharField(max_length=100)

    class Meta:
        unique_together = (("ticket_no", 'flight_if'),)
    amount = models.CharField()


#
# class Boarding_passes(Ticket_flight):
#     ticket_no = models.CharField()
#     flight_id = models.CharField()
#     boarding_no = models.CharField()
#     seat_no = models.CharField()
#
# class Aircraft(models.Model):
#     aircraft_mode = models.CharField()
#     model = models.CharField()
#     range_ = models.CharField()
#
# class Seats(models.Model):
#     aircraft_code = models.CharField()
#     seat_no = models.CharField()
#     fare_conditions = models.CharField()


