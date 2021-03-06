#coding:utf-8

from flask_script import Manager,Server

from main import app,db,User,Post,Comment

#把app传给Manager对象，以初始化Flask Script
manager = Manager(app)

manager.add_command("server",Server())


@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User,Post=Post,Comment=Comment)

if __name__ == "__main__":
    manager.run()