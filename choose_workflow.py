# keep
import constant as c
import os
import re
import yaml

class ChooseWorkflow:
    def which_workflow(self):
        # TODO: add docstring

        # # !debugging
        # print(f"\nStarting {self.which_workflow.__name__} function")
        # print(f"Location -* {os.path.basename(__file__)} *-")
        # print("which_workflow \n")

        breaker = False
        while True:

            while True:

                # prints "choose workflow"
                choose_workflow_text = "\n-*- Choose Workflow: -*-"
                print(choose_workflow_text)

                # counts the length of the workflow text and prints under line break
                dots = len(choose_workflow_text)
                dotsdots = ""
                for i in range(0, dots):
                    dotsdots += "―"
                print(f"""{dotsdots}""")

                # printout workflow file options
                for idx, value in enumerate(c.workflows_files_dic.values()):
                    print(f"""    {idx}: {value[1]} - {value[2]}""")
                item_to_add = input("Add item> ")
                item_not_added = 0

                self.item_to_add = item_to_add

                print(f"\n>>{c.workflows_files_dic[int(item_to_add)][1]}<< was selected")
                while True:
                    want_to_continue = input("\nAre you happy with your choice? Type (y/n): \n")
                    if want_to_continue in ["y", "n"]:
                        if want_to_continue == "y":
                            breaker = True
                            break
                        else:
                            break
                    else:
                        print("Invalid input. Only enter either 'y' (yes) or 'n' (no).")
                if breaker:
                    break


            # regular expression to match numbers from 0-1 and only single digit numbers
            if re.match("^[0-1]$", item_to_add):
                if int(item_to_add) == 0:
                    item_not_added += 1
                    item_removed = c.workflows_files_dic[item_not_added][1]
                    item_element_removed = c.workflows_files_dic[item_not_added][0]

                    # prints which was kept and removed
                    print(f"\n>>{item_removed}<< was removed from temporary directory")
                    print(f">>{c.workflows_files_dic[int(item_to_add)][1]}<< was added to project directory") 
                    
                    # print(f"\nlist not exist before", c.list_not_exist) # !debugging
                    removed_element = c.list_not_exist.remove(item_element_removed)
                    # print(f"\nlist not exist after", c.list_not_exist) # !debugging

                    os.remove(c.workflows_files_dic[item_not_added][3])

                else:
                    item_not_added += 0
                    item_removed = c.workflows_files_dic[item_not_added][1]
                    item_element_removed = c.workflows_files_dic[item_not_added][0]
                    
                    # prints which was kept and removed
                    print(f"\n>>{item_removed}<< was removed from temporary directory")
                    print(f">>{c.workflows_files_dic[int(item_to_add)][1]}<< was added to project directory") 

                    # print(f"\nlist not exist before", c.list_not_exist) # !debugging
                    removed_element = c.list_not_exist.remove(item_element_removed)
                    # print(f"\nlist not exist after", c.list_not_exist) # !debugging

                    os.remove(c.workflows_files_dic[item_not_added][3])
                break
            else:
                print("Invalid input. Only enter numbers either 0 or 1.")


    def workflow_setup(self):
        # TODO: add docstring

        # # !debugging
        # print(f"\nStarting {self.workflow_setup.__name__} function")
        # print(f"Location -* {os.path.basename(__file__)} *-")
        # print("workflow_setup \n")

        # open the YAML file for reading
        file_name = c.workflows_files_dic[int(self.item_to_add)][1]
        file_path = os.path.join(c.temp_workflows_path, c.workflows_files_dic[int(self.item_to_add)][1])
        with open(file_path, 'r') as yaml_file: # TODO: fix this, for some weird reason it doesnt get to parent directory. !fixed
            data = yaml.safe_load(yaml_file)
            # print(data) # !debugging

        # access env value in workflow yaml file
        env_value = data['env']

        workflow_settings_text = f"\n-*- Editing settings ({file_name}) -*-"
        print(workflow_settings_text)
        dots = len(workflow_settings_text)
        dotsdots = ""
        for i in range(0, dots):
            dotsdots += "―"
        print(f"""{dotsdots}""")

        # setting up the organization workflow yaml file
        if "organization_name" in env_value:
            
            # TODO: make this in to function
            breaker = False
            while True:
                # asks the user for the new setting
                print(f"""    Current value for organization_name: {env_value['organization_name']}""")
                new_setting = input("Enter new value> ")
                print(f"Organization_name changed to: {new_setting}")
                env_value['organization_name'] = new_setting
                while True:
                    want_to_continue = input("\nWas value typed correctly? Type (y/n): \n")
                    if want_to_continue in ["y", "n"]:
                        if want_to_continue == "y":
                            breaker = True
                            break
                        else:
                            break
                    else:
                        print("Invalid input. Only enter either 'y' (yes) or 'n' (no).")
                if breaker:
                    break

            # TODO: make this in to function
            breaker = False
            while True:
                # asks the user for the project table id number
                print(f"""    Current value for project_number: {env_value['project_number']}""")
                new_project_id_number = input("Enter new value> ")
                env_value['project_number'] = new_project_id_number
                while True:
                    want_to_continue = input("\nWas value typed correctly? Type (y/n): \n")
                    if want_to_continue in ["y", "n"]:
                        if want_to_continue == "y":
                            breaker = True
                            break
                        else:
                            break
                    else:
                        print("Invalid input. Only enter either 'y' (yes) or 'n' (no).")
                if breaker:
                    break

            # replaces the old settings with the new ones
            with open(os.path.join(c.temp_workflows_path, c.workflows_files_dic[1][1]), 'w') as yaml_file:
                yaml.dump(data, yaml_file)
        
        # setting up the normal workflow yaml file
        else:
            # TODO: make this in to function
            breaker = False
            while True:
                # asks the user for the new setting
                print(f"Current username setting: {env_value['username']}")
                new_setting = input("Enter your username: ")
                env_value['username'] = new_setting
                while True:
                    want_to_continue = input("\nWas value typed correctly? Type (y/n): \n")
                    if want_to_continue in ["y", "n"]:
                        if want_to_continue == "y":
                            breaker = True
                            break
                        else:
                            break
                    else:
                        print("Invalid input. Only enter either 'y' (yes) or 'n' (no).")
                if breaker:
                    break

            # TODO: make this in to function
            breaker = False
            while True:
                # asks the user for the project table id number
                print(f"Current project_number setting: {env_value['project_number']}")
                new_project_id_number = input("Enter projects id number: ")
                env_value['project_number'] = new_project_id_number
                while True:
                    want_to_continue = input("\nWas value typed correctly? Type (y/n): \n")
                    if want_to_continue in ["y", "n"]:
                        if want_to_continue == "y":
                            breaker = True
                            break
                        else:
                            break
                    else:
                        print("Invalid input. Only enter either 'y' (yes) or 'n' (no).")
                if breaker:
                    break
            
            # replaces the old settings with the new ones
            with open(os.path.join(c.temp_workflows_path, c.workflows_files_dic[1][1]), 'w') as yaml_file:
                yaml.dump(data, yaml_file)
    