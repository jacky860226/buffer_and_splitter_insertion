import Wire_delay_adder
import Basic
from data_leveler import Down_delay_initialer


class Buffer_splitter_inserter:
    def __init__(self, module):
        self.module = module
        self.wire_delay_adder = Wire_delay_adder.DynamicProgramming(module)
        self.buffer_cnt = 0
        self.splitter_cnt = 0

    def insert_buffer_and_splitter(self):
        self.old_wires = self.module.wires.copy()
        for wire in self.old_wires:
            self._process_wire(wire)
            self.module.wires.remove(wire)

    def insert_splitter(self):
        self.old_wires = self.module.wires.copy()
        for wire in self.old_wires:
            self._process_wire_splitter(wire)
            self.module.wires.remove(wire)

    def buffer_decrease(self):
        delay_initialer = Down_delay_initialer(self.module)
        delay_initialer.create_raw_delay()
        dec_buffer = 0
        node_set = set(self.module.cell_dict.values())
        while len(node_set) > 0:
            node_list = list(node_set)
            node_list.sort(key=lambda x: delay_initialer[x])
            node = node_list[0]
            node_set.remove(node)
            if len(node.get_outputs()) > 1:
                continue
            dec_buffer += node.delay_push_down()
        return dec_buffer

    def _process_wire(self, wire):
        node_port_list, res = self.wire_delay_adder.get_wire_extra_delay(wire)
        for i in range(len(node_port_list)):
            assert(res[0][1][i] == wire.output_delay[node_port_list[i]])
        self._build(wire.input_port, res[1], node_port_list)

    def _process_wire_splitter(self, wire):
        node_port_list, res = self.wire_delay_adder.get_wire_extra_delay(wire)
        for i in range(len(node_port_list)):
            assert(res[0][1][i] == wire.output_delay[node_port_list[i]])
        self._build_splitter(wire.input_port, res[1], node_port_list)

    def _build(self, output_port, tree, node_port_list):
        new_wire = Basic.Wire()
        self.module.wires.add(new_wire)
        self.module.add_wire_to_cell_output(
            new_wire, output_port[1], output_port[0])
        if isinstance(tree, int):
            cell, port_name = node_port_list[tree]
            self.module.add_wire_to_cell_input(new_wire, port_name, cell)
            return
        SPO = len(tree)
        new_node = None
        if SPO == 1:
            new_node = Basic.Node(self.module.library.get_buffer())
            self.module.cell_dict["jinkela_bfr_" +
                                  str(self.buffer_cnt)] = new_node
            self.buffer_cnt += 1
        else:
            new_node = Basic.Node(self.module.library.get_splitter(SPO))
            self.module.cell_dict["jinkela_spl_" +
                                  str(self.splitter_cnt)] = new_node
            self.splitter_cnt += 1
        new_port_name = min(new_node.input_port_name)
        assert(len(new_node.input_port_name) == 1)
        self.module.add_wire_to_cell_input(
            new_wire, new_port_name, new_node)
        SPO_cnt = 0
        for new_output_port_name in new_node.output_port_name:
            self._build((new_node, new_output_port_name),
                        tree[SPO_cnt], node_port_list)
            SPO_cnt += 1

    def _build_splitter(self, output_port, tree, node_port_list):
        new_wire = Basic.Wire()
        self.module.wires.add(new_wire)
        self.module.add_wire_to_cell_output(
            new_wire, output_port[1], output_port[0])
        delay = 0
        while True:
            if isinstance(tree, int):
                cell, port_name = node_port_list[tree]
                self.module.add_wire_to_cell_input(
                    new_wire, port_name, cell, delay)
                return
            elif len(tree) > 1:
                break
            delay += 1
            tree = tree[0]
        SPO = len(tree)
        new_node = None
        assert(SPO > 1)
        new_node = Basic.Node(self.module.library.get_splitter(SPO))
        self.module.cell_dict["jinkela_spl_" +
                              str(self.splitter_cnt)] = new_node
        self.splitter_cnt += 1
        new_port_name = min(new_node.input_port_name)
        assert(len(new_node.input_port_name) == 1)
        self.module.add_wire_to_cell_input(
            new_wire, new_port_name, new_node, delay)
        SPO_cnt = 0
        for new_output_port_name in new_node.output_port_name:
            self._build_splitter((new_node, new_output_port_name),
                                 tree[SPO_cnt], node_port_list)
            SPO_cnt += 1
