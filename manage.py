from flask_script import Manager,Server
from app import create_app

app = create_app('default')

app.config['SECRET_KEY'] = 'ASG2459THWERGN0W9E8RPGN23TB24R89GNWF'


manager = Manager(app)

manager.add_command('server', Server)

if __name__ == '__main__':
    manager.run()
