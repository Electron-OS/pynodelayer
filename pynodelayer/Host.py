from Core import SocketIO
import importlib

socketIO = SocketIO()
sio = socketIO.createClient()

@sio.event
def runTask(data):
  # library.class.function
  data_split = data['func'].split('.')
  module = importlib.import_module(data_split[0])
  _class = getattr(module , data_split[1])
  if len(data['args']) == 0:
    sio.emit(data['id'] , getattr(_class(), data_split[2])())
  else:
    sio.emit(data['id'] , getattr(_class(), data_split[2])(data['args']))