import json
import os

class json_helper():

    def jsonreader(self,json_name):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, '..', 'resources', json_name)
        with open(file_path) as data_file:
            json_data = json.load(data_file)
            return json_data