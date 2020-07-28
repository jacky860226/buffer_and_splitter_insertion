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
    VP.read_file(file_name)
    mod = VP.parse()
    print("\nGate count: {} Delay: {}".format(mod.gate_count, mod.delay))
    module = majority_mapper(mod, lib)
    module.net_renaming(0, "maj_n")
    module.instance_renaming(0, "maj_g")
    if len(argv) == 2:
        out_file = argv[1]
    else:
        out_file = file_name[:-2] + "_majority.v"
    with open(out_file, 'w+') as f:
        f.write(module.to_verilog())
    print("\nGate count: {} Delay: {}".format(module.gate_count, module.delay))

file_to_process = "./Files/decoder.v"

def main(argv):
    file = [file_to_process]
    if len(argv) > 0:
        file = argv
    process(file)

main(sys.argv[1:])
