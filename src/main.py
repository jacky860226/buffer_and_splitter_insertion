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
    moudle = Basic.Module(rawModule)
    delay_initialer = Up_delay_initialer(moudle)
    leveler = Leveler(moudle, delay_initialer, 'U')
    leveler.process()
    inserter = Inserter.Buffer_splitter_inserter(moudle)
    if arg.input is not None:
        with open(arg.output, 'w') as outputStream:
            moudle.verilog_output(outputStream)
    else:
        moudle.verilog_output(sys.stdout)
    print(arg.input)
    print("JJ level =", delay_initialer.max_delay() - 2)
    print("JJ count =", moudle.get_JJ_count())
    print("bufferNum =", inserter.buffer_cnt,
          ", splitterNum =", inserter.splitter_cnt, "\n")
