from abc import ABC, abstractmethod


# Определение интерфейса стратегии
class Strategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass


# Конкретные стратегии
class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return f"Strategy A: Processed {data}"


class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return f"Strategy B: Processed {data}"


# Контекст, использующий стратегию
class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute(self, data):
        result = self._strategy.execute(data)
        print(result)

from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self):
        self.base_operation()
        self.required_operations()
        self.hook()

    def base_operation(self):
        print("Base operation: выполняется в базовом классе")

    @abstractmethod
    def required_operations(self):
        pass

    def hook(self):
        pass


class ConcreteClassA(AbstractClass):
    def required_operations(self):
        print("ConcreteClassA: специфическая операция")

    def hook(self):
        print("ConcreteClassA: дополнительный хуковый метод")


class ConcreteClassB(AbstractClass):
    def required_operations(self):
        print("ConcreteClassB: другая специфическая операция")

def client_code(abstract_class: AbstractClass):
    abstract_class.template_method()



context = Context(ConcreteStrategyA())
context.execute("data1")  # Использует стратегию A

context.set_strategy(ConcreteStrategyB())
context.execute("data2")  # Использует стратегию B

client_code(ConcreteClassA())
print("\n")
client_code(ConcreteClassB())