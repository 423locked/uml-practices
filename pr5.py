from abc import ABC, abstractmethod

# Абстрактная фабрика (Abstract Factory)
class AbstractProductA(ABC):
    @abstractmethod
    def functionality(self) -> str:
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def another_functionality(self) -> str:
        pass

class ConcreteProductA1(AbstractProductA):
    def functionality(self) -> str:
        return "ConcreteProductA1"

class ConcreteProductA2(AbstractProductA):
    def functionality(self) -> str:
        return "ConcreteProductA2"

class ConcreteProductB1(AbstractProductB):
    def another_functionality(self) -> str:
        return "ConcreteProductB1"

class ConcreteProductB2(AbstractProductB):
    def another_functionality(self) -> str:
        return "ConcreteProductB2"

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()

def abstract_factory_client(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(product_a.functionality())
    print(product_b.another_functionality())

print("Абстрактная фабрика:")
abstract_factory_client(ConcreteFactory1())
abstract_factory_client(ConcreteFactory2())

# Посредник (Mediator)

class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: object, event: str) -> None:
        pass

class ConcreteMediator(Mediator):
    def init(self, component1, component2):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers:")
            self._component1.do_b()

class BaseComponent:
    def init(self, mediator: Mediator = None):
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator

class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component 1 does A.")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Component 1 does B.")

class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component 2 does C.")

    def do_d(self) -> None:
        print("Component 2 does D.")
        self.mediator.notify(self, "D")

print("\nПосредник:")
c1 = Component1()
c2 = Component2()
mediator = ConcreteMediator(c1, c2)

c1.do_a()
c2.do_d()

# Строитель (Builder)

class Product:
    def init(self):
        self.parts = []

    def add(self, part: str) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}")

class Builder(ABC):
    @abstractmethod
    def produce_part_a(self) -> None: pass

    @abstractmethod
    def produce_part_b(self) -> None: pass

    @abstractmethod
    def produce_part_c(self) -> None: pass

class ConcreteBuilder1(Builder):
    def init(self):
        self.reset()

    def reset(self):
        self._product = Product()

    @property
    def product(self) -> Product:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")

class Director:
    def init(self):
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

print("\nСтроитель:")
director = Director()
builder = ConcreteBuilder1()
director.builder = builder

director.build_minimal_viable_product()
builder.product.list_parts()

director.build_full_featured_product()
builder.product.list_parts()

# Адаптер (Adapter)

class Target:
    def request(self) -> str:
        return "Target: The default target's behavior."

class Adaptee:
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"

class Adapter(Target):
    def init(self, adaptee: Adaptee):
        self._adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self._adaptee.specific_request()[::-1]}"

print("\nАдаптер:")
def adapter_client_code(target: Target) -> None:
    print(target.request())

print("Client: I can work just fine with the Target objects:")
target = Target()
adapter_client_code(target)

adaptee = Adaptee()
print("Client: The Adaptee class has a weird interface. See, I don't understand it:")
print(f"Adaptee: {adaptee.specific_request()}")

print("Client: But I can work with it via the Adapter:")
adapter = Adapter(adaptee)
adapter_client_code(adapter)
