from module import Module
from pathlib import Path
from helper import fragment_split, get_between
from default_cell_library import Library


class VerilogParser:
    def __init__(self, lib: Library):
        self._cells = lib
        self._top_module = None
        self._parsed = None
        self._modules = dict()
        self.target = None

    def read_file(self, file_name: str):
        v_file = Path(file_name)
        if not v_file.is_file():
            print("file not exist")
            return False
        with open(file_name) as my_file:
            text = my_file.read()
        self._parsed = text.split(';')
        return True

    def read_string(self, file_contenr: str):
        self._parsed = file_contenr.split(';')
        return True

    def parse(self):
        for fragment in self._parsed:
            self._line_parser(fragment)
        return self.target

    def _line_parser(self, line):
        if "endmodule" in line:
            return
        if "module" in line:
            self._module_parser(line)
            return
        if "input " in line:
            self._inputs_parser(line)
            return
        if "output " in line:
            self._outputs_parser(line)
            return
        if "wire " in line:
            self._wire_parser(line)
            return
        if "assign" in line:
            assignment = line[line.find("assign") + len("assign"):].split('=')
            left = assignment[0].strip()
            right = assignment[1].strip()
            if self.target.get_net(left) is None or self.target.get_net(right) is None:
                width = self.target.wire_vectors.get(left) + 1
                for i in range(width):
                    r = "{}[{}]".format(right, str(i))
                    l = "{}[{}]".format(left, str(i))
                    self.target.add_alias(r, l)
            else:
                self.target.add_alias(right, left)
            return
        self._instance_parser(line)

    def _module_parser(self, line):
        essential = get_between(line, "module ")
        fragment = fragment_split(essential)
        if len(fragment) == 1:
            module_name = fragment[0].split('(')[0].strip()
        else:
            module_name = fragment[0].strip()
        if module_name not in self._modules.keys():
            self._modules[module_name] = Module(module_name)
        self.target = self._modules.get(module_name)
        module_part = get_between(essential, '(', ')').strip()
        self.target.set_interface(module_part.split(','))

    def _inputs_parser(self, line):
        fragment = fragment_split(line)
        if len(fragment) == 2:
            self.target.add_input(fragment[1].strip())
        else:
            self.target.add_input(fragment[2].strip(), int(get_between(fragment[1], '[', ':')))

    def _outputs_parser(self, line):
        fragment = fragment_split(line)
        if len(fragment) == 2:
            self.target.add_output(fragment[1].strip())
        else:
            self.target.add_output(fragment[2].strip(), int(get_between(fragment[1], '[', ':')))


    def _wire_parser(self, line):
        fragment = fragment_split(line)
        if len(fragment) == 2:
            self.target.add_wire(fragment[1].strip())
        else:
            try:
                self.target.add_wire(fragment[2].strip(), int(get_between(fragment[1], '[', ':')))
            except ValueError:
                print(fragment[1])

    def _instance_parser(self, line):
        fragment = fragment_split(line)
        cell = self._cells.get(fragment[0].strip())
        if len(fragment) == 2:
            name = fragment[1].split('(')[0].strip()
            ports = get_between(fragment[1], '(', ')').split(',')
        else:
            name = fragment[1].strip()
            ports = get_between(fragment[2], '(', ')').split(',')
        if cell is not None:
            mapping = dict()
            if '(' not in ports[0]:
                mapping = dict(zip(cell.interface, [p.strip() for p in ports]))
            else:
                for p in ports:
                    mapping[get_between(p, '.', '(').strip()] = get_between(p, '(', ')').strip()
            self.target.add_instance(name, cell, mapping)
        else:
            print("cell {} undefined".format(fragment[0]))
