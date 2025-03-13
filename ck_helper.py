def print_attrs(obj, lvl=0):
    for k in obj.__dict__:
        value = getattr(obj, k)
        print('='*40)
        print('    ' * lvl, f'[{k}]')
        print('    ' * lvl, value)
        if type(value) == list:
            value = value[0]
        
        if '__dict__' in dir(value):
            print_attrs(value, lvl + 1)