#!/bin/bash

# This script handles deployment to the production environment for the AsliDeal project.

# Exit immediately if a command exits with a non-zero status
set -e

# Define variables
DOCKER_COMPOSE_FILE="../infra/docker-compose.yml"
K8S_DEPLOYMENT_FILE="../infra/k8s/deployment.yaml"
K8S_SERVICE_FILE="../infra/k8s/service.yaml"

# Function to deploy using Docker Compose
deploy_docker() {
    echo "Deploying using Docker Compose..."
    cd ../infra
    docker-compose up -d --build
    echo "Docker Compose deployment completed."
}

# Function to deploy using Kubernetes
deploy_k8s() {
    echo "Deploying to Kubernetes..."
    kubectl apply -f $K8S_DEPLOYMENT_FILE
    kubectl apply -f $K8S_SERVICE_FILE
    echo "Kubernetes deployment completed."
}

# Check for deployment method
if [ "$1" == "docker" ]; then
    deploy_docker
elif [ "$1" == "k8s" ]; then
    deploy_k8s
else
    echo "Usage: $0 {docker|k8s}"
    exit 1
fi