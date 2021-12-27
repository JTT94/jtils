from argparse import Namespace

def dict_to_namespace(mydict):
    return  Namespace(**mydict)

def namespace_to_dict(ns, copy=True):
    d = vars(ns)
    if copy:
        d = d.copy()
    return d
