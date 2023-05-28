import constant as c
import os
import shutil
import time

class MoveItems:
    # 1. TODO: Check if file already exist (already done)
    # 2. TODO: Make a list of files that is going to be moved dictionary
    # 3. TODO: start moving them with for loop


    def move_files(self):
        # TODO: add docstring

        # # !debugging
        # print(f"\nStarting {self.move_files.__name__} function")
        # print(f"Location -* {os.path.basename(__file__)} *-")
        # print("move_files \n")

        print("\nStarting to add files...")
        time.sleep(1)
        for idx, file_value in enumerate(c.item_destinations_dic.values()):
            file_name = file_value[0]
            source = os.path.join(file_value[1], file_name)
            destination = os.path.join(file_value[2], file_name)
            # print(file_value) # !debugging
            if destination in c.list_not_exist:
                shutil.move(source, destination)

                # print(f"Added {file_name} to {destination}") # !debugging
                print(f"""      [ {file_name.upper()} ] 
                ↳ was moved to @ {destination}""") 
        print("\nEverything was successfully added\n")
    
