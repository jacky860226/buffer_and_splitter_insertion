from abstract_net_model import UnitBlock, Block, Device, Net
from pins import PinIn, PinOut


class Alias(UnitBlock):
    def __init__(self, name: str, parent: (Block, Device), org: Net, alias: Net):
        super().__init__(name, parent)
        self._input = PinIn("alias", self, alias)
        self._output = PinOut("org", self, org)

    def unbind(self):
        self._input.unbind()
        self._output.unbind()

    @property
    def wire_in(self):
        return self._input.connection

    @property
    def wire_out(self):
        return self._output.connection

    @property
    def input_pins(self):
        return [self._input]

    @property
    def output_pins(self):
        return [self._output]

    @property
    def gate_count(self):
        return 0

    def get_delay(self, other=None):
        return 0

    def truth_value(self, other):
        return 2

    def to_verilog(self):
        return "\tassign {} = {};".format(self._output.connection.name, self._input.connection.name)
