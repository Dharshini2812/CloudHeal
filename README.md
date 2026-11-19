# CloudHeal – Cloud-Native DevOps Monitoring & Auto-Recovery System

![GitHub Actions](https://github.com/Dharshini2812/CloudHeal/actions/workflows/tests.yml/badge.svg)

CloudHeal is a cloud-native DevOps monitoring and auto-recovery learning project that demonstrates application health monitoring, metrics collection, visualization, automated testing, containerization and Kubernetes-based recovery.

The project uses Prometheus to collect application metrics, Grafana to visualize monitoring data, and Kubernetes liveness probes to automatically restart an unhealthy application container.

## Key Features

- **Application Health Monitoring:** FastAPI health-check endpoint.
- **Metrics Collection:** Prometheus metrics and custom application health metrics.
- **Monitoring Dashboard:** Grafana dashboard for application monitoring.
- **Alerting:** Grafana alert rules for application health status.
- **Containerization:** Docker and Docker Compose.
- **Auto-Recovery:** Kubernetes liveness probes automatically restart unhealthy containers.
- **Automated Testing:** Pytest test cases.
- **CI/CD:** GitHub Actions automatically runs tests on push and pull requests.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API |
| Prometheus | Metrics collection |
| Grafana | Monitoring dashboard |
| Docker | Containerization |
| Docker Compose | Multi-container management |
| Kubernetes | Deployment and auto-recovery |
| Pytest | Automated testing |
| GitHub Actions | Continuous Integration |

## Project Architecture

1. FastAPI runs the CloudHeal application.
2. Prometheus collects application metrics from `/metrics`.
3. Grafana connects to Prometheus and displays monitoring dashboards.
4. Kubernetes manages the application pod.
5. Kubernetes liveness probes monitor `/health` and restart the container after repeated failures.
6. GitHub Actions runs automated tests whenever code is pushed or a pull request is created.

## Project Structure

```text
CloudHeal/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── k8s/
│   └── deployment.yaml
│
├── prometheus/
│   └── prometheus.yml
│
├── tests/
│   └── test_main.py
│
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── deployment.yaml
├── service.yaml
├── .dockerignore
├── .gitignore
└── README.md
```

## Local Setup

Create and activate a virtual environment:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Start the application:

```powershell
uvicorn main:app --reload
```

Application URLs:

- API: http://127.0.0.1:8000
- Swagger API Documentation: http://127.0.0.1:8000/docs
- Health Check: http://127.0.0.1:8000/health
- Metrics: http://127.0.0.1:8000/metrics

## Docker Monitoring Stack

Start all services:

```powershell
docker compose up --build
```

Access the services:

- CloudHeal API: http://localhost:8000
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

Grafana's initial local login is `admin / admin`. Change the password after your first login.

## Kubernetes Deployment & Auto-Recovery

CloudHeal was deployed using Docker Desktop Kubernetes.

Apply the deployment and service configurations:

```powershell
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

Check the deployment:

```powershell
kubectl get pods
kubectl get deployments
kubectl get services
```

Access CloudHeal:

http://localhost:30080

### Automatic Recovery Demonstration

Trigger a simulated application failure:

```powershell
Invoke-RestMethod -Method Post -Uri http://localhost:30080/demo/fail
```

Monitor the pod:

```powershell
kubectl get pods -w
```

Kubernetes detects repeated health-check failures through the liveness probe and automatically restarts the application container.

Verify recovery:

```powershell
Invoke-RestMethod -Uri http://localhost:30080/health
```

Expected response:

```json
{
  "status": "healthy"
}
```

**Note:** The demo failure endpoint is intended only for learning and testing. Do not expose it in production.

## Automated Testing

Run the test suite:

```powershell
python -m pytest -q
```

**Latest local test result:**
- 3 tests passed
- 0 tests failed

## GitHub Actions – Continuous Integration

GitHub Actions is configured to run automatically on:

- Push events
- Pull requests

The workflow:
1. Checks out the repository.
2. Sets up Python 3.11.
3. Installs project dependencies.
4. Runs automated tests using Pytest.

**Latest workflow execution:** Successful.

## Project Outcomes

- Implemented application health monitoring.
- Collected and visualized Prometheus metrics.
- Created Grafana monitoring dashboards and alert rules.
- Containerized the application using Docker.
- Deployed the application using Kubernetes.
- Demonstrated automatic container restart after application failure.
- Implemented automated testing and GitHub Actions CI.

## Repository

GitHub: https://github.com/Dharshini2812/CloudHeal

## Future Enhancements

- Configure SMTP for actual email alert delivery.
- Add Kubernetes resource monitoring.
- Implement advanced recovery strategies.
- Improve monitoring dashboards and alerting.
- Extend automated test coverage.

---

**CloudHeal – Monitoring, Detecting and Recovering from Application Failures.**