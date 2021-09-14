import json
import os

# This class reads in the JSON config file with all the projects important directories.
class PathConfig:

    # Class variable for config file location.
    if os.name == 'nt':
        config_file = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__))),
                                   "config/local_project_dirs.json")
    else:
        config_file = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__))), "config/project_dirs.json")
    print(config_file)

    # Constructor method calls the JSON loader.
    def __init__(self):
        print('Loading config')
        with open(self.config_file) as json_config_file:
            self.config = json.load(json_config_file)

    def __getattr__(self, name):
        try:
            return self.config[name]
        except KeyError:
            print("Key given is not in the configuration file.")

path_config = PathConfig()