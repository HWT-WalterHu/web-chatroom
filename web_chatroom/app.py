from web_chatroom import create_app,db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from flask_socketio import SocketIO
import sys

import eventlet
app = create_app()

socketio = SocketIO(app, async_mode='eventlet')
from web_chatroom.request_hook import *

manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

from web_chatroom.socketioutils import *



if __name__ == '__main__':
    # manager.run()
    if sys.argv[1] == 'server':
        print('please visit 82.156.8.254:8080/login')
        socketio.run(app, host='10.0.24.5', port=8080)
    else:
        socketio.run(app,host='0.0.0.0', port=5000)


