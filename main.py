
from fastapi import FastAPI, Response
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Gauge

app = FastAPI(title="CloudHeal", version="1.0.0")

# Application health status
healthy = True

# Custom Prometheus health metric
cloudheal_health = Gauge(
    "cloudheal_health_status",
    "CloudHeal application health status (1=Healthy, 0=Unhealthy)"
)

# Initial health status
cloudheal_health.set(1)

# Enable Prometheus instrumentation
Instrumentator().instrument(app).expose(
    app,
    endpoint="/metrics"
)


@app.get("/")
def home():
    return {
        "project": "CloudHeal",
        "message": "Cloud-native monitoring and auto-recovery"
    }


@app.get("/health")
def health():
    if not healthy:
        return Response(
            content='{"status":"unhealthy"}',
            status_code=503,
            media_type="application/json"
        )

    return {"status": "healthy"}


@app.post("/demo/fail")
def simulate_failure():
    global healthy

    healthy = False
    cloudheal_health.set(0)

    return {"message": "Demo failure enabled"}


@app.post("/demo/recover")
def restore_health():
    global healthy

    healthy = True
    cloudheal_health.set(1)

    return {"message": "Application is healthy again"}
