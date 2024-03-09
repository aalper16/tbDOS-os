import toml

def get_data(name):
    with open(name, 'r') as get_toml:
        getdata = toml.load(get_toml)
        return getdata
    
def load_data(name, data):
    with open(name, 'w') as load_toml:
        toml.dump(data, load_toml)