from abstract_net_model import LogicBlock
from module import Module
from wires import *
from typing import List
from logic_cut import *
from default_cell_library import *
from verilog_parser import *


majority_primary_gates = [
            0, 255,
            170, 85, 204, 51, 240, 15,
            136, 119, 160, 95, 192, 63,
            34, 221, 10, 245, 12, 243,
            17, 238, 5, 250, 3, 252,
            68, 187, 80, 175, 48, 207,
            232, 23, 212, 43, 178, 77, 142, 113
]

majority_primary_truth = [
            None, None,
            2, 1, 2, 1, 2, 1,
            8, 7, 8, 7, 8, 7,
            2, 13, 2, 13, 2, 13,
            1, 14, 1, 14, 1, 14,
            4, 11, 4, 11, 4, 11,
            232, 23, 212, 43, 178, 77, 142, 113
        ]

majority_primary_inputs = [
            [], [],
            [0], [0], [1], [1], [2], [2],
            [0, 1], [0, 1], [0, 2], [0, 2], [1, 2], [1, 2],
            [0, 1], [0, 1], [0, 2], [0, 2], [1, 2], [1, 2],
            [0, 1], [0, 1], [0, 2], [0, 2], [1, 2], [1, 2],
            [0, 1], [0, 1], [0, 2], [0, 2], [1, 2], [1, 2],
            [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]
]

majority_blocks = dict()
majority_found = set()
skipped = set()


def majority_feasible_checker(target: Wire, maj_mod: Module):
    if len(target.get_parents()) != 2:
        return {}
    level = 4
    parents = target.get_parents()
    lp = parents.pop().get_ancestors(level)
    rp = parents.pop().get_ancestors(level)
    if isinstance(lp, dict):
        print(lp)
    if isinstance(rp, dict):
        print(rp)
    total = set.union(lp, rp, target.get_parents())
    ancestors = set.intersection(lp, rp)
    if len(ancestors) == 0:
        return {}
    comb = list()
    temp = set(ancestors)
    single_table = {x.name: True for x in ancestors}
    while len(temp) != 0:
        ans = temp.pop()
        for a in temp:
            if set.intersection(ans.get_children(), a.get_children(), ancestors) != 0:
                if not ans.is_descendent_of(a, level*2) and not a.is_descendent_of(ans):
                    comb.append({ans, a})
                    single_table[ans.name] = False
                    single_table[a.name] = False
        if single_table[ans.name]:
            comb.append({ans})

    border = set()
    score = 0
    raw_score = 0

    for x in comb:
        destination = set(x)
        temp_boarder = {target}
        while len(destination) != 0:
            for tb in set(temp_boarder):
                if tb in destination:
                    to_remove = True
                    for tb2 in temp_boarder:
                        if tb2.is_descendent_of(tb, level*2):
                            to_remove = False
                            break
                    if to_remove:
                        destination.remove(tb)
                    continue
                for d in destination:
                    if tb.is_descendent_of(d, level * 2):
                        temp_boarder.remove(tb)
                        temp_boarder.update(tb.get_parents())
                        break
        clean_boarder = set()
        for t in temp_boarder:
            if not isinstance(t, Constant):
                clean_boarder.add(t)
        if len(clean_boarder) <= 3:
            evaluator = set()
            for eva in total:
                if eva in evaluator:
                    continue
                for tb in temp_boarder:
                    if eva.is_descendent_of(tb, level*2):
                        if maj_mod.get_net(eva.name) is None and eva.name not in skipped:
                            evaluator.add(eva)
                        break
            if len(evaluator) - sum(b.name in skipped for b in temp_boarder) > score:
                border = temp_boarder
                score = len(evaluator) - sum(b.name in skipped for b in temp_boarder)
                raw_score = len(evaluator)
                continue
            if len(evaluator) - sum(b.name in skipped for b in temp_boarder) == score:
                # print(target.name, len(evaluator), score, raw_score, [x.name for x in border], [x.name for x in temp_boarder])
                if len(border) == 0:
                    border = temp_boarder
                    score = len(evaluator) - sum(b.name in skipped for b in temp_boarder)
                    raw_score = len(evaluator)
                else:
                    if len(evaluator) > raw_score:
                        border = temp_boarder
                        score = len(evaluator) - sum(b.name in skipped for b in temp_boarder)
                        raw_score = len(evaluator)

    if len(border) != 3:
        return {}
    for t in total:
        for b in border:
            if t.is_descendent_of(b, level*2):
                skipped.add(t.name)
                break
    return border


