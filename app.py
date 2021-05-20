from flask import Flask
from flask_restful import Resource, Api
##import twitter_tools as tt
import socket

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self, name):
        ret=socket.gethostname())
        ret_body='{"'+ret+'": name}'
print(socket.gethostname())
        return ret_body

#class Search(Resource):
#    def get(self, name):
#        person = tt.twitter(name)
#        return person

#api.add_resource(Search, '/search/<name>')
api.add_resource(Hello, '/hello/<name>')

if __name__ == '__main__':
     app.run(host='0.0.0.0',port=5001)
   # app.run(debug=True)
