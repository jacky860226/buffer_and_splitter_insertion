from abstract_net_model import LogicBlock
from instance import Instance
from module import Module
from default_cell_library import Library
from wires import Wire, PortIn, PortOut, Constant
from typing import Dict
from pins import PinIn, PinOut
import math


class Distributor(LogicBlock):
    def __init__(self, parent: Module, source: Wire, child_wires: Dict[Wire, int] = None):
        super().__init__("{}_v_fanout".format(source.name), parent)
        self._before = 0
        self._tracker = 0
        self._outputs = set()
        self._after = dict()
        self._delay_est = 1
        self._gate = 1
        if child_wires is None:
            org_post = set(source.post)
            for p in org_post:
                p.unbind()
                split_out_wire = parent.create_wire()
                p.bind(split_out_wire)
                self._add_wire(split_out_wire)
        else:
            for p in child_wires.keys():
                self._add_wire(p, child_wires[p])
        self._input = PinIn("v_fanout_in", self, source)

    def __hash__(self):
        return hash(self.name)

    def ideal_case(self):
        self._delay_est = 1
        self._gate = 1

    def reset_delay(self):
        self._before = 0
        for a in self._after.keys():
            self._after[a] = 0

    def worst_case(self, limit=2):
        self._delay_est = math.ceil(math.log(len(self._outputs), limit))
        self._gate = sum(limit**i for i in range(self._delay_est))

    def _add_wire(self, other: Wire, delay: int = 0):
        split_out_pin = PinOut("v_fanout_out_{}".format(str(self._tracker)), self, other)
        self._outputs.add(split_out_pin)
        self._tracker = self._tracker + 1
        self._after[split_out_pin.name] = delay

    def _level_up(self):
        new_source = self.parent.create_wire()
        internal_wires = dict()
        fo = len(self._outputs)
        for i in range(fo):
            wire, delay = self._pop_out()
            if delay > 0:
                delay = delay - 1
            internal_wires[wire] = delay
        ds = Distributor(self.parent, new_source, internal_wires)
        self._add_wire(new_source)
        return ds

    def _pop_out(self, pin: PinOut = None):
        if pin is None:
            pin = self._outputs.pop()
        else:
            self._outputs.remove(pin)
        delay = self._after[pin.name]
        wire = pin.connection
        pin.unbind()
        del self._after[pin.name]
        return wire, delay

    def _decompose(self, degree: int):
        total = len(self._outputs)
        basket = list()
        while total > degree:
            basket.append(degree)
            total = total - degree
        if total != 0:
            basket.append(total)
        if len(basket) > 1:
            if basket[-1] == 1:
                basket[-2] = basket[-2] - 1
        del basket[-1]
        return basket

    def add_delay(self, other: str, margin: int):
        if self._after.get(other) is None:
            print("No such connection")
            return
        self._after[other] = self._after.get(other) + margin

    def buffer_float(self):
        mutual = min(self._after.values())
        if mutual != 0:
            self._before = self._before + mutual
            for k in self._after.keys():
                self._after[k] = self._after[k] - mutual
        if isinstance(self._input.connection.source_instance, Distributor):
            self._input.connection.source_instance.add_delay(self._input.connection.source.name, self._before)
            self._before = 0

    def splitter_submerge(self):
        threashold = min(self._after.values())
        to_next = {x for x in self._outputs if self._after.get(x.name) > threashold}
        if len(to_next) <= 1:
            return self
        internal_splitter = self.parent.create_wire()
        self._add_wire(internal_splitter)
        to_next_wires = dict()
        for x in to_next:
            wire, delay = self._pop_out(x)
            to_next_wires[wire] = delay - 1
        child_splitter = Distributor(self.parent, internal_splitter, to_next_wires)
        return child_splitter.splitter_submerge()

    def break_up(self, degree: int, extra_splitters: set):
        if self in extra_splitters:
            print(self.name, self.fan_out)
        if len(self._outputs) <= degree:
            extra_splitters.add(self)
            self.buffer_float()
            upper = self._input.connection.source_instance
            if not isinstance(upper, Distributor):
                return
            else:
                return upper.break_up(degree, extra_splitters)
        upper = self._input.connection.source_instance
        if not isinstance(upper, Distributor):
            lower = self._level_up()
            return lower.break_up(degree, extra_splitters)
        extra_splitters.add(self)
        basket = self._decompose(degree)
        for item in basket:
            internal_wires = dict()
            for i in range(item):
                wire, delay = self._pop_out()
                internal_wires[wire] = delay
            sibling = self.parent.create_wire()
            ds = Distributor(self.parent, sibling, internal_wires)
            extra_splitters.add(ds)
            upper._add_wire(sibling)
            ds.buffer_float()
        self.buffer_float()
        return upper.break_up(degree, extra_splitters)

    @property
    def source(self):
        return self._input.connection

    @property
    def input_pins(self):
        return [self._input]

    @property
    def fan_out(self):
        return len(self._outputs)

    @property
    def output_pins(self):
        return self._outputs

    def get_delay(self, other: str):
        if self._after.get(other) is None:
            print("No such connection")
            return
        return self._before + self._delay_est + self._after.get(other)

    @property
    def max_delay(self):
        return self._before + self._delay_est + max(self._after.values())

    @property
    def ideal_gate_count(self):
        dls = list(self._after.values())
        finals = list()
        level = 1
        while(True):
            count = sum(x > min(dls) for x in dls)
            if count <= 1:
                finals = dls
                break
            level = level + 1
            finals.extend([x for x in dls if x == min(dls)])
            dls = [x - 1 for x in dls if x > min(dls)]
            level = level + min(dls)
            dls = [x - min(dls) for x in dls]
        return 2 * level + self._before * 2 + 2 * sum(finals)

    @property
    def gate_count(self):
        return 2 * self._gate + self._before * 2 + 2 * sum(x for x in self._after.values())

    def to_verilog(self):
        return "Black box"

    def cell_mapping(self, library: Library):
        buffer_model = library.get_buffer()
        input_wire = self._input.connection
        self._input.unbind()
        for i in range(self._before):
            wire_down = self.parent.create_wire()
            self.parent.register_instance(
                buffer_model.instantiate("{}_bfr_after".format(wire_down.name), self.parent, [input_wire, wire_down]))
            input_wire = wire_down
        wires = [input_wire]
        for x in self._outputs:
            output_wire = x.connection
            delay = self._after[x.name]
            x.unbind()
            for i in range(delay):
                wire_up = self.parent.create_wire()
                self.parent.register_instance(
                    buffer_model.instantiate("{}_bfr_before".format(wire_up.name), self.parent,
                                             [wire_up, output_wire]))
                output_wire = wire_up
            wires.append(output_wire)
        splitter_model = library.get_splitter(self.fan_out)
        self.parent.register_instance(splitter_model.instantiate(self.name, self.parent, wires))


