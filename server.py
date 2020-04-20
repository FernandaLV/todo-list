import connexion
from flask_cors import CORS


app = connexion.App(__name__, specification_dir='resources/')

app.add_api('swagger.yml')
CORS(app.app,resources=r'/api/*',methods=['GET', 'POST', 'OPTIONS', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.run(debug=True)
