import os 

libs = ['keras', 'opencv-python', 'pymysql', 'flask', 'toml', 'numpy']

def install_req():
    global libs
    for lib in libs:
        os.system('pip install '+lib)