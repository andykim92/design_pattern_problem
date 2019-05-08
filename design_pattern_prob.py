## What is wrong with the following code?
## How can this be fixed?

import ConsertReservation
import MuseumReservation
import ThemeParkReservation

import Event
import Customor

class Reservations():

    def __init__(self, event_id, event_start_time, event_end_time, event_seats, customer_id, customer_payment_method, ):
        self.event = Event(event_id, event_start_time, event_end_time, event_seats)
        self.customer = Customer(customer_id, customer_payment_method)

    def reserve_concert(self, ):
        consert_reservation = ConsertReservation()
        return consert_reservation.reserve_concert(self.event, self.customer)

    def reserve_museum(self, ):
        museum_reservation = MuseumReservation()
        return museum_reservation.reserve_museum(self.event, self.customer)

    def reserve_theme_park(self, ):
        theme_park_reservation = ThemeParkReservation()
        return theme_park_reservation.reserve_theme_park(self.event, self.customer)
