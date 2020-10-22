import socketio

class SocketIO:
    def createClient(self):
        sio = socketio.Client()
        sio.connect('http://localhost:3000')
        
        return sio