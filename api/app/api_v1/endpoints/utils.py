import os
import time
from pathlib import Path

import yaml


class Utils:
    def __init__(self):
        self.app_dir = Path(os.getcwd())

    def get_config(self):
        config = yaml.safe_load(open(os.path.join(self.app_dir, "config.yaml")))

        return config

    def get_upload_folder(self):
        conf = self.get_config()
        upload_dir = os.path.join(self.app_dir, conf["UPLOAD_DIR"])
        self.create_folder(upload_dir)

        return upload_dir

    def create_folder(self, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)

    def get_output_dir(self):
        conf = self.get_config()
        output_dir = os.path.join(self.app_dir, conf["OUTPUT_DIR"])
        self.create_folder(output_dir)

        return output_dir

    def get_models_dir(self):
        conf = self.get_config()
        models_dir = os.path.join(self.app_dir, conf["MODELS_DIR"])
        # self.create_folder(models_dir)

        return models_dir

    def time_taken(self, start_time):
        temp_time = time.time() - start_time
        hours = temp_time // 3600
        temp_time = temp_time - 3600 * hours
        minutes = temp_time // 60
        seconds = temp_time - 60 * minutes

        return f"{round(minutes)} Min {round(seconds)} sec"
