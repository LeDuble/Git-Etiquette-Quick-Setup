import os

# parent directory
# parent_dir = os.path.abspath("..") # !not in use atm might cause problems TODO: it works no need to change this variable
parent_dir = os.path.dirname(os.getcwd())

# .github folder
github_folder = os.path.join(parent_dir, ".github")

# workflows folder
workflows_folder = os.path.join(github_folder, "workflows")
## workflows files
workflows_file = os.path.join(workflows_folder, "WFprojects.yaml") # !changed github_folder to workflows_folder
workflows_org_file = os.path.join(workflows_folder, "WFprojects_organization_version.yaml") # !changed github_folder to workflows_folder

# templates
issue_template_folder = os.path.join(github_folder, "ISSUE_TEMPLATE")
## template card for pull request
## template cards for issues
frontend_issues_template_file = os.path.join(issue_template_folder, "frontend-card.yml")
backend_issues_template_file = os.path.join(issue_template_folder, "backend-card.yml")
design_issues_template_file = os.path.join(issue_template_folder, "design-card.yml")
config_issues_template_file = os.path.join(issue_template_folder, "config.yml")

# temporary folder name (created)
temp_folder = "temp_folder_ge"
temp_folder_path = os.path.join(parent_dir, temp_folder)
temp_github_path = os.path.join(temp_folder_path, ".github")
temp_workflows_path = os.path.join(temp_github_path, "workflows")
temp_issue_template_folder = os.path.join(temp_github_path, "ISSUE_TEMPLATE") # TODO: fix naming to "temp_issue_template_folder"
path_for_temp = os.path.join(parent_dir, "temp_folder_ge") # fix it later

# !fix these
## workflow file deletion from the temporary folder (when not needed)
del_workflows_file = os.path.join(temp_workflows_path, "WFprojects.yaml")
del_workflows_org_file = os.path.join(temp_workflows_path, "WFprojects_organization_version.yaml")
pull_request_template = os.path.join(temp_folder_path, "pull_request_template.md") # TODO: add file in to end of the variable name to make it more recognizable !also fix the location in the github repository

# Git Etiquette Template repository link & name
git_etiquette_repo_url = "https://github.com/LeDuble/Git-Etiquette-Template.git"
git_etiquette_repo_name = "Git-Etiquette-Template.git"

# dictionary for paths of files and folders
item_dic = {
    0: [github_folder, ".github"],
    1: [workflows_folder, "workflows"],
    2: [issue_template_folder, "ISSUE_TEMPLATE"],
    3: [workflows_file, "WFprojects.yaml"],
    4: [workflows_org_file, "WFprojects_organization_version.yaml"],
    5: [pull_request_template, "pull_request_template.md"],
    6: [frontend_issues_template_file, "frontend_card_template.yml"],
    7: [backend_issues_template_file, "backend_card_template.yml"],
    8: [design_issues_template_file, "design_card_template.yml"],
    9: [config_issues_template_file, "config_card.yml"],
}

# dictionary for folder paths
folder_dic = {
    0: [github_folder, ".github"],
    1: [workflows_folder, "workflows"],
    2: [issue_template_folder, "ISSUE_TEMPLATE"],
}

# dictionary for file paths
file_dic = {
    0: [workflows_file, "WFprojects.yaml"],
    1: [workflows_org_file, "WFprojects_organization_version.yaml"],
    2: [os.path.join(github_folder, "pull_request_template.md"), "pull_request_template.md"],
    3: [frontend_issues_template_file, "frontend_card_template.yml"],
    4: [backend_issues_template_file, "backend_card_template.yml"],
    5: [design_issues_template_file, "design_card_template.yml"],
    6: [config_issues_template_file, "config_card.yml"],
}

# dictionary for workflows files
workflows_files_dic = {
    0: [workflows_file, "WFprojects.yaml", "Single user version (token auth)", del_workflows_file], 
    1: [workflows_org_file, "WFprojects_organization_version.yaml", "Organization version (app auth)", del_workflows_org_file],
}

# dictionary for items, their sources and destination values 
# {key: [file name, source value, destination value]}
item_destinations_dic = {
    0: ["WFprojects.yaml", temp_workflows_path, workflows_folder],
    1: ["WFprojects_organization_version.yaml", temp_workflows_path, workflows_folder], 
    2: ["pull_request_template.md", temp_github_path, github_folder],
    3: ["frontend-card.yml", temp_issue_template_folder, issue_template_folder],
    4: ["backend-card.yml", temp_issue_template_folder, issue_template_folder],
    5: ["design-card.yml", temp_issue_template_folder, issue_template_folder],
    6: ["config.yml", temp_issue_template_folder, issue_template_folder],
}


item_not_added1 = [] # TODO: edit name later & # TODO: add meaningful comment

items_requested = [] # TODO: move in to another file that represents saved values/variables/lists
# print(items_requested) # !debugging

# list of files and folders that already exist
list_exist = [] # TODO: move in to another file that represents saved values/variables/lists

# list of files and folders that doesn't exist
list_not_exist = [] # TODO: move in to another file that represents saved values/variables/lists

# which operation system in use posix/nt
operation_system = "" # TODO: move in to another file that represents saved values/variables/lists

# file mode when posix system is detected
mode = 0o700 # TODO: add this in to checkos permissions when posix system is detected

folders_to_check = [] # TODO: add meaningful comment
folders_found = [] # TODO: add meaningful comment

files_found = [] # TODO: add meaningful comment
files_found_paths = [] # TODO: add meaningful comment

# folders created by the program
folders_created = [] # TODO: add meaningful comment

