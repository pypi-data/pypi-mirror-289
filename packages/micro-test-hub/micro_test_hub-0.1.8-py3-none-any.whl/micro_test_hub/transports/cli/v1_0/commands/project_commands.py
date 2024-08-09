import os
from typing import Dict, List
import click
import yaml
import json

from micro_test_hub.test_suites.MicroTestProject import MicroTestProject

MICROHUB_FILE_EXTENSION = '.microhub'
ACTIVE_PROJECT_FILE = '.mhap'
valid_service_types = ['GCP', 'DOCKER', 'FUNCTION', 'DB']
valid_gcp_services = ['PUBSUB', 'FIRESTORE', 'STORAGE']
valid_db_names = ['POSTGRESS']
valid_platform_types = ['DOCKER-COMPOSE', 'GCP']
valid_code_languages = ['NODEJS', 'PYTHON']

def is_valid_env_file(file_path: str) -> bool:
    """
    Checks if the given file is a valid environment file.

    Args:
        file_path (str): The path to the environment file.

    Returns:
        bool: True if the file is valid, False otherwise.
    """
    if not os.path.isfile(file_path):
        click.echo('The specified file does not exist.')
        return False

    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() and not line.startswith('#'):
                    if '=' not in line:
                        click.echo('The specified file is not a valid environment file.')
                        return False
        return True
    except Exception as e:
        click.echo(f'An error occurred while reading the file: {e}')
        return False

def load_env_file_to_dict(file_path: str) -> dict:
    """
    Loads the content of the environment file into a dictionary.

    Args:
        file_path (str): The path to the environment file.

    Returns:
        dict: A dictionary containing the key-value pairs from the environment file.
    """
    env_dict = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    env_dict[key] = value
    except Exception as e:
        click.echo(f'An error occurred while reading the file: {e}')
    return env_dict

def prompt_for_env_vars() -> dict:
    """
    Prompts the user to input environment variables manually.

    Returns:
        dict: A dictionary containing the key-value pairs entered by the user.
    """
    env_vars = {}
    while True:
        key = click.prompt('Please enter the environment variable name (or leave blank to finish)', default='', show_default=False)
        if key == '':
            break
        value = click.prompt(f'Please enter the value for {key}')
        env_vars[key] = value
    return env_vars

def create_env_vars() -> dict:
    """
    Creates environment variables either from a file or by getting the variable name and value from the input.

    Returns:
        dict: A dictionary containing the environment variables.
    """
    while True:
        env_file = click.prompt('Please enter the path of env file (or leave blank to enter variables manually)', default='', show_default=True)
        if env_file == '':
            return prompt_for_env_vars()
        if is_valid_env_file(env_file):
            return load_env_file_to_dict(env_file)

def prompt_for_selection(prompt_message: str, options: List, no_selection: bool=True) -> str|None:
    """
    Prompts the user to select an option from a list of options.

    Args:
        prompt_message (str): The message to display to the user.
        options (list): The list of options to choose from.
        no_selection (bool): Whether to include an option for no selection.

    Returns:
        The selected option, or None if the selection is invalid.
    """
    
    while True:
        # Display the list of options with indices
        click.echo(prompt_message)
        for i, option in enumerate(options):
            click.echo(f'{i}: {option}')
        if no_selection:    
            click.echo(f'{len(options)}: No Selection')
        # Prompt the user to enter the index of the desired option
        option_index = click.prompt('Enter the number corresponding to your choice', type=int)

        # Validate the user's input and return the corresponding option
        if 0 <= option_index < len(options):
            return options[option_index]
        elif no_selection:
            return None
        else:
            click.echo('Invalid selection. Select a valid option.')


def folder_exists(folder: str) -> bool:
    # check if the folder path exists
    if not os.path.isdir(folder):
        return False
    return True
    
    
def set_project_name(name: str) -> str:
    # doc string comments
    """
    Replaces spaces in the project name with underscores.
    
    Args:
        name (str): The project name.
        
    Returns:
        str: The project name with spaces replaced by underscores.
    """
    # replace the spaces with underscores
    name = name.replace(' ', '_')
    return name

def read_active_project() -> str:
    active_project = None
    if os.path.isfile(ACTIVE_PROJECT_FILE):
        with open(ACTIVE_PROJECT_FILE, 'r') as file:
            active_project = file.read().strip()
    return active_project

