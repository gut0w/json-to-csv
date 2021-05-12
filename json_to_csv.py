import argparse
import csv
import json
from datetime import datetime
from jsonpath_ng import jsonpath, parse

DEFAULT_SEPARATOR = ';'

def main(filename: str, expression: str, separator: str) -> None:
    with open(filename, 'r') as file:
        data = json.loads(file.read())
        jsonpath_expr = parse(expression)
        
        for match in jsonpath_expr.find(data):
            keys = match.value.keys()
            break

        all_entries = [{key : value for key, value in match.value.items() if key in keys} for match in jsonpath_expr.find(data)]
        now = datetime.now().strftime('%Y-%m-%d_%H-%M')
        with open(f'result_{now}.csv', 'w', newline='') as output:
            dict_writer = csv.DictWriter(output, keys, delimiter=separator)
            dict_writer.writeheader()
            dict_writer.writerows(all_entries)
                
                        
            
        


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='enter filename')
parser.add_argument('expression', help='enter jsonPath expression')
parser.add_argument('separator', help='enter CSV separator character')
args = parser.parse_args()
print(args.filename, args.expression, args.separator if args.separator is not None else DEFAULT_SEPARATOR)
main(args.filename, args.expression, args.separator if args.separator is not None else DEFAULT_SEPARATOR)
    

    