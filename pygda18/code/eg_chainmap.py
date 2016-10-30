from collections import ChainMap

defaults = {
    'bg_color': 'black',
    'max_items': 10
}

config = ChainMap(defaults)
config.maps.insert(0, {'max_items': 20})

print(config)
print(config['max_items'])
