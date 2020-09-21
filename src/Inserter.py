import BufferAndSplitterInsertionSolver as BSI
import Basic


class Buffer_splitter_inserter:
    def __init__(self, module):
        self.module = module
        self.buffer_cnt = 0
        self.splitter_cnt = 0
        self.old_wires = module.wires.copy()
        for wire in self.old_wires:
            self._process_wire(wire)
            module.wires.remove(wire)

    def _process_wire(self, wire):
        node_port_list = list()
        S = list()
        for key, value in wire.output_delay.items():
            node_port_list.append(key)
            S.append(value)
        solver = BSI.DP_Solver()
        res = solver.solve(S.copy(), self.module.library.max_fan_out)
        for i in range(len(node_port_list)):
            assert(res[0][1][i] == wire.output_delay[node_port_list[i]])
        self._build(wire.input_port, res[1], node_port_list)

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
