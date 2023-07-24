import os
import json


class font:
    def __init__(self):
        self.cache = list()

    def read_cache(self, file_path):
        if not os.path.exists(file_path):
            return False
        self.cache.append(json.load(file_path))
        return True


