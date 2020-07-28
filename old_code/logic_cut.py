from karnaugh import *
from abstract_net_model import Net
from module import *


class LogicCut:
    def __init__(self, target: Net, edge: list, mod: Module):
        self.node_list = dict()
        self.inputs = list()
        for e in edge:
            bv = BooleanVariable(e.name)
            self.node_list[e.name] = bv
            self.inputs.append(bv)
        end_node = BooleanNode(target.name)
        self.target = end_node
        self.node_list[target.name] = end_node
        to_process = [target]
        while len(to_process) != 0:
            target_net = to_process.pop(0)
            target_node = self.node_list.get(target_net.name)
            if target_node is None:
                target_node = BooleanNode(target_net.name)
                self.node_list[target_net.name] = target_node
            if len(target_node.inputs) != 0:
                continue
            input_names = [x.connection.name for x in target_net.source_instance.input_pins]
            input_nodes = []
            for x in input_names:
                nd = self.node_list.get(x)
                if nd is None:
                    nd = BooleanNode(x)
                    input_nodes.append(nd)
                    self.node_list[x] = nd
                    to_process.append(mod.get_net(x))
                else:
                    input_nodes.append(nd)
                    if not isinstance(nd, BooleanVariable):
                        if len(nd.inputs) == 0:
                            to_process.append(mod.get_net(x))
            truth = target_net.source_instance.truth_value()
            target_node.assign(input_nodes, truth)

    @property
    def truth(self):
        collector = []
        for i in range(2**len(self.inputs)):
            bpattern = format(i, '0{}b'.format(len(self.inputs)))
            pattern = [x == '1' for x in bpattern]
            for j in range(len(self.inputs)):
                self.inputs[len(self.inputs) - 1 - j].assign(pattern[j])
            if self.target.evaluate():
                collector.append(i)
        if len(collector) == 0:
            return 0
        return sum([2**c for c in collector])






