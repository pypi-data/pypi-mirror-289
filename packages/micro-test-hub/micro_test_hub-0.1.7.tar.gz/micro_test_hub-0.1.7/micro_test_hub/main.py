import argparse
import json
from subprocess import Popen, PIPE, STDOUT

from platforms.docker_compose.DockerComposePlatform import DCPlatform
from services.Service import Service
from test_suites.MicroTestSuite import MicroTestSuite


def load_service_config(service_name):
    with open(f'data/services/{service_name}.json') as f:
        service_config = json.load(f)
    # Save the updated configuration back to the file if necessary
    # with open(f'data/services/{service_name}.json', 'w') as f:
    #     json.dump(service_config, f, indent=4)
    return service_config


def update_specific_field(d, keys, value):
    """
    Update a specific field in a nested dictionary without replacing entire sub-dictionaries.
    
    :param d: The dictionary to update.
    :param keys: A list of keys that leads to the specific field to update.
    :param value: The new value to set for the specified field.
    """
    current = d
    for key in keys[:-1]:  # Navigate to the sub-dictionary containing the target field
        current = current.setdefault(key, {})
    current[keys[-1]] = value  # Update the target field


def extract_key_value_pairs(d, current_path=None):
    """
    Recursively extract all key paths and their corresponding values from a nested dictionary.

    :param d: The dictionary to traverse.
    :param current_path: The current path of keys leading to a specific value.
    :return: Yields tuples of (path, value) where path is a list of keys leading to the value.
    """
    if current_path is None:
        current_path = []
    for key, value in d.items():
        # Update the path with the current key
        new_path = current_path + [key]
        if isinstance(value, dict):
            # If the value is a dictionary, continue the recursion
            yield from extract_key_value_pairs(value, new_path)
        else:
            # If the value is not a dictionary, yield the path and value
            yield (new_path, value)


def configure_services_from_config(config_path):
    with open(config_path) as f:
        config = json.load(f)
    services = []
    for service_name, config_updates in config.items():
        service_config = load_service_config(service_name)
        for path, value in extract_key_value_pairs(config_updates):
            update_specific_field(service_config, path, value)
            print(f"Path: {path}, Value: {value}")
        services.append(Service(**service_config))
    return services


def get_identity_token():
    try:
        p = Popen("gcloud auth print-identity-token", shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        auth_token = p.stdout.read().decode("utf-8").strip("\n")
        return auth_token
    except Exception as e:
        print(f"Error while getting identity token: {str(e)}")
        return None


def update_config_with_identity_token(file_path, identity_token):
    # Step 1: Read the JSON file and create a Python dict
    with open(file_path, 'r') as file:
        config = json.load(file)

    # Step 2: Assuming get_identity_token is a function that returns the new identity token
    # it = get_identity_token() # Uncomment and define get_identity_token() as needed

    # Step 3: Update the "web_gateway" -> "environment" -> "X_PA_GCP_JWT" with the new identity token
    config["web_gateway"]["environment"]["X_PA_GCP_JWT"] = identity_token

    # Write the updated configuration back to the file
    with open(file_path, 'w') as file:
        json.dump(config, file, indent=4)


# Example usage
# update_config_with_identity_token('path/to/config.json', 'new_identity_token_here')

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Run tests based on a JSON configuration.')
    parser.add_argument('-f', '--file', required=False, default='data/config.json', help='Path to the JSON file with service configurations.')
    parser.add_argument('-t', '--test-path', required=False, default='data/tests', help='Path to the directory containing test definitions.')

    args = parser.parse_args()
    identity_token = get_identity_token()
    update_config_with_identity_token(args.file, identity_token)
    # Load the services by reading the data from the JSON file specified in command line
    services = configure_services_from_config(args.file)

    dc_platform = DCPlatform(yaml_input=None)

    test_suite = MicroTestSuite(id="1", name="Test Suite 1", services=services, platform=dc_platform, tests_path=args.test_path)
    test_suite.run()
    results = test_suite.test_results()
    test_suite.stop()
    if results:
        print("Test results: SUCCESS")
    else:
        print("Test results: FAILURE")


if __name__ == "__main__":
    main()
