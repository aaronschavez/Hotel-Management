from collections import defaultdict
from datetime import datetime

class Reservation:
    __id_counter: int = 0

    def __init__(self, guest: dict, room_number: int, check_in: datetime, check_out: datetime):
        self.reservation_id: int = Reservation.__id_counter
        Reservation.__id_counter += 1
        self.guest: dict = guest
        self.room_number: int = room_number
        self.check_in: datetime = check_in
        self.check_out: datetime = check_out
    
    def __str__(self) -> str:
        return f"Reservation(id = {self.reservation_id}, guest_id = {self.guest.customer_id}, guest_name = {self.guest.name}, room_number = {self.room_number}, check_in = {self.check_in}, check_out = {self.check_out})"

class ReservationSystem:
    def __init__(self):
        self.reservations = defaultdict(list)

    def add_reservation(self, reservation: Reservation) -> None:
        """Agrega una nueva reserva al sistema."""
        self.reservations[reservation.room_number].append(reservation)
        print(f"Reserva creada para cliente: {reservation.guest.name}, en la habitación {reservation.room_number}")
        

    def cancel_reservation(self, reservation_id: int) -> None:
        """Cancela una reserva existente por ID."""
        for room, reservations in self.reservations.items():
            for r in reservations:
                if r.reservation_id == reservation_id:
                    reservations.remove(r)
                    print(f"Reserva {reservation_id} cancelada")
                    return
        print("Reserva no encontrada")

