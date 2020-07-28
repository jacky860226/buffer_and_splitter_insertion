from abc import ABC, abstractmethod


class Net(ABC):
    @abstractmethod
    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent
        self._source = None
        self.post = set()

    def __hash__(self):
        return hash(id(self))

    def __eq__(self, other):
        return id(self) == id(other)

    @property
    def source(self):
        return self._source

    @property
    def source_instance(self):
        if self._source is not None:
            return self._source.parent
        return

    @property
    def fullname(self):
        return "{}.{}".format(self.parent.name, self.name)

    @abstractmethod
    def connect_from(self, other):
        pass

    @abstractmethod
    def disconnect_from(self):
        pass

    @abstractmethod
    def connect_to(self, other):
        pass

    @abstractmethod
    def disconnect_to(self, other):
        pass

    @abstractmethod
    def to_verilog(self):
        pass


class Pin(ABC):
    @abstractmethod
    def __init__(self, name: str, parent, con: Net = None):
        self.name = name
        self.parent = parent
        self._alias = None
        if con is not None:
            self.bind(con)

    def __hash__(self):
        return hash(id(self))

    def __eq__(self, other):
        return id(self) == id(other)

    @property
    def fullname(self):
        return "{}.{}".format(self.parent.name, self.name)

    @property
    @abstractmethod
    def connection(self):
        pass

    @abstractmethod
    def bind(self, other):
        pass

    @abstractmethod
    def unbind(self):
        pass


class Device(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_delay(self, other):
        pass

    @property
    @abstractmethod
    def delay(self):
        pass

    @property
    @abstractmethod
    def interface(self):
        pass

    @property
    @abstractmethod
    def input_labels(self) -> list:
        pass

    @property
    @abstractmethod
    def output_labels(self) -> list:
        pass

    @property
    @abstractmethod
    def gate_count(self):
        pass

    @abstractmethod
    def instantiate(self, name: str, parent, mapping):
        pass


class CellDevice(Device):
    @abstractmethod
    def __init__(self, name):
        super().__init__(name)
        self._truth_values = dict()

    @abstractmethod
    def truth_value(self):
        pass


class Block(ABC):
    @abstractmethod
    def __init__(self, name, parent):
        self.parent = parent
        self.name = name

    def __hash__(self):
        return hash(id(self))

    def __eq__(self, other):
        return id(self) == id(other)

    @property
    @abstractmethod
    def input_pins(self) -> list:
        pass

    @property
    @abstractmethod
    def output_pins(self) -> list:
        pass

    @abstractmethod
    def get_delay(self, other: str):
        pass

    @property
    @abstractmethod
    def gate_count(self):
        pass

    @abstractmethod
    def to_verilog(self):
        pass


class UnitBlock(Block):
    @abstractmethod
    def truth_value(self, other):
        pass


class LogicBlock(Block):
    @abstractmethod
    def cell_mapping(self, library):
        pass







