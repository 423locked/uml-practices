from abc import ABC, abstractmethod

# Заместитель (Proxy)

class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass

class RealSubject(Subject):
    def request(self) -> None:
        print("RealSubject: Handling request.")

class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.")

print("Заместитель:")
real_subject = RealSubject()
proxy = Proxy(real_subject)
proxy.request()

# Компоновщик (Composite)

class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class Leaf(Component):
    def operation(self) -> str:
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component: Component) -> None:
        self._children.append(component)

    def remove(self, component: Component) -> None:
        self._children.remove(component)

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Composite({'+'.join(results)})"

print("\nКомпоновщик:")
leaf = Leaf()
tree = Composite()
branch1 = Composite()
branch1.add(Leaf())
branch1.add(Leaf())
tree.add(branch1)
tree.add(Leaf())
print(f"Result: {tree.operation()}")

# Инверсия управления (Inversion of Control, IoC)

class Service(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteServiceA(Service):
    def operation(self) -> str:
        return "ConcreteServiceA operation"

class ConcreteServiceB(Service):
    def operation(self) -> str:
        return "ConcreteServiceB operation"

class Client:
    def __init__(self, service: Service):
        self._service = service

    def perform_operation(self):
        print(f"Client: {self._service.operation()}")

print("\nИнверсия управления:")
service_a = ConcreteServiceA()
client_a = Client(service_a)
client_a.perform_operation()

service_b = ConcreteServiceB()
client_b = Client(service_b)
client_b.perform_operation()