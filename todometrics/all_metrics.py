def all_metrics(metrics):

    metricsGetCreate  = metrics.get("create")
    metricsGetReadAll = metrics.get("read_all")
    metricsGetReadOne = metrics.get("read_one")
    metricsGetUpdate  = metrics.get("update")
    metricsGetDelete  = metrics.get("delete")
    
    allMetricsR = {
        "create": metricsGetCreate,
        "read_all": metricsGetReadAll,
        "read_one": metricsGetReadOne,
        "update": metricsGetUpdate,
        "delete": metricsGetDelete
    }

    return allMetricsR

def create_metrics(metrics):
    createMetricsR = {
        "create": metrics.get("create")
    }
    return createMetricsR

def read_all_metrics(metrics):
    readAllMetricsR = {
        "read_all": metrics.get("read_all")
    }
    return readAllMetricsR

def read_one_metrics(metrics):
    readOneMetricsR = {
        "read_one": metrics.get("read_one")
    }
    return readOneMetricsR

def update_metrics(metrics):
    updateMetricsR = {
        "update": metrics.get("update")
    }
    return updateMetricsR

def delete_metrics(metrics):
    deleteMetricsR = {
        "delete": metrics.get("delete")
    }
    return deleteMetricsR