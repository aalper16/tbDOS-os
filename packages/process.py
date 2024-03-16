import toml

def get_():
    with open('reg/proc.toml', 'r') as gett_toml:
        return toml.load(gett_toml)

def post(include):
    with open('reg/proc.toml', 'a') as load_toml:
        toml.dump(include, load_toml)