class VirtualBuffer(LogicBlock):
    def __init__(self, parent: Module, source: Wire, delay: int):
        super().__init__("{}_v_buffer".format(source.name), parent)
        buf_out = parent.create_wire()
        org_post = set(source.post)
        for p in org_post:
            p.unbind()
            p.bind(buf_out)
        self._input = PinIn("v_bfr_in", self, source)
        self._output = PinOut("v_bfr_out", self, buf_out)
        self._delay = delay

    @property
    def input_pins(self):
        return [self._input]

    @property
    def output_pins(self):
        return {self._output}

    def get_delay(self, other=None):
        return self._delay

    def decrease(self, margin: int = 1):
        if self._delay == 0:
            print("delay is already 0")
            return
        self._delay = self._delay - margin
        if self._delay == 0:
            source = self._input.connection
            self._input.unbind()
            to = self._output.connection
            self._output.unbind()
            to.post.pop().bind(source)
            self.parent.remove_net(to.name)

    def increase(self, margin: int = 1):
        self._delay = self._delay + margin

    @property
    def gate_count(self):
        return 2 * self._delay

    def to_verilog(self):
        return "Black box"

    def cell_mapping(self, library):
        if self._delay == 0:
            return
        buffer_model = library.get_buffer()
        input_wire = self._input.connection
        self._input.unbind()
        for i in range(self._delay - 1):
            wire_down = self.parent.create_wire()
            self.parent.register_instance(
                buffer_model.instantiate("{}_bfr_after".format(wire_down.name), self.parent, [input_wire, wire_down]))
            input_wire = wire_down
        output_wire = self._output.connection
        self._output.unbind()
        self.parent.register_instance(
            buffer_model.instantiate("{}_bfr_after".format(output_wire.name), self.parent, [input_wire, output_wire]))


