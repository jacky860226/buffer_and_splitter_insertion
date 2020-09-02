import argparse
import Parser
import Middle
import sys


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
    # rawModule.print()
    middle = Middle.Middle(rawModule)
    # middle.printConnect()
    print("original JJ = ", middle.ori_jj)
    print("original buffer = ", middle.buffer_cnt, ", splitter = ",
          middle.splitter_cnt, "total = ", middle.buffer_cnt + middle.splitter_cnt)
    middle.BufferAndSplitterInsertion()
    print("new buffer = ", middle.new_buffer_cnt, ", splitter = ",
          middle.new_splitter_cnt, "total = ", middle.new_buffer_cnt + middle.new_splitter_cnt)

    fout = open(arg.input+".jinkela.v", "w")
    rawModule.verilog_output(fout)
    fout.close()

    # rawModule.print()
    middle_new = Middle.Middle(rawModule)
    print("new JJ = ", middle_new.ori_jj)
