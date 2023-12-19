def convert_units(initial_unit, target_unit, value=1):
    units_table = {'in': {'in': 1, 'pt': 72.26999, 'mm': 25.40014},
                   'pt': {'in': 0.01384, 'pt': 1, 'mm': 0.35146},
                   'mm': {'in': 0.03937, 'pt': 2.84526, 'mm': 1}}

    return value * units_table[initial_unit][target_unit]
