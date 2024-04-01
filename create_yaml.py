import yaml

data = {'train' : 'data_sets/train/images/',
        'val' : 'data_sets/valid/images/',
        'test' : 'data_sets/test/images/',
        'names' : ['megal', 'ilbe'],
        'nc' : 2}

with open('data_sets/data.yaml', 'w') as f:
    yaml.dump(data, f)
with open('ata_sets/data.yaml', 'r') as f:
    print(yaml.safe_load(f))