def add_services() -> List[Dict]|None:
    """
    Prompts the user to add services to the project configuration.
    
    Returns:
        List[Dict]: A list of dictionaries containing the service configurations.
    """
    add_service = True
    services = []
    while add_service:
        service = {}
        service['name'] = click.prompt('Please enter the service name')

        # Use the generic function to prompt for service type
        service['type'] = prompt_for_selection('Please select the project type:', valid_service_types)
        service['downstream'] = click.confirm('Is it a service that your test could interact with?')
       
        if service['type'] == 'DOCKER':
            service['image_uri'] = click.prompt('Please enter the path of the image')
            service['container_port'] = click.prompt('Please enter the container port', type=int) 
            service['host_port'] = click.prompt('Please enter the host port', type=int)
            service['volumes'] = add_service_volumes()
            service['container_command'] = click.prompt('Please enter the container_command', default='', show_default=True)
            service['container_command_args'] = click.prompt('Please enter the container_command_args', default='', show_default=True)
            service['env_vars'] = create_env_vars()
        elif service['type'] == 'GCP':
            # Use the generic function to prompt for service type
            service['service_type'] = prompt_for_selection('Please select the gcp service name:', valid_gcp_services)
            if service['service_type'] == 'GCS':
                service['buckets'] = []
                add_bucket = True
                while add_bucket:
                    bucket = {}
                    bucket['name'] = click.prompt('Please enter the bucket name')
                    bucket['location'] = click.prompt('Please enter the bucket location', default='', show_default=True)
                    service['buckets'].append(bucket)
                    add_bucket = click.confirm('Do you want to add another bucket?')
            elif service['service_type'] == 'PUBSUB':
                service['topics'] = []
                add_topic = True
                while add_topic:
                    topic = {}
                    topic['name'] = click.prompt('Please enter the topic name')
                    topic['subscriptions'] = []
                    add_subscription = True
                    while add_subscription:
                        subscription = {}
                        subscription['name'] = click.prompt('Please enter the subscription name')
                        subscription['push_endpoint'] = click.prompt('Please enter the push end point')
                        topic['subscriptions'].append(subscription)
                        add_subscription = click.confirm('Do you want to add another subscription?')
                    service['topics'].append(topic)
                    add_topic = click.confirm('Do you want to add another topic?')        
        elif service['type'] == 'FUNCTION':
            service['code_repo'] = click.prompt('Please enter the repo of the function')    
            service['code_branch'] = click.prompt('Please enter the branch name of the repo')    
            service['code_folder'] = click.prompt('Please enter the folder name of the code', default='', show_default=True)
            service['lang_type'] = prompt_for_selection('Please select the function code language:', valid_code_languages,
                                                        no_selection=False)
            service['env_vars'] = create_env_vars()
        elif service['type'] == 'DB':
            # Use the generic function to prompt for service type
            service['db_type'] = prompt_for_selection('Please select the DB name:', valid_db_names)
            service['sql_init_file'] = click.prompt('Please enter the path of the sql init file') 
               
        services.append(service)
        add_service = click.confirm('Do you want to add another service?')
    return services    

def add_service_volumes() -> List[Dict]:
    """
    Prompts the user to add volumes to the service configuration.
    
    Args:
        service (Dict): A dictionary containing the service configuration.
        
    Returns:
        Dict: A dictionary containing the service configuration with volumes added.
    """
    add_volume = True
    volumes = []
    while add_volume:
        volume = {}
        volume['container'] = click.prompt('Please enter the container volume')
        volume['host'] = click.prompt('Please enter the host volume')
        volumes.append(volume)
        add_volume = click.confirm('Do you want to add another volume?')
    return volumes

def add_services_dependencies(services: List[Dict]) -> List[Dict]:
    """
    Prompts the user to add dependencies between services.
    
    Args:
        services (List[Dict]): A list of dictionaries containing the service configurations.
        
    Returns:
        List[Dict]: A list of dictionaries containing the service configurations with dependencies added.
    """
    all_services = [service['name'] for service in services]
    for service in services:
        # only add dependencies for DOCKER and FUNCTION services
        if service['type'] not in  ['DOCKER', 'FUNCTION']:
            continue
        dependencies = []
        all_but_current = [s for s in all_services if s != service['name']]
        add_service_dependency = True
        while add_service_dependency:
            dependency = prompt_for_selection(f"Adding service dependencies for {service['name']}", all_but_current)
            if dependency:
                dependencies.append(dependency)
                add_service_dependency = click.confirm('Do you want to add another dependency?')
            else:
                add_service_dependency = False    
        if 'dependencies' not in service:
            service['dependencies'] = dependencies
        else:
            service['dependencies'].extend(dependencies)
    return services

