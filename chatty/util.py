import codecs

import yaml

def load_vars(vars_file='vars.yml'):
    return yaml.load(codecs.open(vars_file, encoding='utf-8'))
