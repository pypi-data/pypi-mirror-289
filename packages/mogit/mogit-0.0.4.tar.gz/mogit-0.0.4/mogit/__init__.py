import os
from hashlib import sha1
import time

from .objs import MoGitStorage, Commit
from .repo import StagingArea, RepoData, CommitLog, Tags, Config, Branchs
from . import ignorefile


class MoGit:
    def __init__(self):
        self.base_dir = ".mogit"
        self.objs = MoGitStorage(os.path.join(self.base_dir, "objs"))  # 存储管理器
        self.staging_area = StagingArea(self)  # 暂存区

        self.config = RepoData(self)  # 仓库配置
        self.app_config = Config()  # 用户配置

        self.commits = CommitLog(self)  # 提交管理器
        self.branchs = Branchs(self)  # 分支管理器
        self.tags = Tags(self)  # 标签管理器

        if not os.path.exists(self.base_dir):
            print("MoGit未初始化")
            exit()

        if os.path.exists(".mogitignore"):
            with open(".mogitignore") as f:
                self.matchs = ignorefile.parse(f, ".")
        else:
            self.matchs = self.fake_match

    @staticmethod
    def init():
        """
        初始化仓库
        """
        base_dir = ".mogit"
        objs = os.path.join(base_dir, "objs")  # 源文件

        os.makedirs(objs, exist_ok=True)
        RepoData.init()
        StagingArea.init()
        CommitLog.init()
        Tags.init()

    def get_hash(self, hashs):
        """
        获取tag的hash
        """
        res = self.tags.get(hashs)
        if res is None:
            return hashs
        else:
            return res

    def hash_file(self, file_path):
        """
        计算文件hash
        """
        hasher = sha1()
        with open(file_path, "rb") as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()

    def fake_match(self, path):
        return False

    def check_path(self, path):
        """
        检查
        """
        if not self.matchs(path) and ".mogit" + os.sep not in path:
            return True

        return False

    def add(self, file_path):
        """
        添加文件至暂存区
        """
        if os.path.isfile(file_path):
            self.staging_area.add(file_path)

        elif os.path.isdir(file_path):
            for path, dirs, files in os.walk(file_path):
                for file in files:
                    file_path = os.path.join(path, file)

                    if self.check_path(file_path):
                        self.staging_area.add(file_path)

    def commit(self, message):
        """
        提交文件
        """
        author = self.app_config.get("author")
        mail = self.app_config.get("mail")
        if author is None:
            print('WARNING: 未定义作者，可使用 "mogit set author <author>" 来设定')
        if author is None:
            print('WARNING: 未定义作者，可使用 "mogit set mail <mail>" 来设定')

        commit_data = {
            "timestamp": time.time(),
            "msg": message,
            "files": self.staging_area.get_all(),
            "author": author,
            "mail": mail,
        }

        self.staging_area.clean()

        comm = Commit(commit_data)
        self.objs.add_object(comm)
        self.commits.add(comm.hash)

        self.config.set("LastCommit", comm.hash)

    def checkout(self, hashs):
        """
        检出提交
        """
        obj = self.objs.get_object(self.get_hash(hashs))
        if obj is None:
            print("没有这个提交")
            exit()
        for path, dirs, files in os.walk("."):
            for file in files:
                file_path = os.path.join(path, file)

                if self.check_path(file_path):
                    os.remove(file_path)

        for i in obj.data["files"]:
            file = self.objs.get_object(i["hash"])
            with open(i["name"], "wb") as f:
                f.write(file.data["content"])
        self.config.set("LastCommit", hashs)

    def tag(self, tag, hashs):
        """
        提交文件
        """
        self.tags.set(tag, hashs)

    def log(self):
        """
        获取所有提交
        """
        for commit_hash in self.commits.get_all():
            print(f"Commit: {commit_hash}")

    def create_branch(self, name):
        self.branchs.add_branch(name)

    def switch_branch(self, name):
        self.branchs.switch(name)


if __name__ == "__main__":

    # 使用示例
    MoGit.init()
    simple_git = MoGit()
    simple_git.create_branch("")
    for i in range(4):
        simple_git.add(".")
        simple_git.commit("Initial commit")

    simple_git.tag("a", "93148e363210a8c3f8bdfac9c544d87c8cf8f6be")
