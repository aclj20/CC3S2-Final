#!/usr/bin/env bash
set -euo pipefail

minikube start --driver=docker
# para que los comandos de docker funcionen dentro de minikube
eval $(minikube docker-env)

# construye la imagen docjer dentro de minikube
docker build -t proyecto-final:latest .

kubectl apply -f kubernetes/

kubectl set image deployment/proyecto-final-deployment proyecto-final=proyecto-final:latest

# regresa en el historial de deployment
kubect rollout history deployment
kubectl rollout undo deployment

# pods del kubernetes
kubectl get pods


