from hashlib import sha1
import pickle
import os


class MoGitObj:
    def __init__(self, type, data):
        self.type = type
        self.data = data
        self.hash = ""
        self.calc_hash()

    def calc_hash(self):
        data = {"type": self.type, "data": self.data}
        byte = pickle.dumps(data)
        hasher = sha1(byte)
        self.hash = hasher.hexdigest()

    def save(self, storage_path):
        os.makedirs(
            os.path.join(storage_path, self.hash[:2], self.hash[2:4]), exist_ok=True
        )
        with open(
            os.path.join(storage_path, self.hash[:2], self.hash[2:4], self.hash), "wb"
        ) as f:
            pickle.dump(self, f)

    @staticmethod
    def load(storage_path, hash):
        path = os.path.join(storage_path, hash[:2], hash[2:4], hash)
        if os.path.exists(path):
            with open(path, "rb") as f:
                return pickle.load(f)

        return None


class Blob(MoGitObj):
    def __init__(self, content):
        super().__init__("blob", content)


class Commit(MoGitObj):
    def __init__(self, commit_data):
        super().__init__("commit", commit_data)

    def get_commit(self):
        return self.data


class MoGitStorage:
    def __init__(self, storage_path):
        self.storage_path = storage_path

    def add_object(self, obj):
        obj.save(self.storage_path)

    def get_object(self, hash):
        return MoGitObj.load(self.storage_path, hash)
