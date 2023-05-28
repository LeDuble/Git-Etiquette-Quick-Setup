from os import path
from shutil import rmtree
from os import path
import constant as c

class PromptContinue:
    def continue_or_not(self):
        # TODO: add docstring

        # # !debugging
        # print(f"\nStarting {self.continue_or_not.__name__} function")
        # print(f"Location -* {path.basename(__file__)} *-")
        # print("continue_or_not\n")

        # prompt user whether to continue or not, only accepts y or n, exits if n chosen otherwise continue
        while True:
            want_to_continue = input("\nWould you like to continue? (y/n): ")
            if want_to_continue in ["y", "n"]:
                if want_to_continue == "y":
                    return True
                else:
                    print("Exiting the program")
                    if path.exists(c.path_for_temp):
                        rmtree(c.path_for_temp)
                        print(f"-* *- Temporary directory deleted successfully -* *-")
                    exit()
            else:
                print("Invalid input. Only enter either 'y' (yes) or 'n' (no).")