def majority_picking(target: Module, lib: Library):
    maj_mod = target.interface_copy()
    dfs = list(target.outputs)
    rev = False
    dfs.sort(key=lambda x: target.get_delay(x.name), reverse=rev)
    visited = set()
    while len(dfs) != 0:
        cur = dfs.pop()
        if isinstance(cur, PortIn) or isinstance(cur, Constant):
            continue
        if cur in visited:
            continue
        if maj_mod.get_net(cur.name) is None:
            maj_mod.add_wire(cur.name)
        border = majority_feasible_checker(cur, maj_mod)
        feasible = False

        if len(border) == 3:
            l = LogicCut(cur, list(border), target)
            selection = majority_seperation(l.truth)
            if selection is not None:
                feasible = True
                border_sorted = list(border)
                border_sorted.sort(key=lambda x: target.get_delay(x.name), reverse=rev)
                for b in border_sorted:
                    if maj_mod.get_net(b.name) is None:
                        maj_mod.add_wire(b.name)
                    if b not in visited:
                        dfs.append(b)
                if len(selection) == 1:
                    sela = set(selection).pop()
                    if len(sela) == 1:
                        t_truth = majority_primary_gates[sela[0]]
                        gate_mapping(maj_mod, cur, [maj_mod.get_net(b.name) for b in border], t_truth, lib)
                        # print(l.truth, cur.name, [b.name for b in border])
                else:
                    majority_blocks[cur.name] = tuple([[maj_mod.get_net(b.name) for b in border], selection])
                    # print(l.truth, cur.name, [b.name for b in border])
        if not feasible:
            parents = cur.get_parents()
            parents_sorted = list(parents)
            parents_sorted.sort(key=lambda x: target.get_delay(x.name), reverse=rev)
            for parent in parents_sorted:
                if maj_mod.get_net(parent.name) is None:
                    maj_mod.add_wire(parent.name)
                if parent not in visited:
                    dfs.append(parent)
            inst = cur.source_instance
            if inst is not None:
                if isinstance(inst, Alias):
                    maj_mod.add_alias(inst.wire_in.name, inst.wire_out.name)
                else:
                    mapping = {x: inst.pins.get(x).connection.name for x in inst.model.interface}
                    maj_mod.add_instance(inst.name, inst.model, mapping)
        if cur.name in skipped:
            skipped.remove(cur.name)
        visited.add(cur)
    return maj_mod


def majority_seperation(target: int):
    results = set()
    total = len(majority_primary_gates)
    if target in majority_primary_gates:
        sel = majority_primary_gates.index(target)
        if sel > 31:
            return {tuple([sel])}
        return
    for i in range(total):
        for j in range(i + 1, total):
            for k in range(j + 1, total):
                truths = tuple([i, j, k])
                mapped = True
                patterns = [format(majority_primary_gates[x], '08b') for x in truths]
                t_value = format(target, '08b')
                for item in range(8):
                    if t_value[item] == '1' and sum([x[item] == '1' for x in patterns]) <= 1:
                        mapped = False
                        break
                    if t_value[item] == '0' and sum([x[item] == '1' for x in patterns]) >= 2:
                        mapped = False
                        break
                if mapped:
                    results.add(truths)
    if len(results) == 0:
        return
    widths = [sum(s < 2 for s in x)for x in results]
    width = max(widths)
    if width > 1:
        return
    return results


