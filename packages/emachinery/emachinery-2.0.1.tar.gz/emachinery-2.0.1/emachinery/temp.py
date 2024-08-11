import yaml, os
from rich import print

with open(os.path.dirname(__file__)+'/signal_library.yaml', encoding='utf-8') as f:
    signal_library = yaml.load(f, Loader=yaml.FullLoader)

    print(signal_library)
