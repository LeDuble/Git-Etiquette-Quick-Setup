import os
import constant as c
import time

class CheckExistence:
    """Summary:
        Check files and folders that are missing
    """

    def existence_validator(self):
        # TODO: add docstring

        # # !debugging
        # print(f"\nStarting {self.existence_validator.__name__} function")
        # print(f"Location -* {os.path.basename(__file__)} *-")
        # print("existence_validator\n")

        # TODO: need to add path, like os.getcwd + file name # !fixed perhaps?
        for idx, value in enumerate(c.item_dic.values()):
            # print(c.item_dic.get(idx), "debugging") # !debugging
            if os.path.exists(value[0]):
                # if it exist, dont replace # !keep this
                # print(f"yes {value[1]}") # !debugging
                c.list_exist.append(value[1])
                # print(files_exist) # !debugging
            else:
                # if it doesnt exist, do replace only prompted by user # !keep this
                # print(f"no {value[1]}") # !debugging
                c.list_not_exist.append(value[0]) # !value changed from 1 to 0
                
                # use this to check which folders do not exist in the project directory and make it in to a list
                if any(value[1] in values for i in c.folder_dic.values() for values in i):
                    c.folders_to_check.append(value[0])
                    # print("folders", c.folders_to_check) #! debugging
                    c.folders_found.append(value[1])
                
                elif any(value[1] in values for i in c.file_dic.values() for values in i):
                    c.files_found.append(value[1])
                    c.files_found_paths.append(value[0])
        
        
        # prints folders that are missing from the project directory
        print(f"\nThe project directory is missing following items: ")
        print("""
╭――――――――――――――――――――――――――――――――――――――――――――╮
│               -   Folders   -              │
╰――――――――――――――――――――――――――――――――――――――――――――╯
         """)
        if not c.folders_found:
            print("""      No necessary folders missing""")
        else:
            # time.sleep(0.25)
            for i in c.folders_found:
                dots = len(i)
                dotsdots = ""
                print(f"""      [ {i.upper()} ]""")
                for i in range(0, dots):
                    dotsdots += "―"
                print(f"""        {dotsdots}	""")
                # time.sleep(0.5)

        # prints files that are missing from the project directory
        print("""
╭―――――――――――――――――――――――――――――――――――――――――――――╮
│               -    Files    -               │
╰―――――――――――――――――――――――――――――――――――――――――――――╯
         """)
        if not c.files_found:
            print("""      No necessary files missing""")
        else:
            for i, y in  zip(c.files_found, c.files_found_paths):
                dots = len(i)
                dotsdots = ""
                print(f"""      [ {i.upper()} ] """)
            # ↳ @ {y}""") # this reveals the path where files going to be added to
                for i in range(0, dots):
                    dotsdots += "―"
                print(f"""        {dotsdots}	""")
                # time.sleep(0.5)
            print("\n...and these will be added via quick setup\n")