from abstract_net_model import Block, Net, Pin


class PinIn(Pin):
    def __init__(self, name: str, parent: Block, con: Net = None):
        Pin.__init__(self, name, parent, con)

    @property
    def connection(self):
        return self._alias

    def bind(self, other: Net):
        self._alias = other
        other.connect_to(self)

    def unbind(self):
        if self._alias is None:
            return
        self._alias.disconnect_to(self)
        self._alias = None


class PinOut(Pin):
    def __init__(self, name: str, parent: Block, con: Net = None):
        Pin.__init__(self, name, parent, con)

    @property
    def connection(self):
        return self._alias

    def bind(self, other: Net):
        self._alias = other
        other.connect_from(self)

    def unbind(self):
        if self._alias is None:
            return
        self._alias.disconnect_from()
        self._alias = None

    @property
    def delay(self):
        return self.parent.get_delay(self.name)
