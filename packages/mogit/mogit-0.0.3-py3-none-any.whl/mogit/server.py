from flask import Flask, request
from . import MoGit
import os

app = Flask(__file__)


@app.route("/clone/<repo>")
def repo_metadata(repo):
    base_dir = app.config.get("repo_base_dir")
    repo_dir = os.path.join(base_dir, repo)

    if not os.path.exists(repo_dir):
        return {"msg": "仓库不存在"}, 404

    old_dir = os.getcwd()
    os.chdir(repo_dir)
    mogit = MoGit()
    last_commit = mogit.config.get("LastCommit")
    commits = mogit.commits.get_all()
    branchs = []
    for f in os.listdir(".mogit/commits"):
        name, ext = os.path.splitext(f)
        branchs.append(name)

    data = {
        "last": last_commit,
        "commits": commits,
        "branchs": branchs,
        "branch": mogit.config.get("Branch"),
    }
    os.chdir(old_dir)
    return data


@app.route("/clone/<repo>/list")
def clone_list(repo):
    base_dir = app.config.get("repo_base_dir")
    repo_dir = os.path.join(base_dir, repo)
    commit = request.args.get("commit", "l")
    branch = request.args.get("branch", "d")
    if not os.path.exists(repo_dir):
        return {"msg": "仓库不存在"}, 404

    old_dir = os.getcwd()
    os.chdir(repo_dir)
    mogit = MoGit()

    return "尚未实现"


if __name__ == "__main__":
    app.config["repo_base_dir"] = "."
    app.run()
