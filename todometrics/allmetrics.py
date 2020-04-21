def allMetrics(metrics):

    metricsGetCreate  = metrics.get("create")
    metricsGetReadAll = metrics.get("read_all")
    metricsGetReadOne = metrics.get("read_one")
    metricsGetUpdate  = metrics.get("update")
    metricsGetDelete  = metrics.get("delete")
    
    allMetricsR = {
        "create": metricsGetCreate,
        "read_all": metricsGetReadAll,
        "read": metricsGetReadOne,
        "update": metricsGetUpdate,
        "delete": metricsGetDelete
    }

    return allMetricsR