import os
import constant as c

class FolderCreator:
    def __init__(self, folders):
        self.folders = folders

    def create_folders(self):
        # TODO: add docstring here

        # # !debugging
        # print(f"\nStarting {self.create_folders.__name__} function")
        # print(f"Location -* {os.path.basename(__file__)} *-")
        # print("create_folders \n")

        # check whether the current operation system is one of the two [nt or posix]
        # and construct/place/move the folders as assigned to the current operation system
        if c.operation_system in ["nt", "posix"]:

            if c.operation_system == "nt":
                for folder in self.folders:
                    if not os.path.exists(folder):
                        os.makedirs(folder)
                        c.folders_created.append(folder)

            elif c.operation_system == "posix":
                for folder in self.folders:
                    if not os.path.exists(folder):
                        os.mkdir(folder) # os.mkdir(folder, c.mode) # TODO: add mode here
                        c.folders_created.append(folder)
            
            # shows which folders were created
            for i in c.folders_created:
                print(f"folders created {i}")