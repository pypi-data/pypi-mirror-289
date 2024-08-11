from . import MoGit
from .repo import Config
import click
import os


@click.group()
def cli():
    pass


@cli.command(help="初始化仓库")
def init():
    if os.path.exists(".mogit"):
        print("已初始化")
        return
    MoGit.init()
    print("初始化完毕 ")


@cli.command(help="加入暂存区")
@click.argument("path")
def add(path):
    mogit = MoGit()
    if os.path.exists(path):
        mogit.add(path)
    else:
        print("文件或目录不存在")


@cli.command(help="创建提交")
@click.argument("msg")
def commit(msg):
    mogit = MoGit()
    mogit.commit(msg)


@cli.command(help="检出提交")
@click.argument("idx")
def checkout(idx):
    mogit = MoGit()
    mogit.checkout(idx)


@cli.command(help="创建提交")
@click.argument("tag")
@click.option("-h", "--hash", default=False)
def tag(tag, hash):
    mogit = MoGit()
    if hash:
        mogit.tag(tag, hash)
    else:
        mogit.tag(tag, mogit.config.get("LastCommit"))


@cli.command(help="列出所有提交")
def log():
    mogit = MoGit()
    mogit.log()


@cli.command(help="分支操作")
@click.argument("opcode")
@click.option("-n", "--new", is_flag=True)
def branch(opcode, new):
    mogit = MoGit()
    if new:
        mogit.create_branch(opcode)
    else:
        mogit.switch_branch(opcode)


@cli.command(help="设置")
@click.argument("key")
@click.argument("val")
def set(key, val):
    config = Config()
    config.set(key, val)


if __name__ == "__main__":
    cli()
