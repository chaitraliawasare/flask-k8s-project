# 🚀 Cloud-Native DevOps Platform (Flask + Kubernetes)

## 📌 Overview

This project demonstrates a **cloud-native DevOps architecture** by deploying a containerized Flask application with PostgreSQL using Docker and Kubernetes.

The system is designed with a focus on **scalability, reliability, and observability**, following modern DevOps practices.

---

## 🏗️ Architecture

Client → Nginx (Reverse Proxy) → Flask App (Pods) → PostgreSQL  
                                  ↓  
                        Prometheus → Grafana
---

## ⚙️ Tech Stack

* 🐳 Docker (Containerization)
* ☸️ Kubernetes (Container Orchestration)
* 🌐 Nginx (Reverse Proxy)
* 🐘 PostgreSQL (Database)
* 📊 Prometheus (Monitoring)
* 📈 Grafana (Visualization)
* 🐍 Flask (Backend Application)

---

## 🚀 Features

* Containerized microservices using Docker
* Kubernetes-based deployment with scaling support
* Nginx reverse proxy for traffic routing
* PostgreSQL integration with Flask
* Monitoring using Prometheus and Grafana
* Modular and production-like architecture

---

## 🛠️ Deployment Steps

### 1. Clone the repository

```bash
git clone https://github.com/chaitraliawasare/flask-k8s-project.git
cd flask-k8s-project
```

### 2. Build Docker images

```bash
docker build -t flask-app .
```

### 3. Deploy to Kubernetes

```bash
kubectl apply -f k8s/
```

### 4. Verify deployment

```bash
kubectl get pods
kubectl get services
```

---

## 📸 Screenshots (To be added)

* Application UI
<img width="669" height="455" alt="image" src="https://github.com/user-attachments/assets/7c418904-19d9-4ca5-bf09-22ee290a5304" />

* Kubernetes pods running
  <img width="1293" height="1070" alt="image" src="https://github.com/user-attachments/assets/866857e9-0c6f-40bf-8c20-88ab8c365808" />

* Grafana dashboards
* Monitoring metrics

---

## 🔮 Future Enhancements

* Add CI/CD pipeline using GitHub Actions
* Implement auto-scaling (HPA)
* Add logging with ELK stack
* Improve security with DevSecOps practices

---

## 📌 Key Learnings

* Kubernetes deployments and service networking
* Container orchestration and scaling concepts
* Monitoring and observability setup
* Real-world DevOps workflow and architecture

---

## 👩‍💻 Author

**Chaitrali Awasare**
DevOps Engineer

---
