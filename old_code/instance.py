from abstract_net_model import Block, UnitBlock, CellDevice,Device, Net
from pins import PinIn, PinOut
from typing import Dict


class Instance(Block):
    def __init__(self, name: str, parent: Device, model: Device, mapping: Dict[str, Net]):
        super().__init__(name, parent)
        self._model = model
        self._pins = dict()
        self._inputs = list()
        self._outputs = list()
        for x in model.input_labels:
            pin = PinIn(x, self, mapping.get(x))
            self._pins[x] = pin
            self._inputs.append(pin)
        for x in model.output_labels:
            pin = PinOut(x, self, mapping.get(x))
            self._pins[x] = pin
            self._outputs.append(pin)

    @property
    def model(self):
        return self._model.name

    @property
    def input_pins(self):
        return self._inputs

    @property
    def output_pins(self):
        return self._outputs

    @property
    def gate_count(self):
        return self._model.gate_count

    def get_delay(self, other: str):
        return self._model.get_delay(other)

    def to_verilog(self):
        verilog = "\t{} {} (".format(self._model.name, self.name)
        verilog = verilog + ','.join(["\n\t\t.{}({})".format(x, self._pins.get(x).connection.name)
                                      for x in self._model.interface])
        verilog = verilog + "\n\t);"
        return verilog


class DirectInstance(UnitBlock):
    def __init__(self, name: str, parent: Device, model: CellDevice, mapping: Dict[str, Net]):
        super().__init__(name, parent)
        self._model = model
        self._pins = dict()
        self._inputs = list()
        self._outputs = list()
        for x in model.input_labels:
            pin = PinIn(x, self, mapping.get(x))
            self._pins[x] = pin
            self._inputs.append(pin)
        for x in model.output_labels:
            pin = PinOut(x, self, mapping.get(x))
            self._pins[x] = pin
            self._outputs.append(pin)

    @property
    def model(self):
        return self._model

    @property
    def input_pins(self):
        return self._inputs

    @property
    def output_pins(self):
        return self._outputs

    @property
    def pins(self):
        return self._pins

    @property
    def gate_count(self):
        return self._model.gate_count

    def get_delay(self, other: str):
        return self._model.get_delay(other)

    def to_verilog(self):
        verilog = "\t{} {} (".format(self._model.name, self.name)
        verilog = verilog + ','.join(["\n\t\t.{}({})".format(x, self._pins.get(x).connection.name)
                                      for x in self.model.interface])
        verilog = verilog + "\n\t);"
        return verilog

    def truth_value(self, other=None):
        return self._model.truth_value()

    def to_aqfp_verilog(self, connections):
        assert len(connections) == 4, "missing clock connections"
        verilog = "\t{} {} (".format(self._model.name, self.name)
        verilog = verilog + ','.join(["\n\t\t.{}({})".format(x, self._pins.get(x).connection.name)
                                      for x in self._model.interface])
        verilog += ",\n\t\t.dcin({}),\n\t\t.dcout({}),\n\t\t.xin({}),\n\t\t.xout({})".format(*connections)
        verilog = verilog + "\n\t);"
        return verilog
