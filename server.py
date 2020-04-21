import connexion
from flask_cors import CORS
from health.bdcheck import *

app = connexion.App(__name__)

app.add_api('resources/swagger.yml')
CORS(app.app,resources=r'/api/*',methods=['GET', 'POST', 'OPTIONS', 'PUT', 'DELETE'])

# Add a flask route to expose information
app.add_url_rule('/healthcheck', 'healthcheck', view_func=lambda: health.run())  
app.add_url_rule("/environment", "environment", view_func=lambda: envdump.run())


if __name__ == '__main__':
    app.run(debug=True)

