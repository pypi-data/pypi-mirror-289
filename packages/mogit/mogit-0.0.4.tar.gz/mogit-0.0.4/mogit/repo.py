import os
import json
from .objs import Blob
from pathlib import Path


class StagingArea:
    def __init__(self, mogit):
        self.path = os.path.join(".mogit", "staging.json")
        self.mogit = mogit

    @staticmethod
    def init():
        path = os.path.join(".mogit", "staging.json")

        if not os.path.exists(path):
            with open(path, "w") as f:
                json.dump([], f, indent=4)

    def add(self, filename):

        with open(filename, "rb") as f:
            data = {"name": filename, "content": f.read()}
            blob = Blob(data)
        self.mogit.objs.add_object(blob)
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
    def __init__(self, mogit):
        self.mogit = mogit
        self.path = os.path.join(".mogit", "data.json")

    @staticmethod
    def init():
        path = os.path.join(".mogit", "data.json")
        with open(path, "w") as f:
            json.dump({"branch": "main"}, f, indent=4)

    def get_all(self):
        with open(self.path) as f:
            data = json.load(f)
        return data

    def write(self, data):
        with open(self.path, "w") as f:
            f.write(json.dump(data, f))

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


class Branchs:
    def __init__(self, mogit):
        self.mogit = mogit

    def add_branch(self, name):
        data = self.mogit.config.get_all()
        data["branchs"] = data.get("branchs", [])
        data["branchs"].append(name)
        data["branch"] = name
        self.mogit.config.write(data)

        all_commit = self.mogit.commits.get_all()
        self.mogit.commits.write(all_commit)

    def get_all(self):
        data = self.mogit.config.get_all()
        data["branchs"] = data.get("branchs", [])
        return data["branchs"]

    def del_branch(self, name):

        if self.mogit.config.get("branch") == name:
            print("无法删除当前分支")
            exit()

        data = self.mogit.config.get_all()
        data["branchs"] = data.get("branchs", [])
        if name in data["branchs"]:
            data["branchs"].pop(name)
        else:
            print("分支不存在")
            exit()
        self.mogit.config.write(data)
        path = os.path.join(".mogit", "commits", f"{name}.json")
        os.remove(path)

    def switch(self, name):
        # 切换分支
        path = os.path.join(".mogit", "commits", f"{name}.json")

        if os.path.exists(path):
            self.config.set("branch", name)
        else:
            print("分支不存在")

        last_commit = self.mogit.commits.get(-1)
        self.mogit.config.set("LastCommit", last_commit)
        if last_commit:
            self.mogit.checkout(last_commit)


class CommitLog(StagingArea):
    def __init__(self, mogit):
        self.mogit = mogit

    def get_path(self, branch=None):
        if branch == None:
            branch = self.mogit.config.get("branch")
        path = os.path.join(".mogit", "commits", f"{branch}.json")
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

    def get_all(self, branch=None):
        return json.load(open(self.get_path(branch)))

    def get(self, n, branch=None):
        return json.load(open(self.get_path(branch)))[n]

    def get_last_commit(self, branch=None):
        return self.get(-1, branch)


class Tags(RepoData):
    def __init__(self, mogit):
        self.mogit = mogit
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
