class Customer:
    __id_counter: int = 0

    def __init__(self, name: str, email: str):
        self.customer_id: int = Customer.__id_counter
        Customer.__id_counter += 1
        self.name: str = name
        self.email: str = email
    
    def __str__(self) -> str:
        return f"Customer(id = {self.customer_id}, name = {self.name}, email = {self.email})"

class CustomerManagement:
    def __init__(self):
        self.customers: dict[int, Customer] = {}

    def add_customer(self, customer: Customer) -> None:
        """Agrega un nuevo cliente al sistema."""
        self.customers[customer.customer_id] = customer
        print(f"Cliente id: {customer.customer_id}, Nombre: {customer.name} agregado")

    def get_customer(self, customer_id: int) -> Customer:
       """Obtiene la información de un cliente por ID."""
       return self.customers.get(customer_id, "Clinete no encontrado")

