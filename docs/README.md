# 🚀 Cloud-Native DevOps Platform (Flask + Kubernetes + AWS EKS)

## 📌 Overview

This project demonstrates a **cloud-native DevOps architecture** by deploying a containerized Flask application with PostgreSQL using Docker and Kubernetes.

It was implemented in two environments:

- 🖥️ Local setup using Minikube
- ☁️ Cloud deployment using AWS EKS

The system is designed with a focus on **scalability, reliability, and real-world DevOps practices**.

---

## 🏗️ Architecture

### 🖥️ Local (Minikube)

Client → Nginx → Flask Pods → PostgreSQL
↓
Prometheus → Grafana

### ☁️ Cloud (AWS EKS)

User → AWS LoadBalancer → EKS Cluster → Flask Pods → PostgreSQL

---

## ⚙️ Tech Stack

- 🐳 Docker (Containerization)
- ☸️ Kubernetes (Orchestration)
- 🌐 Nginx (Reverse Proxy)
- 🐘 PostgreSQL (Database)
- 📊 Prometheus (Monitoring)
- 📈 Grafana (Visualization)
- 🐍 Flask (Backend Application)
- 📦 Amazon ECR (Container Registry)
- ☁️ Amazon EKS (Managed Kubernetes)

---

## 🚀 Features

- Containerized microservices using Docker
- Kubernetes-based deployment with scaling support
- Nginx reverse proxy for traffic routing
- PostgreSQL integration with Flask
- Monitoring using Prometheus and Grafana
- Cloud deployment on AWS EKS
- Real-world troubleshooting and debugging

---

## 🛠️ Local Deployment (Minikube)

### 1. Clone Repository

```bash
git clone https://github.com/chaitraliawasare/flask-k8s-project.git
cd flask-k8s-project
```

### 2. Start Minikube

```bash
minikube start
```

### 3. Build Docker Image

```bash
docker build -t flask-app .
```

### 4. Deploy to Kubernetes

```bash
kubectl apply -f k8s/
```

### 5. Verify

```bash
kubectl get pods
kubectl get services
```

---

## ☁️ Cloud Deployment (AWS EKS)

### 1. Create EKS Cluster

```bash
eksctl create cluster \
  --name flask-cluster \
  --region ap-south-1 \
  --nodes 2 \
  --node-type t3.medium \
  --managed
```

---

### 2. Push Image to ECR

```bash
aws ecr create-repository --repository-name flask-app

docker build --platform linux/amd64 -t flask-app .

docker tag flask-app:latest <account-id>.dkr.ecr.ap-south-1.amazonaws.com/flask-app:latest

docker push <account-id>.dkr.ecr.ap-south-1.amazonaws.com/flask-app:latest
```

---

### 3. Deploy to EKS

```bash
kubectl apply -f k8s/
```

---

### 4. Expose Application

```bash
kubectl expose deployment flask-app \
  --type=LoadBalancer \
  --port=80 \
  --target-port=5000
```

---

### 5. Verify Deployment

```bash
kubectl get nodes
kubectl get pods
kubectl get svc
```

---

## 📸 Screenshots

### Application UI

![App](app running.png)

### Kubernetes Pods Running

![Pods](flask-k8s-project/kubectl services.png)

### AWS Load Balancer (Console)

![LoadBalancer](flask-k8s-project/loadbalancer.png)

---

## 🐞 Real-World Issues Faced & Fixes

### ❌ CloudFormation Stack Already Exists

- Cause: Incomplete cluster deletion
- Fix: Delete nodegroup stack → then cluster stack

---

### ❌ ImagePullBackOff (ECR)

- Cause: Missing IAM permissions
- Fix: Attach policy:

```bash
aws iam attach-role-policy \
  --role-name <node-role> \
  --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly
```

---

### ❌ Architecture Mismatch (ARM vs AMD)

- Cause: Built on M1/M2 Mac
- Fix:

```bash
docker build --platform linux/amd64
```

---

### ❌ LoadBalancer DNS Not Resolving

- Cause: DNS propagation delay
- Fix: Wait 2–5 minutes

---

### ❌ VPC Deletion Failure

- Cause: Dependent resources
- Fix: Delete ENIs, subnets, and gateways manually

---

## 💡 Key Learnings

- EKS uses CloudFormation under the hood
- IAM roles are critical for service communication
- Docker image architecture must match runtime environment
- Kubernetes networking and LoadBalancer provisioning are asynchronous
- Debugging infrastructure is a key DevOps skill

---

## 🔮 Future Enhancements

- CI/CD pipeline using GitHub Actions
- Horizontal Pod Autoscaling (HPA)
- Logging with ELK stack
- Kubernetes Secrets for secure credentials
- Ingress + custom domain + HTTPS

---

## 📊 Results

- Successfully deployed multi-container application on Kubernetes
- Verified communication between Flask and PostgreSQL
- Achieved public access via AWS LoadBalancer
- Implemented monitoring and observability
- Solved real-world infrastructure issues

---

## 👩‍💻 Author

**Chaitrali Awasare**
DevOps Engineer

---