@click.command()
def create_project():
    """
    Creates a new project configuration file.
    """
    
    project = {}
    
    # Ask for project name
    project['name'] = set_project_name(click.prompt('Please enter the project name'))
    project['tests_path'] = click.prompt('Please enter the path of the test folder')

    while not folder_exists(project['tests_path']):
        project['tests_path'] = click.prompt('The specified folder does not exist. Please enter a valid path')
        
    project['platform'] = prompt_for_selection('Please select the project platform:', 
                                                   valid_platform_types, 
                                                   no_selection=False)
    project['services'] = add_services()
    project['services'] = add_services_dependencies(project['services'])
    
    # Convert the project dictionary to a YAML string
    project_yaml = yaml.dump(project, default_flow_style=False)

    # Save the YAML string to a file
    with open(f"{project['name']}{MICROHUB_FILE_EXTENSION}", 'w') as file:
        file.write(project_yaml)

    click.echo(f"Project {project['name']} created successfully!")

@click.command()
@click.option('--name', required=True, help='project name')
def update_project(name):
    """
    Update the given project.
    
    Args:
    
    name (str): The name of the project to set as active.
    """
    # search for a yaml file with the project name
    project_file = f'{name}{MICROHUB_FILE_EXTENSION}'
    if not os.path.isfile(project_file):
        click.echo(f'{name} PROJECT DOES NOT EXIST')
        return
    with open(project_file, 'r+') as file:
        project = yaml.safe_load(file)
        click.echo(json.dumps(project, indent=4))
        updated_services = add_services()
        project['services'].extend(updated_services)
        project['services'] = add_services_dependencies(project['services'])
        project_yaml = yaml.dump(project, default_flow_style=False)
        file.seek(0)
        file.write(project_yaml)
        file.truncate()
        click.echo(f"Project {project['name']} updated successfully!")
        
@click.command()
@click.option('--name', required=True, help='project name')
def set_active_project(name):
    """
    Sets the active project.
    
    Args:
    
    name (str): The name of the project to set as active.
    """
    
    # search for a yaml file with the project name
    if not os.path.isfile(f'{name}{MICROHUB_FILE_EXTENSION}'):
        click.echo(f'{name} PROJECT DOES NOT EXIST')
        return
	# Write the active project name to the .mhap file
    with open(ACTIVE_PROJECT_FILE, 'w') as file:
        file.write(name)
    click.echo(f'Active project set to {name}')
    
@click.command()
def list_projects():
    
    """
    Lists all the projects.
    """
    
    project_files = [f for f in os.listdir('.') if f.endswith(MICROHUB_FILE_EXTENSION)]
    active_project = read_active_project()
    for project_file in project_files:
        with open(project_file, 'r') as file:
            project = yaml.safe_load(file)
            if active_project == project['name']:
                click.echo(f"{project['name']} (Active)")
            else:
                click.echo(project['name'])    
            
@click.command()
@click.option('--name', required=True, help='project name')
def delete_project(name):
    # delete the yaml file with name the project name
    if not os.path.isfile(f'{name}{MICROHUB_FILE_EXTENSION}'):
        click.echo(f'{name} PROJECT DOES NOT EXIST')
        return
    os.remove(f'{name}{MICROHUB_FILE_EXTENSION}')
    # if the project is the active project, remove the active project file
    active_project = read_active_project()
    if active_project == name:
        os.remove(ACTIVE_PROJECT_FILE)
    click.echo(f'{name} PROJECT DELETED SUCCESSFULLY')
    

@click.command()
@click.option('--project-name', required=False, help='project name')
@click.option('--mode', type=click.Choice(['attached', 'detached']), default='detached', required=False, help='Mode of operation')
def run_test(project_name=None, mode='detached'):
    
    """
    Runs the tests for the specified project.
    
    Args:
    project_name (str): The name of the project to run the tests for.
    """
    
    if not project_name:
        project_name = read_active_project()
        if not project_name:
            click.echo('No active project set. Please specify a project name.')
            return
    project_file = f'{project_name}{MICROHUB_FILE_EXTENSION}'
    if not os.path.isfile(project_file):
        click.echo(f'{project_name} project does not exist.')
        return
    with open(project_file, 'r') as file:
        project = yaml.safe_load(file)
        #click.echo(json.dumps(project, indent=4))
        # Run the tests
        micro_test_project = MicroTestProject(**project)
        results = micro_test_project.run_test(mode)
        click.echo(f'results for project {project_name} is {results}')
        
        