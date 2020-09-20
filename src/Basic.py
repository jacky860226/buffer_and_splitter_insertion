
import default_cell_library


class Wire:
    def __init__(self):
        self.input_port = None
        self.output_port_set = set()
        self.output_delay = dict()


class Node:
    def __init__(self, _type):
        self.type = _type
        if _type is not None:
            self.input_port_name = set(_type.input_labels)
            self.output_port_name = set(_type.output_labels)
        else:
            self.input_port_name = set()
            self.output_port_name = set()
        self.input_wire = dict()
        self.output_wire = dict()

    def add_input_wire(self, port_name, wire):
        assert(port_name in self.input_port_name)
        self.input_wire[port_name] = wire

    def add_output_wire(self, port_name, wire):
        assert(port_name in self.output_port_name)
        self.output_wire[port_name] = wire

    def get_inputs(self):
        return self.input_wire.items()

    def get_outputs(self):
        return self.output_wire.items()


class Input(Node):
    def __init__(self, input_wire):
        super().__init__(None)
        self.output_port_name = input_wire


class Output(Node):
    def __init__(self, output_wire):
        super().__init__(None)
        self.input_port_name = output_wire


class Module:
    def __init__(self, raw_module):
        self.special_constant = ["1'b0", "1'b1"]
        for b in self.special_constant:
            raw_module.input.add(b)
        self.library = default_cell_library.Library()
        self.name = raw_module.name
        self.input = Input(raw_module.input)
        self.output = Output(raw_module.output)

        self._create_cell_dict(raw_module)
        wire_dict = self._create_wire_dict(raw_module)

        for b in self.special_constant:
            if len(wire_dict[b].output_port_set) == 0:
                del wire_dict[b]
                self.input.output_port_name.remove(b)
                del self.input.output_wire[b]

        self.wires = set()
        for wire in wire_dict.values():
            self.wires.add(wire)

    def add_wire_to_cell_input(self, wire, port_name, cell, delay=0):
        wire_output = (cell, port_name)
        wire.output_port_set.add(wire_output)
        wire.output_delay[wire_output] = delay
        cell.add_input_wire(port_name, wire)

    def add_wire_to_cell_output(self, wire, port_name, cell):
        wire_input = (cell, port_name)
        assert(wire.input_port is None)
        wire.input_port = wire_input
        cell.add_output_wire(port_name, wire)

    def _create_cell_dict(self, raw_module):
        self.cell_dict = dict()
        for sm in raw_module.subModuleList:
            cellTy = self.library[sm.masterName]
            self.cell_dict[sm.name] = Node(cellTy)

    def _create_wire_dict(self, raw_module):
        wire_dict = dict()
        for w in self.input.output_port_name:
            wire_dict[w] = Wire()
        for w in self.output.input_port_name:
            wire_dict[w] = Wire()
        for w in raw_module.wire:
            wire_dict[w] = Wire()
        for (L, R) in raw_module.assign:
            wire_dict[L] = wire_dict[R]
        for sm in raw_module.subModuleList:
            cur_cell = self.cell_dict[sm.name]
            for port_name in cur_cell.input_port_name:
                wire_name = sm.ioDict[port_name]
                cur_wire = wire_dict[wire_name]
                self.add_wire_to_cell_input(cur_wire, port_name, cur_cell)
            for port_name in cur_cell.output_port_name:
                wire_name = sm.ioDict[port_name]
                cur_wire = wire_dict[wire_name]
                self.add_wire_to_cell_output(cur_wire, port_name, cur_cell)
        for w in self.input.output_port_name:
            cur_wire = wire_dict[w]
            self.add_wire_to_cell_output(cur_wire, w, self.input)
        for w in self.output.input_port_name:
            cur_wire = wire_dict[w]
            self.add_wire_to_cell_input(cur_wire, w, self.output)
        return wire_dict

    def verilog_output(self, fout):
        input_wires = set()
        output_wires = set()
        wire_cnt = 0
        wire_name_table = dict()
        for wire_name, wire in self.input.output_wire.items():
            wire_name_table[wire] = wire_name
            input_wires.add(wire)
        for wire_name, wire in self.output.input_wire.items():
            wire_name_table[wire] = wire_name
            output_wires.add(wire)
        fout.write("module %s(" % (self.name))
        first = False
        for w in input_wires:
            if first:
                fout.write(',')
            first = True
            fout.write(wire_name_table[w])
        for w in output_wires:
            if first:
                fout.write(',')
            first = True
            fout.write(wire_name_table[w])
        fout.write(");\n")
        for w in self.wires:
            if w in input_wires or w in output_wires:
                continue
            wire_name_table[w] = "jinkela_wire_"+str(wire_cnt)
            wire_cnt += 1
            fout.write("    wire %s;\n" % (wire_name_table[w]))
        for w in input_wires:
            fout.write("    input %s;\n" % (wire_name_table[w]))
        for w in output_wires:
            fout.write("    output %s;\n" % (wire_name_table[w]))
        fout.write("\n")

        for old_name, node in self.cell_dict.items():
            fout.write("    %s %s (\n" % (node.type.name, old_name))
            outNum = len(node.input_port_name) + len(node.output_port_name)
            for port_name, wire in node.get_inputs():
                outNum -= 1
                fout.write("        .%s(%s)" %
                           (port_name, wire_name_table[wire]))
                if outNum == 0:
                    fout.write("\n")
                else:
                    fout.write(",\n")
            for port_name, wire in node.get_outputs():
                outNum -= 1
                fout.write("        .%s(%s)" %
                           (port_name, wire_name_table[wire]))
                if outNum == 0:
                    fout.write("\n")
                else:
                    fout.write(",\n")
            fout.write("    );\n\n")
        fout.write("endmodule\n")
