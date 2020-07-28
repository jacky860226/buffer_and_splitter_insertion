from abstract_net_model import Device, CellDevice
from wires import Wire, PortIn, PortOut
from instance import DirectInstance
from typing import Dict, List


class Cell(CellDevice):
    def __init__(self, name: str, interfaces: list, inputs: list, output: str, tt: int, area, delay):
        super().__init__(name)
        self._interface = interfaces
        self._gate_count = area
        self._delay = delay
        self._inputs = [PortIn(x, self) for x in inputs]
        self._output = PortOut(output, self)
        self._truth_values = tt

    def get_delay(self, other=None):
        return self._delay

    @property
    def delay(self):
        return self._delay

    @property
    def gate_count(self):
        return self._gate_count

    @property
    def interface(self):
        return self._interface

    @property
    def input_labels(self):
        return [x.name for x in self._inputs]

    @property
    def output_labels(self):
        return [self._output.name]

    def truth_value(self):
        return self._truth_values

    def instantiate(self, name: str, parent: Device, mapping: Dict[str, Wire]):
        return DirectInstance(name, parent, self, mapping)


class Buffer(CellDevice):
    def __init__(self, name: str, interfaces: list, input: str, output: str, area, delay):
        super().__init__(name)
        self._interface = interfaces
        self._gate_count = area
        self._delay = delay
        self._input = PortIn(input, self)
        self._output = PortOut(output, self)

    def get_delay(self, other=None):
        return self._delay

    @property
    def delay(self):
        return self._delay

    @property
    def gate_count(self):
        return self._gate_count

    @property
    def interface(self):
        return self._interface

    @property
    def input_labels(self):
        return [self._input.name]

    @property
    def output_labels(self):
        return [self._output.name]

    def instantiate(self, name: str, parent: Device, mapping_buf: List[Wire]):
        mapping = {self._input.name: mapping_buf[0], self._output.name: mapping_buf[1]}
        return DirectInstance(name, parent, self, mapping)

    def truth_value(self):
        return 1


class Splitter(CellDevice):
    def __init__(self, name: str, interfaces: list, input: str, outputs: set, area, delay):
        super().__init__(name)
        self._interface = interfaces
        self._gate_count = area
        self._delay = delay
        self._input = PortIn(input, self)
        self._outputs = {x: PortOut(x, self) for x in outputs}

    def get_delay(self, other: str):
        return self._delay

    @property
    def delay(self):
        return self._delay

    @property
    def gate_count(self):
        return self._gate_count

    @property
    def interface(self):
        return self._interface

    @property
    def input_labels(self):
        return [self._input.name]

    @property
    def output_labels(self):
        return [x for x in self._outputs]

    @property
    def fan_out(self):
        return len(self._outputs)

    def instantiate(self, name: str, parent: Device, mapping_splitter: List[Wire]):
        mapping = {self._input.name: mapping_splitter.pop(0)}
        for x in self._outputs.values():
            mapping[x.name] = mapping_splitter.pop()
        return DirectInstance(name, parent, self, mapping)

    def truth_value(self):
        return 1
