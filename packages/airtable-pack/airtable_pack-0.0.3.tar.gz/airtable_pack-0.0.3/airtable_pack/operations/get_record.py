from pyairtable import Table
from pyairtable.formulas import match

def get_record(table: Table, filter_: dict) -> dict:
    formula = match(filter_)
    result = table.all(formula=formula)
    return result
