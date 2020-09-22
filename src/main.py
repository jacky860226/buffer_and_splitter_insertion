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


def UpUpSolver(rawModule, wire_delay_adder_ty):
    module = Basic.Module(rawModule)

    delay_initialer = Up_delay_initialer(module)

    leveler = Leveler(module, delay_initialer, 'U',
                      wire_delay_adder_ty(module))
    leveler.process()

    inserter = Inserter.Buffer_splitter_inserter(module)
    inserter.insert_splitter()
    dec_buffer = inserter.buffer_decrease()
    inserter.insert_buffer_and_splitter()

    leveler.reset_unprocess_wire_delay()
    leveler.cal_wire_delay()
    for wire in module.wires:
        for delay in wire.output_delay.values():
            assert(delay == 0)

    JJ_level = delay_initialer.max_delay() - 2
    JJ_count = module.get_JJ_count()
    print("JJ level =", JJ_level)
    print("JJ count =", JJ_count)
    print("bufferNum =", inserter.buffer_cnt,
          ", splitterNum =", inserter.splitter_cnt)
    print("buffer decrease by decreaser:", dec_buffer)

    return module, JJ_level, JJ_count, inserter.buffer_cnt, inserter.splitter_cnt


def DownDownSolver(rawModule, wire_delay_adder_ty):
    module = Basic.Module(rawModule)

    delay_initialer = Down_delay_initialer(module)
    leveler = Leveler(module, delay_initialer, 'D',
                      wire_delay_adder_ty(module))
    leveler.process()

    inserter = Inserter.Buffer_splitter_inserter(module)
    inserter.insert_splitter()
    dec_buffer = inserter.buffer_decrease()
    inserter.insert_buffer_and_splitter()

    leveler.reset_unprocess_wire_delay()
    leveler.cal_wire_delay()
    for wire in module.wires:
        for delay in wire.output_delay.values():
            assert(delay == 0)

    JJ_level = delay_initialer.max_delay() - 2
    JJ_count = module.get_JJ_count()
    print("JJ level =", JJ_level)
    print("JJ count =", JJ_count)
    print("bufferNum =", inserter.buffer_cnt,
          ", splitterNum =", inserter.splitter_cnt)
    print("buffer decrease by decreaser:", dec_buffer)

    return module, JJ_level, JJ_count, inserter.buffer_cnt, inserter.splitter_cnt


def SecondSolver(rawModule, wire_delay_adder_ty):
    module = Basic.Module(rawModule)

    leveler = Second_leveler.Second_leveler(
        module, wire_delay_adder_ty(module))
    leveler.process()

    inserter = Inserter.Buffer_splitter_inserter(module)
    inserter.insert_splitter()
    dec_buffer = inserter.buffer_decrease()
    inserter.insert_buffer_and_splitter()

    JJ_level = leveler.delay_calculater.max_delay() - 2
    JJ_count = module.get_JJ_count()
    print("JJ level =", JJ_level)
    print("JJ count =", JJ_count)
    print("bufferNum =", inserter.buffer_cnt,
          ", splitterNum =", inserter.splitter_cnt)
    print("buffer decrease by decreaser:", dec_buffer)

    return module, JJ_level, JJ_count, inserter.buffer_cnt, inserter.splitter_cnt


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

    UpUp_module = UpUpSolver(rawModule, Wire_delay_adder.DynamicProgramming)[0]
    DownDown_module = DownDownSolver(
        rawModule, Wire_delay_adder.DynamicProgramming)[0]
    SecondSolver(rawModule, Wire_delay_adder.DynamicProgramming)

    print("")

    output_module = UpUp_module

    if output_module is not None:
        if arg.output is not None:
            with open(arg.output, 'w') as outputStream:
                output_module.verilog_output(outputStream)
        else:
            output_module.verilog_output(sys.stdout)
