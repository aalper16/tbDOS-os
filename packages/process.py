from packages import process_toml

def get():
    process_toml.get_data('reg/proc.toml')

def post(include):
    process_toml.load_data('reg/proc.toml', include)