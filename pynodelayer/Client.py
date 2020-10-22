from Core import SocketIO

class Client:
  def __init__(self):
    self.socketIO = SocketIO()
    self.sio = self.socketIO.createClient()