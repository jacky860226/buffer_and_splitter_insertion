from abc import ABC, abstractmethod


class BooleanTerm(ABC):
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if not isinstance(other, BooleanTerm):
            return False
        return self.name == other.name

    @abstractmethod
    def evaluate(self):
        pass

    @property
    @abstractmethod
    def truth_value(self):
        pass


class BooleanVariable(BooleanTerm):
    def __init__(self, name: str):
        super().__init__(name)
        self.value = None

    def assign(self, value: bool):
        self.value = value

    def evaluate(self):
        return self.value

    @property
    def truth_value(self):
        if self.value is None:
            return 0
        if self.value:
            return 2
        return 1


class BooleanNode(BooleanTerm):
    def __init__(self, name: str):
        super().__init__(name)
        self.inputs = list()
        self.truth_table = set()

    def assign(self, inputs: list, truth: int):
        self.inputs = list(inputs)
        table = format(truth, '0{}b'.format(2**len(inputs)))
        for i in range(len(table)):
            if int(table[len(table) - 1 - i]) == 1:
                comb = format(i, '0{}b'.format(len(inputs)))
                pattern = tuple([x == '1' for x in list(comb)][::-1])
                self.truth_table.add(pattern)

    def negate(self, inputs: str):
        froms = [x.name for x in self.inputs]
        if inputs not in froms:
            return
        ind = froms.index(inputs)
        new_table = set()
        for t in self.truth_table:
            new_table.add(tuple([not t[x] if x == ind else t[x] for x in range(len(t))]))
        self.truth_table = new_table

    def reorder(self, new_order: list):
        if set.intersection(set(x.name for x in self.inputs), set(new_order)) == set(x.name for x in self.inputs):
            order_table = [[x.name for x in self.inputs].index(x) for x in new_order if x in {x.name for x in self.inputs}]
            new_table = set()
            for t in self.truth_table:
                new_table.add(tuple([t[x] for x in order_table]))
            self.truth_table = new_table
            self.inputs = [self.inputs[x] for x in order_table]

    def evaluate(self):
        pattern = tuple([p.evaluate() for p in self.inputs])
        return pattern in self.truth_table

    @property
    def truth_value(self):
        def btod(digits):
            value = 0
            for i in digits[::-1]:
                value = (value << 1) | int(i)
            return value
        return sum([2 ** btod(x) for x in self.truth_table])













