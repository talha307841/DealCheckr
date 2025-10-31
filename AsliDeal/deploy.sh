#!/usr/bin/env bash
set -euo pipefail

# deploy.sh
# Usage: ./deploy.sh <image_full>
# Copies the IMAGE_FULL into .env and brings up the compose stack.

IMAGE_FULL="$1"
ROOT_DIR="$(pwd)"
ENV_FILE="$ROOT_DIR/.env"

if [ -z "$IMAGE_FULL" ]; then
  echo "Usage: $0 <image_full>"
  exit 2
fi

echo "Deploying image: $IMAGE_FULL"

# Ensure env file exists
if [ ! -f "$ENV_FILE" ]; then
  touch "$ENV_FILE"
fi

# Save previous image for rollback
PREV_IMAGE="$(grep '^IMAGE_FULL=' "$ENV_FILE" | cut -d'=' -f2- || true)"

echo "IMAGE_FULL=$IMAGE_FULL" > "$ENV_FILE"

echo "Pulling image..."
if ! docker pull "$IMAGE_FULL"; then
  echo "Failed to pull image $IMAGE_FULL"
  # restore previous
  if [ -n "$PREV_IMAGE" ]; then
    echo "Restoring previous image: $PREV_IMAGE"
    echo "IMAGE_FULL=$PREV_IMAGE" > "$ENV_FILE"
  fi
  exit 1
fi

echo "Updating containers with docker compose..."
if docker compose pull && docker compose up -d --no-build; then
  echo "Deployment succeeded: $IMAGE_FULL"
  exit 0
else
  echo "Deployment failed, attempting rollback..."
  if [ -n "$PREV_IMAGE" ]; then
    echo "Restoring previous image: $PREV_IMAGE"
    echo "IMAGE_FULL=$PREV_IMAGE" > "$ENV_FILE"
    docker compose pull || true
    docker compose up -d --no-build || true
    echo "Rollback attempted"
  else
    echo "No previous image recorded; manual intervention required"
  fi
  exit 1
fi
