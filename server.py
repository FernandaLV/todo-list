import connexion
from flask_cors import CORS
from health.bdcheck import health
from appmetrics import metrics
from todometrics.allmetrics import allMetrics


app = connexion.App(__name__)

app.add_api('resources/swagger.yml')
CORS(app.app,resources=r'/*',methods=['GET', 'POST', 'OPTIONS', 'PUT', 'DELETE'])

# Add a flask route to expose healthcheck information
app.add_url_rule('/healthcheck', 'healthcheck', view_func=lambda: health.run())  

# Add a flask route to expose metrics information
app.add_url_rule("/metrics", "metrics", view_func=lambda: allMetrics(metrics))

if __name__ == '__main__':
    app.run(debug=True)