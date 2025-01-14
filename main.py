import asyncio
from hotel_management.reservations import Reservation, ReservationSystem
from hotel_management.customers import Customer, CustomerManagement
from hotel_management.rooms import Room, RoomManagement
from hotel_management.payments import process_payment
from datetime import datetime

async def main():
    # Inicializar sistemas
    reservation_system = ReservationSystem()
    customer_mgmt = CustomerManagement()
    room_mgmt = RoomManagement()

    # Crear habitaciones
    room_mgmt.add_room(Room(101, "Single", 100))
    room_mgmt.add_room(Room(102, "Double", 150))
    room_mgmt.add_room(Room(103, "Doble", 180))

    # Agregar clientes
    customer1 = Customer("Alice", "alice@example.com")
    customer_mgmt.add_customer(customer1)

    customer2 = Customer("Bob", "bob@example.com")
    customer_mgmt.add_customer(customer2)

    customer3 = Customer("Angel", "angel@example.com")
    customer_mgmt.add_customer(customer3)

    customer4 = Customer("Raquel", "raquel@example.com")
    customer_mgmt.add_customer(customer4)

    # Verificar disponibilidad de habitaciones
    if room_mgmt.check_availability(101):
        reservation = Reservation(customer_mgmt.get_customer(0), 101, datetime.now(), datetime.now())
        reservation_system.add_reservation(reservation)
        room_mgmt.update_availability(101)
        # Procesar pago asincrónicamente
        await process_payment(reservation.guest.name, room_mgmt.get_room(101).price)

    # Verificar disponibilidad de habitaciones
    if room_mgmt.check_availability(102):
        reservation = Reservation(customer_mgmt.get_customer(1), 102, datetime.now(), datetime.now())
        reservation_system.add_reservation(reservation)
        room_mgmt.update_availability(102)
        # Procesar pago asincrónicamente
        await process_payment(reservation.guest.name, room_mgmt.get_room(102).price)

    # Verificar disponibilidad de habitaciones
    if room_mgmt.check_availability(102):
        reservation = Reservation(customer_mgmt.get_customer(2), 102, datetime.now(), datetime.now())
        reservation_system.add_reservation(reservation)
        room_mgmt.update_availability(102)
        # Procesar pago asincrónicamente
        await process_payment(reservation.guest.name, room_mgmt.get_room(102).price)
    
    # Verificar disponibilidad de habitaciones
    if room_mgmt.check_availability(103):
        reservation = Reservation(customer_mgmt.get_customer(3), 103, datetime.now(), datetime.now())
        reservation_system.add_reservation(reservation)
        room_mgmt.update_availability(103)
        # Procesar pago asincrónicamente
        await process_payment(reservation.guest.name, room_mgmt.get_room(103).price)

if __name__ == "__main__":
    asyncio.run(main())

