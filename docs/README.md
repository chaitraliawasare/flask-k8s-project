# 🚀 Cloud-Native DevOps Platform (Flask + Kubernetes)

## 📌 Overview

This project demonstrates a **production-ready cloud-native DevOps architecture** by deploying a containerized Flask application with PostgreSQL using Docker and Kubernetes.

The system is designed with a focus on **scalability, reliability, observability, and automation**, incorporating real-world DevOps best practices such as **health checks, autoscaling, and CI/CD pipelines**.

---

## 🏗️ Architecture

Client → Nginx (Ingress / Reverse Proxy) → Flask App (Kubernetes Pods) → PostgreSQL  
                      ↓  
                  Monitoring (Prometheus → Grafana)

---

## ⚙️ Tech Stack

* 🐳 Docker – Containerization  
* ☸️ Kubernetes – Container Orchestration  
* 🌐 Nginx – Reverse Proxy / Ingress  
* 🐘 PostgreSQL – Database  
* 📊 Prometheus – Metrics Collection  
* 📈 Grafana – Visualization  
* 🐍 Flask – Backend Application  
* 🔄 GitHub Actions – CI/CD Pipeline  

---

## 🚀 Key Features

### 🔹 Application & Infrastructure
* Containerized microservices using Docker  
* Kubernetes-based deployment with rolling updates  
* Nginx-based traffic routing using Ingress  

### 🔹 Reliability & Health Management
* Implemented **Liveness and Readiness Probes**  
* Automatic container restart on failure  
* Zero-downtime deployments using rolling updates  

### 🔹 Scalability
* Configured **Horizontal Pod Autoscaler (HPA)** based on CPU utilization  
* Dynamic scaling based on load  

### 🔹 Configuration Management
* Used **ConfigMaps and Secrets** for environment configuration  
* Secure handling of database credentials  

### 🔹 Observability
* Integrated **Prometheus** for metrics scraping  
* Visualized metrics using **Grafana dashboards**  
* Exposed custom application metrics (`/metrics` endpoint)  

### 🔹 CI/CD (In Progress)
* Implemented **GitHub Actions pipeline**:
  - Build Docker image  
  - Push to DockerHub  
* Designed deployment stage (requires cloud cluster for full automation)  

---

## 🛠️ Deployment Steps

### 1. Clone the repository

```bash
git clone https://github.com/chaitraliawasare/flask-k8s-project.git
cd flask-k8s-project```

2. Build Docker image
docker build -t chaitrali20/flask-app:latest .
3. Deploy to Kubernetes
kubectl apply -f k8s/
4. Verify deployment
kubectl get pods
kubectl get services
kubectl get ingress
4. Verify deployment
kubectl get pods
kubectl get services
kubectl get ingress
5. Monitor Application
kubectl port-forward svc/prometheus 9090
kubectl port-forward svc/grafana 3000
🧪 Health Checks

/health endpoint implemented for Kubernetes probes

Liveness Probe → Restarts unhealthy containers

Readiness Probe → Controls traffic routing

📈 Autoscaling

Configured HPA using CPU metrics

Metrics Server integrated for resource monitoring

Application scales automatically under load

📸 Screenshots
Application UI
<img width="669" height="455" alt="image" src="https://github.com/user-attachments/assets/7c418904-19d9-4ca5-bf09-22ee290a5304" />
Kubernetes Pods
<img width="1293" height="1070" alt="image" src="https://github.com/user-attachments/assets/866857e9-0c6f-40bf-8c20-88ab8c365808" />
Grafana Dashboards
<!-- Add Grafana screenshots here -->
🔮 Future Enhancements

Deploy to AWS EKS using Terraform

Implement full CI/CD deployment pipeline

Add centralized logging (ELK / EFK stack)

Implement TLS (HTTPS) with Ingress

Add canary/blue-green deployments

📌 Key Learnings

Kubernetes architecture and deployment strategies

Health checks (Liveness & Readiness probes)

Autoscaling using HPA and metrics-server

Monitoring and observability using Prometheus & Grafana

CI/CD pipeline design with GitHub Actions

Debugging real-world production issues

📊 Results

Successfully deployed multi-container application on Kubernetes

Implemented self-healing and auto-scaling mechanisms

Achieved high availability using multiple replicas

Monitored system performance with real-time metrics

Built a production-like DevOps workflow

👩‍💻 Author

Chaitrali Awasare
DevOps Engineer
