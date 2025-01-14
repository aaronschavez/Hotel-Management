class Room:
    def __init__(self, room_number: int, room_type: str, price: float):
        self.room_number: int = room_number
        self.room_type: str = room_type
        self.price: float = price
        self.available: bool = True
    
    def __str__(self) -> str:
        return f"Room(room_number = {self.room_number}, room_type = {self.room_type}, price = {self.price}, available = {self.available})"

class RoomManagement:
    def __init__(self):
        self.rooms : dict[int, Room] = {}

    def add_room(self, room: Room) -> None:
        """Agrega una nueva habitación al sistema."""
        self.rooms[room.room_number] = room
        print(f"Habitación {room.room_number} agregada")
    
    def get_room(self, room_number: int) -> Room:
       """Obtiene la información de un cliente por ID."""
       return self.rooms.get(room_number, "Clinete no encontrado")
    
    def update_availability(self, room_number: int) -> None:
        """Actualiza la disponibilidad de una habitación."""
        room = self.rooms.get(room_number)
        if room:
            room.available = False
        else:
            print(f"Habitación {room_number} no encontrada")

    def check_availability(self, room_number: int) -> bool:
        """Verifica si una habitación está disponible."""
        room = self.rooms.get(room_number)
        if room and room.available:
            print(f"Habitación {room_number} está disponible.")
            return True
        print(f"Habitación {room_number} no está disponible.")
        return False