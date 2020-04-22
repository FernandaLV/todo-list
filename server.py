import connexion
from flask_cors import CORS
from health.bdcheck import health
from appmetrics import metrics
from todometrics.allmetrics import *


app = connexion.App(__name__)

app.add_api('resources/swagger.yml')
CORS(app.app,resources=r'/*',methods=['GET', 'POST', 'OPTIONS', 'PUT', 'DELETE'])

# Add a flask route to expose healthcheck information
app.add_url_rule('/healthcheck', 'healthcheck', view_func=lambda: health.run())  

# Add a flask route to expose metrics information
app.add_url_rule("/metrics/", "metrics", view_func=lambda: allMetrics(metrics))
app.add_url_rule("/metrics/create", "create", view_func=lambda: createMetrics(metrics))
app.add_url_rule("/metrics/read_all", "read_all", view_func=lambda: readAllMetrics(metrics))
app.add_url_rule("/metrics/read_one", "read_one", view_func=lambda: readOneMetrics(metrics))
app.add_url_rule("/metrics/update", "update", view_func=lambda: updateMetrics(metrics))
app.add_url_rule("/metrics/delete", "delete", view_func=lambda: deleteMetrics(metrics))


if __name__ == '__main__':
    app.run(debug=True)