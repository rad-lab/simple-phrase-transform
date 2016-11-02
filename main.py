import argparse
import sys
import simple_phrase_transform


def __extract_file_contents(file):
    f = open(file, 'r')
    contents = []
    for line in f:
        line = line.replace('\n', '')
        contents.append(line)
    f.close()
    return contents


def __write_file(file, content_array):
    f = open(file, 'w+')
    for line in content_array:
        f.write(line + '\n')
    f.close()


def execute(input_file, output_file, grammar_file):

    inputs = __extract_file_contents(input_file)
    grammars = __extract_file_contents(grammar_file)

    simple_phrase_transform.init(grammars)

    output = simple_phrase_transform.transform_batch(inputs)
    __write_file(output_file, output)


if __name__ == "__main__":
    arguments = sys.argv

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--input-file',
        nargs=1,
        help="Input file with phrases to transform",
        dest='input_file'
    )
    parser.add_argument(
        '-o', '--output-file',
        nargs=1,
        help="Destination file for all generated phrases",
        dest='output_file'
    )
    parser.add_argument(
        '-g', '--grammar-file',
        nargs=1,
        help="File with all simple grammar rules",
        dest='grammar_file'
    )

    try:
        args = parser.parse_args()

        arg_input_file = args.input_file[0]
        arg_output_file = args.output_file[0]
        arg_grammar_file = args.grammar_file[0]

    except TypeError:
        sys.exit("Parameters are not valid")

    execute(arg_input_file, arg_output_file, arg_grammar_file)
