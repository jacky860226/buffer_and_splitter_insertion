import BufferAndSplitterInsertionSolver as BSI


class DynamicProgramming:
    def __init__(self, module):
        self.module = module

    def get_wire_extra_delay(self, wire):
        node_port_list = list()
        S = list()
        for key, value in wire.output_delay.items():
            node_port_list.append(key)
            S.append(value)
        solver = BSI.DP_Solver()
        res = solver.solve(S.copy(), self.module.library.max_fan_out)
        return node_port_list, res

    def wire_add_delay(self, wire):
        node_port_list, res = self.get_wire_extra_delay(wire)
        new_delay = res[0][1]
        for i in range(len(node_port_list)):
            key = node_port_list[i]
            wire.output_delay[key] = new_delay[i]
