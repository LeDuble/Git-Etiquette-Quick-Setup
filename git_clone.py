
from os import path
from git import Repo
from shutil import rmtree
import constant as c
from time import sleep

class GitClone:
    """Summary: 
        Clone the repository and creates temporary file for it
    """
    def create_temp_folder(self):
        # TODO: add docstring here

        # # !debugging
        # print(f"\nStarting {self.create_temp_folder.__name__} function")
        # print(f"Location -* {path.basename(__file__)} *-")
        # print("create_temp_folder \n")

        if not path.exists(c.temp_folder_path):
            print("\n")
            # wait until the folder has finished cloning (added "loading screen" incase internet connection is slow and wants to show its proceeding it nonetheless)
            while not path.exists(c.temp_folder_path):
                dots = ""
                if len(dots) == 3:
                    for i in range(0, len(dots)):
                        dots = dots.replace(".", "", 1)
                        print(f"{c.git_etiquette_repo_name} is cloning{dots}")
                        sleep(0.1)
        
                else:
                    dots += "."
                    print(f"{c.git_etiquette_repo_name} is cloning{dots}")
                sleep(0.1)
                # clone git etiquette template repository to temporary folder
                Repo.clone_from(c.git_etiquette_repo_url, c.temp_folder_path)
                
            print("Cloning was successful")
            print("Temporary folder created:", c.temp_workflows_path)
            return True
        else:
            print(f"Temporary folder {c.temp_folder} already exists, cannot continue.")
            # print(path_checker.items_requested[1]) # !debugging
            # print("create_temp_folder returns False") # !debugging
            rmtree(c.path_for_temp) # fix it later
            print("exiting the program")
            exit()