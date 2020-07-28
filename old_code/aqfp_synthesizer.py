from verilog_parser import VerilogParser
from data_levelers import DataLeveler
from default_cell_library import Library
from majority_mapper import *
import sys


def process(argv):
    lib = Library()
    VP = VerilogParser(lib)
    if len(argv) < 1:
        print("Please enter input file")
        return
    file_name = argv[0]
    if not VP.read_file(file_name):
        print("File not found")
        return
    mod = VP.parse()
    module = majority_mapper(mod, lib)
    # module.net_renaming(0, "n")
    # module.instance_renaming(0, "g")
    # print(module.to_verilog())

    print("\n=============Base Model====================================\n")
    print("\nBefore inserting buffers and splitters: Gate count: {} Delay: {}".format(mod.gate_count, mod.delay))
    mod.reset_delay()
    dataleveller = DataLeveler(mod, lib)
    dataleveller.process()
    print("\nAfter inserting buffers and splitters: Gate count: {} Delay: {}".format(mod.gate_count, mod.delay))
    mod.net_renaming()
    mod.instance_renaming()
    out_file = file_name[:-2] + "_balanced.v"
    print("\nbalanced AOI base file saved as {}\n".format(out_file))
    with open(out_file, 'w+') as f:
        f.write(mod.to_verilog())

    print("\n=============Majority Model====================================\n")
    print("\nBefore inserting buffers and splitters: Gate count: {} Delay: {}".format(module.gate_count, module.delay))
    module.reset_delay()
    dataleveller = DataLeveler(module, lib)
    dataleveller.process()
    print("\nAfter inserting buffers and splitters: Gate count: {} Delay: {}".format(module.gate_count, module.delay))
    module.net_renaming()
    module.instance_renaming()
    out_file = file_name[:-2] + "_maj_balanced.v"
    print("\nbalanced MAJ base file saved as {}\n".format(out_file))
    with open(out_file, 'w+') as f:
        f.write(module.to_verilog())
    out_file = file_name[:-2] + "_maj_balanced_ac_dc.v"
    print("\nbalanced MAJ file with ac dc saved as {}\n".format(out_file))
    with open(out_file, 'w+') as f:
        f.write(module.to_aqfp_verilog())


file_to_process = "./Files/adder.v"


def main(argv):
    file = [file_to_process]
    if len(argv) > 0:
        file = argv
    process(file)

main(sys.argv[1:])
