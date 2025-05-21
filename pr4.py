class ConcreteCollection:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def __iter__(self):
        return ConcreteIterator(self._items)


class ConcreteIterator:
    def __init__(self, items):
        self._items = items
        self._index = 0

    def __next__(self):
        if self._index < len(self._items):
            result = self._items[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __iter__(self):
        return self

from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element):
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element):
        pass

class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


class ConcreteElementA(Element):
    def accept(self, visitor: Visitor):
        visitor.visit_concrete_element_a(self)

    def operation_a(self):
        return "Element A"


class ConcreteElementB(Element):
    def accept(self, visitor: Visitor):
        visitor.visit_concrete_element_b(self)

    def operation_b(self):
        return "Element B"


class ConcreteVisitor(Visitor):
    def visit_concrete_element_a(self, element: ConcreteElementA):
        print(f"Visiting {element.operation_a()}")

    def visit_concrete_element_b(self, element: ConcreteElementB):
        print(f"Visiting {element.operation_b()}")


elements = [ConcreteElementA(), ConcreteElementB()]
visitor = ConcreteVisitor()

for element in elements:
    element.accept(visitor)

collection = ConcreteCollection()
collection.add_item("Item 1")
collection.add_item("Item 2")
collection.add_item("Item 3")

for item in collection:
    print(item)