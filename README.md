# CloudHeal
Cloud-native DevOps monitoring and auto-recovery learning project.

## Local setup
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn main:app --reload
```
Open http://127.0.0.1:8000 and /docs.

## Tests
```powershell
pytest -q
```

## Docker monitoring stack
```powershell
docker compose up --build
```
API: http://localhost:8000 | Prometheus: http://localhost:9090 | Grafana: http://localhost:3000

Grafana default local login is admin / admin; change it after login.

## Kubernetes
Build image with `docker build -t cloudheal:1.0 .`, ensure your Kubernetes cluster can access it, then:
```powershell
kubectl apply -f k8s/deployment.yaml
kubectl get pods -w
kubectl port-forward service/cloudheal 8000:8000
```
In another terminal, trigger the demo failure:
```powershell
Invoke-RestMethod -Method Post http://127.0.0.1:8000/demo/fail
```
Watch pod restarts with `kubectl get pods`. Kubernetes liveness probes trigger the restart after repeated failed health checks. The demo failure endpoint is for local learning only; never expose it in production.

Prometheus collects metrics and Grafana displays them; Kubernetes performs the restart.
