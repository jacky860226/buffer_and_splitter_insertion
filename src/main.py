import argparse
import Parser
import Basic
import Inserter
import sys

from data_leveler import Up_delay_initialer, Down_delay_initialer, Leveler


def process_command():
    parser = argparse.ArgumentParser(prog='BufferAndSplitterAdder')
    parser.add_argument('--input', '-i', type=str, default=None,
                        required=False, help='Input file path.')
    parser.add_argument('--output', '-o', type=str, default=None,
                        required=False, help='Output file path.')
    return parser.parse_args()


if __name__ == '__main__':
    arg = process_command()
    parser = Parser.Parser()
    if arg.input is not None:
        inputStream = open(arg.input)
    else:
        inputStream = sys.stdin
    rawModule = parser.parse(inputStream)
    module = Basic.Module(rawModule)

    delay_initialer = Up_delay_initialer(module)
    leveler = Leveler(module, delay_initialer, 'U')
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

    if arg.input is not None:
        with open(arg.output, 'w') as outputStream:
            module.verilog_output(outputStream)
    else:
        module.verilog_output(sys.stdout)
    print(arg.input)
    print("JJ level =", delay_initialer.max_delay() - 2)
    print("JJ count =", module.get_JJ_count())
    print("bufferNum =", inserter.buffer_cnt,
          ", splitterNum =", inserter.splitter_cnt)
    print("buffer decrease by decreaser:", dec_buffer)
    print("")
