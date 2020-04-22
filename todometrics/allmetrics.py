def allMetrics(metrics):

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

def createMetrics(metrics):
    createMetricsR = {
        "create": metrics.get("create")
    }
    return createMetricsR

def readAllMetrics(metrics):
    readAllMetricsR = {
        "read_all": metrics.get("read_all")
    }
    return readAllMetricsR

def readOneMetrics(metrics):
    readOneMetricsR = {
        "read_one": metrics.get("read_one")
    }
    return readOneMetricsR

def updateMetrics(metrics):
    updateMetricsR = {
        "update": metrics.get("update")
    }
    return updateMetricsR

def deleteMetrics(metrics):
    deleteMetricsR = {
        "delete": metrics.get("delete")
    }
    return deleteMetricsR