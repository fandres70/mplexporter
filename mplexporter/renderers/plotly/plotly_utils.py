def convert_symbol(mpl_symbol):
    if mpl_symbol in symbol_map:
        return symbol_map[mpl_symbol]
    else:
        return 'dot'  # default


def convert_dash(mpl_dash):
    if mpl_dash in dash_map:
        return dash_map[mpl_dash]
    else:
        return 'solid'  # default


def get_x_domain(bounds):
    return [bounds[0], bounds[0] + bounds[2]]


def get_y_domain(bounds):
    return [bounds[1], bounds[1] + bounds[3]]


def clean_dict(node, parent=None, node_key=None):
    del_keys = []
    for key, item in node.items():
        if isinstance(item, dict):
            clean_dict(item, node, key)
        else:
            if item in [None, 'none', 'None']:
                del_keys += [key]
    for key in del_keys:
        del node[key]
    if parent is not None:
        if len(node) == 0:
            del parent[node_key]



dash_map = {
    '10,0': 'solid',
    '6,6': 'dash',
    '2,2': 'dot',
    '4,4,2,4': 'dashdot',
    'none': 'solid'
}

symbol_map = {
    'o': 'dot',
    'v': 'triangle-down',
    '^': 'triangle-up',
    '<': 'triangle-left',
    '>': 'triangle-right',
    's': 'square',
    '+': 'cross',
    'x': 'x',
    'D': 'diamond',
    'd': 'diamond',
    '-': 'solid',
    '--': 'dash',
    '-.': 'dashdot'
}