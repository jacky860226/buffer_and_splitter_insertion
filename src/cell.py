class Cell():
    def __init__(self, name: str, interfaces: list, inputs: list, output: str, tt: int, area, delay):
        self.name = name
        self._interface = interfaces
        self._gate_count = area
        self._delay = delay
        self._inputs = [x for x in inputs]
        self._output = output
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


class Buffer():
    def __init__(self, name: str, interfaces: list, input: str, output: str, area, delay):
        self.name = name
        self._interface = interfaces
        self._gate_count = area
        self._delay = delay
        self._input = input
        self._output = output

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

    def truth_value(self):
        return 1


class Splitter():
    def __init__(self, name: str, interfaces: list, input: str, outputs: set, area, delay):
        self.name = name
        self._interface = interfaces
        self._gate_count = area
        self._delay = delay
        self._input = input
        self._outputs = {x for x in outputs}

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

    def truth_value(self):
        return 1
