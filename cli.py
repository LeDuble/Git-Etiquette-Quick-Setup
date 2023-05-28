import folder_structure
import check_os
import check_existence
import prompt_continue
import git_clone
import choose_workflow
import move_items
import info_text
import delete_itself


import constant as c
import os
import shutil
import time


def main():
    """Driver function (main)
    """
    # print(f"\nStarting {main.__name__} function")  # !debugging
    # print(f"Location -* {os.path.basename(__file__)} *-")  # !debugging

    # 1. prints information about the quick setup program
    info_text.info_print()
    promptcontinue = prompt_continue.PromptContinue()
    if promptcontinue.continue_or_not() is True:

        # 2. checks which operation system the user has
        checkos = check_os.CheckOS()
        print(checkos.find_os(), "system detected")  # !debugging

        # 3. checks if any files or folders exists in the project directory
        # prints folder and file names that are not in the project directory
        checkexistence = check_existence.CheckExistence()
        checkexistence.existence_validator()

        if promptcontinue.continue_or_not() is True:
            # print("promptcontinue returned True") # !debugging
            # print(c.list_not_exist) # !debugging

            # 4. clones the git-etiquette template repository in to a temporary folder
            gitclone = git_clone.GitClone()
            if gitclone.create_temp_folder() is True:

                # 5. create folders that are missing from the project directory
                folderstructure = folder_structure.FolderCreator(c.folders_to_check)
                folderstructure.create_folders()

                # 6. user chooses which workfile needs to be added + setup
                chooseworkflow = choose_workflow.ChooseWorkflow()
                chooseworkflow.which_workflow()
                chooseworkflow.workflow_setup()

                # 7. move missing files in to their directed locations
                moveitems = move_items.MoveItems()
                moveitems.move_files()

                # prints delete quick setup y/n
                print("""\nEverything finished successfully. 
                Would you like to delete the quick setup? 
                (This doesn't affect the files that were added with quick setup)""")

                if promptcontinue.continue_or_not() is True:
                    # prompts user whether quick setup and temporary files should be removed
                    delete_itself.delete_setup_directory()
    else:
        print(f"Temporary folder {c.temp_folder} already exists, cannot continue.")
        # print(path_checker.items_requested[1]) # !debugging
        # print("create_temp_folder returns False") # !debugging
        shutil.rmtree(c.path_for_temp) # fix it later
        print("exiting the program")
        exit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n"+"Oh! You pressed CTRL+C")
        print("Program interrupted")
        if os.path.exists(c.path_for_temp):
            print("Removing files and directories which were added with the quick-setup")
            for item in c.folders_created:
                if os.path.exists(item):
                    shutil.rmtree(item)
                    print(f"-* *- Item deleted: {item} -* *-")
            shutil.rmtree(c.path_for_temp)
            print(f"-* *- Temporary directory deleted successfully -* *-")
