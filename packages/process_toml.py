import toml

def get_data(name):
    with open(name, 'r') as gett_toml:
        getdata = toml.load(gett_toml)
        return getdata
    
def load_data(name, data):
    with open(name, 'a') as load_toml:
        toml.dump(data, load_toml)