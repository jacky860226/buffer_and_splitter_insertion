from directed_graph import Vertex
from abstract_net_model import Device, Block, Net
from pins import PinOut, PinIn
from alias import Alias


class Wire(Net, Vertex):
    def __init__(self, name: str, parent: (Block, Device)):
        Vertex.__init__(self, name)
        Net.__init__(self, name, parent)

    def connect_from(self, other: PinOut):
        if self._source is not None:
            print("Invalid connection, more than one fan-in to {}! Existing connection: {}, attempted connection: {}"
                  .format(self.fullname, self._source.fullname, other.fullname))
            return
        self._source = other

    def disconnect_from(self):
        self._source = None

    def connect_to(self, other: PinIn):
        self.post.add(other)

    def disconnect_to(self, other):
        if other in self.post:
            self.post.remove(other)
        else:
            print("attempted to remove no exist connection from pin {} to {}, while existing connections are {}."
                  .format(other.fullname, self.name, ','.join(p.fullname for p in self.post)))

    def get_parents(self):
        if self._source is None:
            return set()
        return {x.connection for x in self._source.parent.input_pins}

    def get_children(self):
        children = set()
        for child in self.post:
            children.update({x.connection for x in child.parent.output_pins})
        return children

    def to_verilog(self):
        return "\twire {};".format(self.name)


class PortIn(Wire):
    def __init__(self, name: str, parent: (Block, Device)):
        super().__init__(name, parent)
        self._source = None

    def connect_from(self, other: PinOut):
        return

    def disconnect_from(self):
        return

    def get_parents(self):
        return set()

    def to_verilog(self):
        return "\tinput {};".format(self.name)


class PortOut(Wire):
    def __init__(self, name: str, parent: (Block, Device)):
        super().__init__(name, parent)
        self.post = set()
        self._assignment = None

    def remove_pre_assignment(self):
        if self._assignment is None:
            return
        if self.alias is None:
            self.parent.remove_instance(self._assignment.name)
            self._assignment = None
            return
        source_wire = self.alias
        if source_wire.source is not None:
            self._assignment.unbind()
            source = source_wire.source
            source.unbind()
            source.bind(self)
            if len(source_wire.post) == 0:
                self.parent.remove_net(source_wire.name)
            self.parent.remove_instance(self._assignment.name)
            self._assignment = None

    def create_pre_assignment(self):
        if self._assignment is not None:
            return
        alias_wire = self.parent.create_wire()
        if self._source is not None:
            source = self._source
            source.unbind()
            source.bind(alias_wire)
        self._assignment = self.parent.add_alias(alias_wire.name, self.name)

    @property
    def pre_assignment(self):
        return self._assignment

    @property
    def alias(self):
        if self._assignment is None:
            return None
        return self._assignment.wire_in

    def connect_to(self, other: PinIn):
        if self._assignment is None:
            alias_wire = self.parent.create_wire()
            if self._source is not None:
                source = self._source
                source.unbind()
                source.bind(alias_wire)
            self._assignment = self.parent.add_alias(alias_wire.name, self.name)
        other.bind(self.alias)

    def connect_from(self, other: PinOut):
        if self._source is None:
            self._source = other
            if isinstance(other.parent, Alias):
                self._assignment = other.parent
            return
        if self.alias is None:
            self._source = other
        else:
            other.bind(self.alias)

    def disconnect_to(self, other):
        return

    def get_children(self):
        return set()

    def to_verilog(self):
        return "\toutput {};".format(self.name)


class VectorWire:
    def __init__(self, wire_type: str, name: str, width: int):
        self.wire_type = wire_type
        self.name = name
        self.width = width

    def to_verilog(self):
        return "\t{} [{}:0] {};".format(self.wire_type, self.width, self.name)


class Constant(Wire):
    def __init__(self, name: str, parent: (Block, Device)):
        super().__init__(name, parent)
        if name == "1'b0":
            self.val = False
        else:
            self.val = True

    def connect_from(self, other: PinOut):
        return

    def disconnect_from(self):
        return

    def get_parents(self):
        return set()

    def to_verilog(self):
        return ""
