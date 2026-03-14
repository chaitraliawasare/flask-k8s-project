# 🚀 Flask Microservice Deployment on Kubernetes

## 📌 Overview

This project demonstrates how to deploy a **containerized Flask application with a PostgreSQL database** on **Kubernetes**.

The application was first containerized using Docker and then deployed to a Kubernetes cluster using **Minikube**. The project demonstrates service discovery, container orchestration, and external service exposure using Kubernetes Services.

---

## 🏗 Architecture

```
User
  ↓
NodePort Service (flask-service)
  ↓
Flask Deployment (3 Pods)
  ↓
Database Service (database)
  ↓
PostgreSQL Pod
```

---

## ⚙️ Tech Stack

* Python Flask
* PostgreSQL
* Docker
* Kubernetes
* Minikube
* kubectl

---

## 📦 Docker Image

Docker image available on Docker Hub.

Pull the image:

```
docker pull <dockerhub-username>/flask-app:latest
```

Example:

```
docker pull chaitrali/flask-app:latest
```

Run locally:

```
docker run -p 5001:5001 chaitrali/flask-app:latest
```

Application will be available at:

```
http://localhost:5001
```

---

## 📂 Project Structure

```
flask-kubernetes-project
│
├── k8s
│   ├── flask-deployment.yaml
│   ├── flask-service.yaml
│   ├── postgres-deployment.yaml
│   └── postgres-service.yaml
│
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🚀 Deploy on Kubernetes

### Start Kubernetes Cluster

```
minikube start
```

Verify cluster:

```
kubectl get nodes
```

---

### Deploy Flask Application

```
kubectl apply -f k8s/flask-deployment.yaml
```

---

### Create Flask Service

```
kubectl apply -f k8s/flask-service.yaml
```

---

### Deploy PostgreSQL

```
kubectl apply -f k8s/postgres-deployment.yaml
```

---

### Create PostgreSQL Service

```
kubectl apply -f k8s/postgres-service.yaml
```

---

## 🔍 Verify Deployment

Check running pods:

```
kubectl get pods
```

Check services:

```
kubectl get svc
```

Check deployments:

```
kubectl get deployments
```

---

## 🌐 Access the Application

Run:

```
minikube service flask-service
```

Or manually:

```
minikube ip
```

Then open:

```
http://<minikube-ip>:<nodeport>
```

---

## 🛠 Debugging Commands

View logs:

```
kubectl logs <pod-name>
```

Describe service:

```
kubectl describe svc flask-service
```

Execute inside container:

```
kubectl exec -it <pod-name> -- sh
```

Port forward:

```
kubectl port-forward deployment/flask-app-deployment 5001:5001
```

---

## ⚠️ Troubleshooting

Common issues solved during this project:

| Issue                       | Solution                                       |
| --------------------------- | ---------------------------------------------- |
| ImagePullBackOff            | Built image inside Minikube Docker environment |
| Service not reachable       | Fixed service targetPort                       |
| Database hostname not found | Created Kubernetes service `database`          |
| External access issue       | Used NodePort + Minikube service command       |

---

## 📚 Key Kubernetes Concepts Used

* Deployments
* Pods
* Services (ClusterIP & NodePort)
* Service Discovery using DNS
* Container Networking
* Debugging with kubectl

---

## 🚧 Future Improvements

* Persistent Volumes for PostgreSQL
* ConfigMaps for environment variables
* Secrets for database credentials
* Ingress controller for HTTP routing
* Monitoring using Prometheus and Grafana

---

## 👩‍💻 Author

DevOps Engineer exploring Kubernetes, container orchestration, and cloud-native architectures.