class DataLeveler:
    def __init__(self, target: Module, cell: Library):
        self.module = target
        self.cell = cell
        self.virtual_splitters = set()
        self.virtual_splitters_final = set()
        self.virtual_buffers = set()

    def process(self):
        self.insert_virtual_splitters()
        self.insert_virtual_buffers()
        self.module.reset_delay()
        self.level_outputs()
        self.register_instances()

    def _level_inputs(self, target: Instance):
        if len(target.input_pins) > 1:
            pre_wires = [x.connection for x in target.input_pins]
            delays = [self.module.get_delay(x.name) for x in pre_wires]
            buffer_table = dict(zip(pre_wires, delays))
            for pre in pre_wires:
                to_be_added = max(delays) - buffer_table[pre]
                if to_be_added != 0:
                    if pre.source is not None:
                        if isinstance(pre.source.parent, VirtualBuffer):
                            pre.source.parent.increase(to_be_added)
                            continue
                        if isinstance(pre.source.parent, Distributor):
                            pre.source.parent.add_delay(pre.source.name, to_be_added)
                            continue
                    self.virtual_buffers.add(VirtualBuffer(self.module, pre, to_be_added))

    def insert_virtual_splitters(self):
        nets = {self.module.get_net(x) for x in self.module.nets}
        for net in nets:
            if len(net.post) > 1:
                self.virtual_splitters.add(Distributor(self.module, net))
        for out in self.module.outputs:
            out.remove_pre_assignment()
        # self.ideal_case_solver()
        # self.worst_case_solver()
        self.clean_up()
        virtual_splitters_sorted = list(self.virtual_splitters)
        while len(virtual_splitters_sorted) != 0:
            self.module.reset_delay()
            virtual_splitters_sorted.sort(key=lambda x: (self.module.get_delay(x.source.name), x.max_delay))
            vs = virtual_splitters_sorted.pop(0)
            self._break_splitter(vs)

    def _break_splitter(self, vs: Distributor):
        for out in vs.output_pins:
            net = out.connection
            margin = 0
            if len(net.post) != 0:
                instance = set(net.post).pop().parent
                mutual = max(self.module.get_delay(x.connection.name) for x in instance.input_pins)
                margin = mutual - self.module.get_delay(net.name)
            else:
                if isinstance(net, PortOut):
                    delays = self.module.delays
                    margin = max(delays.values()) - delays.get(net.name)
            if margin != 0:
                vs.add_delay(out.name, margin)
        vs_leaf = vs.splitter_submerge() # TODO: VirtualSplitterGeneration
        vs_leaf.break_up(self.cell.max_fan_out, self.virtual_splitters_final) # TODO: VirtualSplitterMapping

    def level_outputs(self):
        delays = self.module.delays
        max_delay = max(delays.values())
        for port in delays.keys():
            margin = max_delay - delays.get(port)
            if margin == 0:
                continue
            port_net = self.module.get_net(port)
            if isinstance(port_net.source_instance, Distributor):
                port_net.source_instance.add_delay(port_net.source.name, margin)
                continue
            if isinstance(port_net.source_instance, VirtualBuffer):
                port_net.source.parent.increase(margin)
                continue
            if port_net.alias is None:
                port_net.create_pre_assignment()
            pre = port_net.alias
            self.virtual_buffers.add(VirtualBuffer(self.module, pre, margin))
            port_net.remove_pre_assignment()

    def insert_virtual_buffers(self):
        self.module.reset_delay()
        for instance in self.module.instances:
            self._level_inputs(instance)

    def register_instances(self):
        splitter_count = 0
        print("\n max delay after inserting splitters and buffers is : {}".format(self.module.delay))
        self.module.reset_delay()
        virtual_splitters_sorted = list(self.virtual_splitters_final)
        virtual_splitters_sorted.sort(key=lambda x: self.module.get_delay(x.source.name), reverse=True)
        for vs in virtual_splitters_sorted:
            vs.buffer_float()
            vs.cell_mapping(self.cell)
            splitter_count = splitter_count + 1
        for vb in self.virtual_buffers:
            if vb.get_delay() != 0:
                vb.cell_mapping(self.cell)
            else:
                if vb.output_pins.pop().connection is not None:
                    print("Test Failed")
        print("\n\tthe number of splitters added is: {}".format(splitter_count))
        self.module.reset_delay()

    def ideal_case_solver(self):
        gate_overhead = 0
        self.module.reset_delay()

        for vs in self.virtual_splitters:
            vs.reset_delay()
            vs.ideal_case()
        virtual_splitters_sorted = list(self.virtual_splitters)
        while len(virtual_splitters_sorted) != 0:
            self.module.reset_delay()
            virtual_splitters_sorted.sort(key=lambda x: (self.module.get_delay(x.source.name), x.max_delay))
            vs = virtual_splitters_sorted.pop(0)
            for out in vs.output_pins:
                net = out.connection
                margin = 0
                if len(net.post) != 0:
                    instance = set(net.post).pop().parent
                    mutual = max(self.module.get_delay(x.connection.name) for x in instance.input_pins)
                    margin = mutual - self.module.get_delay(net.name)
                else:
                    if isinstance(net, PortOut):
                        delays = self.module.delays
                        margin = max(delays.values()) - delays.get(net.name)
                if margin != 0:
                    vs.add_delay(out.name, margin)
            vs.buffer_float()
        self.module.reset_delay()
        for target in self.module.instances:
            if len(target.input_pins) > 1:
                pre_wires = [x.connection for x in target.input_pins]
                delays = [self.module.get_delay(x.name) for x in pre_wires]
                buffer_table = dict(zip(pre_wires, delays))
                for pre in pre_wires:
                    to_be_added = max(delays) - buffer_table[pre]
                    self.module.set_delay(pre.name, max(delays))
                    gate_overhead += to_be_added
        self.module.reset_delay()
        delays = self.module.delays
        for o in self.module.outputs:
            margin = max(delays.values()) - delays.get(o.name)
            gate_overhead += margin
        print("\n \tIdeal case: Gate Count: {} Delay: {}".format(self.module.gate_count + 2 * gate_overhead
                                                                 + sum(vs.ideal_gate_count for vs in self.virtual_splitters),
                                                                 self.module.delay))

    def worst_case_solver(self):
        gate_overhead = 0
        self.module.reset_delay()

        for vs in self.virtual_splitters:
            vs.reset_delay()
            vs.worst_case(4)
        self.module.reset_delay()
        for vs in self.virtual_splitters:
            for out in vs.output_pins:
                net = out.connection
                margin = 0
                if len(net.post) != 0:
                    instance = set(net.post).pop().parent
                    mutual = max(self.module.get_delay(x.connection.name) for x in instance.input_pins)
                    margin = mutual - self.module.get_delay(net.name)
                else:
                    if isinstance(net, PortOut):
                        delays = self.module.delays

                        margin = max(delays.values()) - delays.get(net.name)
                if margin != 0:
                    vs.add_delay(out.name, margin)
        self.module.reset_delay()
        for target in self.module.instances:
            if len(target.input_pins) > 1:
                pre_wires = [x.connection for x in target.input_pins]
                delays = [self.module.get_delay(x.name) for x in pre_wires]
                buffer_table = dict(zip(pre_wires, delays))
                for pre in pre_wires:
                    to_be_added = max(delays) - buffer_table[pre]
                    self.module.set_delay(pre.name, max(delays))
                    gate_overhead += to_be_added
        delays = self.module.delays
        for o in self.module.outputs:
            margin = max(delays.values()) - delays.get(o.name)
            gate_overhead += margin
        print("\n \tWorst case: Gate Count: {} Delay: {}".format(self.module.gate_count + 2 * gate_overhead
                                                                 + sum(vs.gate_count for vs in self.virtual_splitters),
                                                                 self.module.delay))

    def clean_up(self):
        self.module.reset_delay()
        for vs in self.virtual_splitters:
            vs.reset_delay()
            vs.ideal_case()


