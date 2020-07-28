from verilog_parser import VerilogParser
from majority_mapper import *
from data_levelers import DataLeveler, flow_checker, float_net_checker, missing_instance_test, splitter_checker
from default_cell_library import Library
from port_inserter import insert_port

# lib = Library()
# VP = VerilogParser(lib)
# file_name = "./Files/apc16.v"
# VP.read_file(file_name)
# module = VP.parse()
# print("\nBefore inserting buffers and splitters: Gate count: {} Delay: {}".format(module.gate_count, module.delay))
# module.reset_delay()
# dataleveller = DataLeveler(module, lib)
# dataleveller.process()
# print("\nAfter inserting buffers and splitters: Gate count: {} Delay: {}".format(module.gate_count, module.delay))
# float_net_checker(module)
# flow_checker(module)
# missing_instance_test(module)
# splitter_checker(module)
# # insert_port(module)
# module.net_renaming()
# module.instance_renaming()
# with open(file_name[:-2] + "_balanced.v", 'w+') as f:
#     f.write(module.to_verilog())


lib = Library()
VP = VerilogParser(lib)
file_name = "./Files/adder8.v"

VP.read_file(file_name)
# module = VP.parse()
mod = VP.parse()
module = majority_mapper(mod, lib)
# module.net_renaming()
# module.instance_renaming()
print(module.to_verilog())

# print("\nBefore inserting buffers and splitters: Gate count: {} Delay: {}".format(module.gate_count, module.delay))
# module.reset_delay()
# dataleveller = DataLeveler(module, lib)
# dataleveller.process()
# print("\nAfter inserting buffers and splitters: Gate count: {} Delay: {}".format(module.gate_count, module.delay))
# float_net_checker(module)
# flow_checker(module)
# missing_instance_test(module)
# splitter_checker(module)
# module.net_renaming()
# module.instance_renaming()
# with open(file_name[:-2] + "_balanced.v", 'w+') as f:
#     f.write(module.to_verilog())


