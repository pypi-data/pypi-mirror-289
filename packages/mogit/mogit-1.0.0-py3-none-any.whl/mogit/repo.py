import os
import json
from .objs import Blob
from pathlib import Path


class StagingArea:
    def __init__(self):
        self.path = os.path.join(".mogit", "staging.json")

    @staticmethod
    def init():
        path = os.path.join(".mogit", "staging.json")

        if not os.path.exists(path):
            with open(path, "w") as f:
                json.dump([], f, indent=4)

    def add(self, filename, objs):

        with open(filename, "rb") as f:
            data = {"name": filename, "content": f.read()}
            blob = Blob(data)
        objs.add_object(blob)
        datas = json.load(open(self.path))
        datas.append({"name": filename, "hash": blob.hash})
        self.write(datas)

    def write(self, data):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    def clean(self):
        self.write([])

    def get_all(self):
        return json.load(open(self.path))


class RepoData:
    def __init__(self):
        self.path = os.path.join(".mogit", "data.json")

    @staticmethod
    def init():
        path = os.path.join(".mogit", "data.json")
        with open(path, "w") as f:
            json.dump({"Branch": "main"}, f, indent=4)

    def get(self, name):
        with open(self.path) as f:
            data = json.load(f)
            return data.get(name, None)

    def set(self, key, val):
        with open(self.path) as f:
            data = json.load(f)
            data[key] = val

        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)


class CommitLog(StagingArea):
    def __init__(self, config):
        self.config = config

    def get_path(self):
        path = os.path.join(".mogit", "commits", f"{self.config.get('Branch')}.json")
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as f:
                json.dump([], f, indent=4)
        return path

    def add(self, hashs):
        datas = json.load(open(self.get_path()))
        datas.append(hashs)
        self.write(datas)

    def write(self, data):
        with open(self.get_path(), "w") as f:
            json.dump(data, f, indent=4)

    def get_all(self):
        return json.load(open(self.get_path()))

    def get(self, n):
        return json.load(open(self.get_path()))[n]


class Tags(RepoData):
    def __init__(self):
        self.path = os.path.join(".mogit", "tags.json")

    @staticmethod
    def init():
        path = os.path.join(".mogit", "tags.json")
        with open(path, "w") as f:
            json.dump({}, f, indent=4)


class Config(RepoData):
    def __init__(self):
        self.path = os.path.join(Path.home(), ".mogitconfig")

        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump({}, f, indent=4)

    def get(self, name):
        with open(self.path) as f:
            data = json.load(f)
            return data.get(name, None)

    def set(self, key, val):
        with open(self.path) as f:
            data = json.load(f)
            data[key] = val

        with open(self.path, "w") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
