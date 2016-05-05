from flask import Flask
from flask_restful import reqparse,Resource,Api
from odoa import ODOA

app = Flask(__name__)
ayat=ODOA()

app = Flask('WSFinal')
api = Api(app)

"""
@app.route('/')
def hello_world():
    return 'Hello World!'
"""
surah=ayat.get_random_surah()

class getIsi(Resource) :
    def get(self):
        try :
            text=surah.get('translate')
            return text
        except Exception as e:
            return e

api.add_resource(getIsi, '/getIsi')

class getAyat(Resource) :
    def get(self):
        try :
            text=surah.get('description')
            return text
        except Exception as e:
            return e

api.add_resource(getAyat, '/getAyat')


class getAsli(Resource) :
    def get(self):
        try :
            text=surah.get('ayat')
            return text
        except Exception as e:
            return e

api.add_resource(getAsli, '/getAsli')


if __name__ == '__main__':
    app.run()
