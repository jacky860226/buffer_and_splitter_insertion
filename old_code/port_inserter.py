from module import Module
from wires import *
from default_cell_library import *


cell_lib = Library()


def insert_port(host: Module):
    for port_in in host.inputs:
        source_port = set(port_in.post).pop()
        interim = host.create_wire()
        source_port.unbind()
        source_port.bind(interim)
        or_a = host.create_wire()
        or_b = host.create_wire()
        host.add_instance("{}_port_xnor_or".format(port_in.name), cell_lib.get("or_bb"),
                          {'a': or_a.name, 'b': or_b.name, 'c': interim.name})
        xnor_a = host.create_wire()
        xnor_b = host.create_wire()
        host.add_instance("{}_port_xnor_and".format(port_in.name), cell_lib.get("and_bb"),
                          {'a': xnor_a.name, 'b': xnor_b.name, 'c': or_a.name})
        host.add_instance("{}_port_xnor_and_ii".format(port_in.name), cell_lib.get("and_ii"),
                          {'a': xnor_a.name, 'b': xnor_b.name, 'c': or_b.name})
        xnor_b_end = xnor_b
        for i in range(4):
            xnor_b = host.create_wire()
            host.register_instance(
                cell_lib.get_buffer().instantiate("{}_bfr_after".format(xnor_b.name), host, [xnor_b, xnor_b_end]))
            xnor_b_end = xnor_b
        host.register_instance(
            cell_lib.get_splitter(2).instantiate("{}_port_splitter".format(port_in.name),
                                                 host, [port_in, xnor_a, xnor_b])
        )
