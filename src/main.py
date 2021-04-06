import argparse
import Parser
import Basic
import Inserter
import sys
import Second_leveler
import Wire_delay_adder

from data_leveler import Up_delay_initialer, Down_delay_initialer, Leveler


def process_command():
    parser = argparse.ArgumentParser(prog='BufferAndSplitterAdder')
    parser.add_argument('--input', '-i', type=str, default=None,
                        required=False, help='Input file path.')
    parser.add_argument('--output', '-o', type=str, default=None,
                        required=False, help='Output file path.')
    return parser.parse_args()


def printer(module, JJ_level, JJ_count, buffer_cnt, splitter_cnt, dec_buffer):
    print("JJ level =", JJ_level)
    print("JJ count =", JJ_count)
    print("bufferNum =", buffer_cnt,
          ", splitterNum =", splitter_cnt)
    print("buffer decrease by decreaser:", dec_buffer)
    print("")


def UpUpSolver(rawModule, wire_delay_adder_ty, init_legal_delay=False):
    module = Basic.Module(rawModule)

    delay_initialer = Up_delay_initialer(module)

    leveler = Leveler(module, delay_initialer, 'U',
                      wire_delay_adder_ty(module), init_legal_delay)
    leveler.process()

    inserter = Inserter.Buffer_splitter_inserter(module)
    dec_buffer = inserter.insert_splitter()
    inserter.insert_buffer_and_splitter()

    leveler.reset_unprocess_wire_delay()
    leveler.cal_wire_delay()
    for wire in module.wires:
        for delay in wire.output_delay.values():
            assert(delay == 0)

    JJ_level = delay_initialer.max_delay() - 2
    JJ_count = module.get_JJ_count()

    return module, JJ_level, JJ_count, inserter.buffer_cnt, inserter.splitter_cnt, dec_buffer


def DownDownSolver(rawModule, wire_delay_adder_ty, init_legal_delay=False):
    module = Basic.Module(rawModule)

    print("cellNum:", len(module.cell_dict))

    delay_initialer = Down_delay_initialer(module)
    leveler = Leveler(module, delay_initialer, 'D',
                      wire_delay_adder_ty(module), init_legal_delay)
    leveler.process()

    inserter = Inserter.Buffer_splitter_inserter(module)
    dec_buffer = inserter.insert_splitter()
    inserter.insert_buffer_and_splitter()

    leveler.reset_unprocess_wire_delay()
    leveler.cal_wire_delay()
    for wire in module.wires:
        for delay in wire.output_delay.values():
            assert(delay == 0)

    JJ_level = delay_initialer.max_delay() - 2
    JJ_count = module.get_JJ_count()

    return module, JJ_level, JJ_count, inserter.buffer_cnt, inserter.splitter_cnt, dec_buffer


def SecondSolver(rawModule, wire_delay_adder_ty):
    module = Basic.Module(rawModule)

    leveler = Second_leveler.Second_leveler(
        module, wire_delay_adder_ty(module))
    leveler.process()

    inserter = Inserter.Buffer_splitter_inserter(module)
    dec_buffer = inserter.insert_splitter()
    inserter.insert_buffer_and_splitter()

    JJ_level = leveler.delay_calculater.max_delay() - 2
    JJ_count = module.get_JJ_count()

    return module, JJ_level, JJ_count, inserter.buffer_cnt, inserter.splitter_cnt, dec_buffer


if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    arg = process_command()
    parser = Parser.Parser()
    if arg.input is not None:
        inputStream = open(arg.input)
    else:
        inputStream = sys.stdin
    rawModule = parser.parse(inputStream)

    print(arg.input)

    # UpUp = UpUpSolver(rawModule, Wire_delay_adder.DynamicProgramming2, False)
    # printer(*UpUp)
    DownDown = DownDownSolver(
        rawModule, Wire_delay_adder.DynamicProgramming2, True)

    first = [DownDown]
    output = min(first, key=lambda x: x[2])

    # the old method
    '''
    for _ in range(1):
        DownDown = DownDownSolver(rawModule, Wire_delay_adder.SecondAdder)
        Second = SecondSolver(rawModule, Wire_delay_adder.SecondAdder)
        first = [output, DownDown, Second]
        output = min(first, key=lambda x: x[2])
    '''

    output_module = output[0]
    printer(*output)

    if output_module is not None:
        if arg.output is not None:
            with open(arg.output, 'w') as outputStream:
                output_module.verilog_output(outputStream)
        else:
            output_module.verilog_output(sys.stdout)
