#!/bin/bash

MODEL_NAME=mnistddpserving
API_TYPE=GRPC
SERVICE_TYPE=MODEL
PERSISTENCE=0

seldon-core-microservice $MODEL_NAME $API_TYPE --service-type $SERVICE_TYPE --persistence $PERSISTENCE