def flow_checker(module: Module):
    module.reset_delay()
    net_names = module.nets
    passed = True
    for net_name in net_names:
        net = module.get_net(net_name)
        if len(net.get_parents()) >= 1:
            delays = {module.get_delay(pre.name) for pre in net.get_parents()}
            if len(delays) == 1:
                continue
            else:
                passed = False
                print("\nUnequal path found at node {}".format(net_name))
    delays = {module.delays.values()}
    if len(delays) != 1:
        print("\nOutputs delay not equal")
        passed = False
    if passed:
        print("\nEven data path test passed.")


def splitter_checker(module: Module):
    net_names = module.nets
    passed = True
    falied_instance = set()
    for net_name in net_names:
        net = module.get_net(net_name)
        if len(net.post) > 1:
            passed = False
            print("Unresolved fan-out found at net {}, fan out num {}".format(net_name, len(net.post)))
            for ins in net.post:
                if isinstance(ins.parent, Distributor):
                    falied_instance.add(ins.parent.name)
    if passed:
        print("\nfan out check passed.")
    return falied_instance


def float_net_checker(module: Module):
    net_names = module.nets
    passed = True
    for net_name in net_names:
        net = module.get_net(net_name)
        if not isinstance(net, PortIn) and not isinstance(net, PortOut) and not isinstance(net, Constant):
            if len(net.post) == 0 or net.source is None:
                passed = False
                print("isolated net found at {}".format(net_name))
    if passed:
        print("\nNetlist check complete")


def missing_instance_test(module: Module):
    net_names = module.nets
    inst_names = module.instance_names
    passed = True
    for net_name in net_names:
        net = module.get_net(net_name)
        if net.source_instance is not None:
            if net.source_instance.name not in inst_names:
                passed = False
                print("net {} source instance {} not recorded in module.".format(net_name, net.source_instance.name))
    if passed:
        print("\nInstance check passed")


