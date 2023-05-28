import os
import constant as c

class CheckOS:
    def find_os(self):
        # TODO: add docstring

        # # !debugging
        # print(f"\nStarting {self.find_os.__name__} function")
        # print(f"Location -* {os.path.basename(__file__)} *-")
        # print("find_os\n")

        # TODO: add comments
        if os.name == "posix":
            # print("posix system detected") # !debugging
            c.operation_system += "posix"

        elif os.name == "nt":
            # print("nt system detected") # !debugging
            c.operation_system += "nt"
                # if it doesn't match either of the two given operation systems, then it will print the following message and exit
        else:
            print("Not supported operation system")
            exit() # TODO: add it in to driver file and change this part in to boolean operation, so that it returns either True or False
        
        return c.operation_system