import sys
import csv

csv_reader = csv.reader(sys.stdin)

def isTypeNumeric(s):
    try:
        f_val = float(s)  # Attempt to convert to float first
        return True
    except ValueError:
        return False

def renderCol(s):
    if s == '':
        return 'NULL'
    if isTypeNumeric(s):
        return s
    else:
        return f"'{s}'"


csv_columns = next(csv_reader)
csv_rows = list(csv_reader)


sql_values = 'select * from (values\n' + \
    ',\n'.join('  (' +', '.join(renderCol(col) for col in row) + ')' for row in csv_rows) + \
    '\n) as t(' + ', '.join(f'"{col}"' for col in csv_columns) + ')'

print(sql_values)
