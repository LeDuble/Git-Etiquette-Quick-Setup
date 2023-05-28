import shutil
import os
import constant as c

def delete_setup_directory():
    dir = os.getcwd()
    # deletes quick setup
    shutil.rmtree(dir)
    # deletes temporary files
    shutil.rmtree(c.path_for_temp)