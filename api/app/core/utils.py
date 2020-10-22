import os
import time
from pathlib import Path

from app.core.config import settings

import yaml


class Utils:
    def __init__(self):
        self.create_folder(settings.UPLOAD_DIR)
        self.create_folder(settings.OUTPUT_DIR)

    def create_folder(self, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)

    def time_taken(self, start_time):
        temp_time = time.time() - start_time
        hours = temp_time // 3600
        temp_time = temp_time - 3600 * hours
        minutes = temp_time // 60
        seconds = temp_time - 60 * minutes

        return f"{round(minutes)} Min {round(seconds)} sec"

    def get_upload_folder(self):
        # conf = self.get_config()
        upload_dir = os.path.join(os.getcwd(), 'app', 'data','uploads')
        # self.create_folder(upload_dir)

        return upload_dir
