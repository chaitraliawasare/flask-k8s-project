# Flask Microservice Deployment on Kubernetes

## Overview

This project demonstrates how to deploy a containerized **Flask web application with a PostgreSQL database** on **Kubernetes**.
The application was originally containerized using Docker and later migrated to Kubernetes for orchestration, scalability, and service discovery.

The deployment uses **Minikube** for running a local Kubernetes cluster and exposes the application using a **NodePort Service**.

---

## Architecture

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

### Kubernetes Components Used

| Component           | Purpose                              |
| ------------------- | ------------------------------------ |
| Deployment          | Manages Flask application pods       |
| Pods                | Run containerized Flask application  |
| Service (NodePort)  | Exposes Flask app externally         |
| Service (ClusterIP) | Internal communication with database |
| Kubernetes DNS      | Service discovery between pods       |

---

## Tech Stack

* **Python Flask**
* **PostgreSQL**
* **Docker**
* **Kubernetes**
* **Minikube**
* **kubectl**

---

## Project Structure

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

## Prerequisites

Before running this project, ensure you have the following installed:

* Docker
* Kubernetes CLI (`kubectl`)
* Minikube
* Python 3.x

Verify installation:

```
kubectl version --client
minikube version
docker --version
```

---

## Start Kubernetes Cluster

Start the Minikube cluster:

```
minikube start
```

Verify the cluster:

```
kubectl get nodes
```

---

## Build Docker Image

Build the Flask application container:

```
docker build -t flask-app .
```

For Minikube local development:

```
eval $(minikube docker-env)
docker build -t flask-app .
```

---

## Deploy Application to Kubernetes

### Deploy Flask Application

```
kubectl apply -f k8s/flask-deployment.yaml
```

### Create Flask Service

```
kubectl apply -f k8s/flask-service.yaml
```

### Deploy PostgreSQL

```
kubectl apply -f k8s/postgres-deployment.yaml
```

### Create PostgreSQL Service

```
kubectl apply -f k8s/postgres-service.yaml
```

---

## Verify Deployment

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

## Access the Application

Use the following command to access the application:

```
minikube service flask-service
```

Alternatively:

```
minikube ip
```

Then open:

```
http://<minikube-ip>:<nodeport>
```

---

## Debugging Commands

Check pod logs:

```
kubectl logs <pod-name>
```

Describe services:

```
kubectl describe svc flask-service
```

Execute into a pod:

```
kubectl exec -it <pod-name> -- sh
```

Port forwarding:

```
kubectl port-forward deployment/flask-app-deployment 5001:5001
```

---

## Troubleshooting Issues Encountered

During deployment several common Kubernetes issues were encountered and resolved:

| Issue                        | Solution                                           |
| ---------------------------- | -------------------------------------------------- |
| ImagePullBackOff             | Built image locally inside Minikube environment    |
| Service not reachable        | Corrected service targetPort to match Flask port   |
| Database hostname resolution | Created Kubernetes service `database`              |
| External access issue        | Used NodePort service and Minikube service command |

---

## Future Improvements

* Implement **Persistent Volumes** for PostgreSQL
* Use **ConfigMaps** for environment configuration
* Use **Secrets** for database credentials
* Implement **Ingress Controller** instead of NodePort
* Add **Prometheus + Grafana monitoring**

---

## Learning Outcomes

Through this project the following Kubernetes concepts were implemented:

* Deployments and Pods
* Kubernetes Services
* Service discovery using DNS
* Exposing applications using NodePort
* Debugging Kubernetes networking issues
* Connecting microservices within a cluster

---

## Author

DevOps Engineer exploring Kubernetes, container orchestration, and cloud-native architectures.

