import argparse

get_args = argparse.ArgumentParser()
get_args.add_argument('filename', help='file you want to process')
get_args.add_argument('-o', '--output', default=None, 
                      help='output filename')
get_args.add_argument('-m', '--method', default=None, 
                      help='the method you want')

args = get_args.parse_args()

filename = args.filename
output = args.output
method = args.method

print('you want to convent to "{}" from "{}" via {}'
        .format(output, filename, method))