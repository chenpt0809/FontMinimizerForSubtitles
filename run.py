import os
import json
from pathlib import Path


class font:
    def __init__(self):
        self.cache = list()

    def read_cache(self, file_path):
        if not os.path.exists(file_path):
            return False
        self.cache.append(json.load(file_path))
        return True

    def get_cache(self, dir_path):
        if not os.path.exists(dir_path):
            return False
        file_list = list()
        path = Path(dir_path)
        c = 0
        for file in path.rglob('*.[TtOo][Tt][FfCc]'):
            file_list.append(file)
            c += 1
            print(f"\r获取字体文件数量：{c}", end='', flush=True)
        else:
            print(f"\r成功获取字体文件数量：{c}", flush=True)