def majority_mapping(lib: Library, mod: Module):
    for mb in majority_blocks.keys():
        border = [mod.get_net(x.name) for x in majority_blocks[mb][0]]
        selection = majority_blocks[mb][1]
        internal_nets = dict()
        for candidate in set.union(*[b.get_children() for b in border]):
            bdn = set(x.name for x in candidate.get_parents())
            mutual = set.intersection(set(x.name for x in candidate.get_parents()), set(b.name for b in border))
            if mutual == bdn:
                if candidate.name not in majority_blocks.keys():
                    candidate_inputs = [BooleanVariable(x.connection.name) for x in
                                        candidate.source_instance.input_pins]
                    candidate_truth = candidate.source_instance.truth_value(None)
                    candidate_boolean = BooleanNode(candidate.name)
                    candidate_boolean.assign(candidate_inputs, candidate_truth)
                    candidate_boolean.reorder([b.name for b in border])
                    pos = [[b.name for b in border].index(x.name) for x in candidate_boolean.inputs]
                    for i in range(40):
                        if majority_primary_truth[i] == candidate_boolean.truth_value and majority_primary_inputs[i] == pos:
                            internal_nets[i] = candidate
                            break
        min_selection = None
        final_selection = None
        for s in selection:
            temp = set.union(set(int(x/2) for x in internal_nets.keys()), set(int(x/2) for x in s))
            if min_selection is None:
                min_selection = temp
                final_selection = s
            else:
                if len(temp) < len(min_selection):
                    min_selection = temp
                    final_selection = s
                    continue
                if len(temp) == len(min_selection):
                    if sum(x > 3 for x in temp) < sum(x > 3 for x in min_selection):
                        min_selection = temp
                        final_selection = s

        final = list()
        pre_wires = list()
        for c in final_selection:
            if internal_nets.get(c) is None:
                if c % 2 == 1:
                    counter = c - 1
                else:
                    counter = c + 1
                if internal_nets.get(counter) is None:
                    pre_wires.append(None)
                    final.append(True)
                else:
                    pre_wires.append(internal_nets.get(counter))
                    final.append(False)
            else:
                pre_wires.append(internal_nets.get(c))
                final.append(True)

        majority_mapping_single(lib, mod, mod.get_net(mb), border, final_selection, pre_wires, final)


def majority_mapping_single(lib: Library, mod: Module, target: Wire, border: list,
                            selection: tuple, pre_wire: list, final: list):
    internals = list()
    if len(border) != 3 or len(selection) != 3 or len(final) != 3 or len(pre_wire) != 3:
        return
    value = 232
    for i in range(3):
        if selection[i] == 0:
            value = 8
            del final[i]
            continue
        if selection[i] == 1:
            value = 14
            del final[i]
            continue
        if selection[i] < 8:
            internals.append(border[i])
            if majority_primary_truth[selection[i]] == 1:
                final[i] = not final[i]
        else:
            if pre_wire[i] is not None:
                internals.append(pre_wire[i])
            else:
                new_wire = mod.create_wire()
                internals.append(new_wire)
                truth = majority_primary_truth[selection[i]]
                start_border = [border[x] for x in majority_primary_inputs[selection[i]]]
                gate_mapping(mod, new_wire, start_border, truth, lib)
    bn = BooleanNode(target.name)
    inputs = [BooleanVariable(x.name) for x in internals]
    bn.assign(inputs, value)
    for i in range(len(final)):
        if not final[i]:
            bn.negate(inputs[i].name)
    gate_mapping(mod, target, internals, bn.truth_value, lib)


def gate_mapping(mod: Module, target: Wire, border: list, truth: int, lib: Library):
    model = lib.get_mapping(truth)
    mapping = dict(zip(model.input_labels, [b.name for b in border]))
    mapping[model.output_labels[0]] = target.name
    mod.add_instance("{}_maj_net".format(target.name), model, mapping)


def majority_mapper(mod: Module, lib: Library):
    maj_mod = majority_picking(mod, lib)
    majority_mapping(lib, maj_mod)
    return maj_mod


class MajorityBlock(LogicBlock):
    def __init__(self, parent: Module, source: Wire, inputs: List[Wire], truth: int):
        name = "{}_pre_majority".format(source.name)
        super().__init__(name, parent)
        self._inputs = inputs
        self._output = source
        self.truth = truth

    @property
    def input_pins(self):
        return self._inputs

    @property
    def output_pins(self):
        return {self._output}

    def get_delay(self, other: str = None):
        return 2

    def gate_count(self):
        return 0

    def to_verilog(self):
        return "\tMajority_block ({}, {}, {})".format(self._output.name,
                                                      ";".join([i.name for i in self.input_pins]),
                                                               self.truth)
    def cell_mapping(self, library):
        pass


