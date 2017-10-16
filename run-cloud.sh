#!/bin/bash
export BUCKET_NAME=informatics-neural-multi
export JOB_NAME="make_model_train$(date +%Y%m%d_%H%M%S)"
export JOB_DIR=gs://$BUCKET_NAME/$JOB_NAME
export REGION=europe-west1

gcloud ml-engine jobs submit training $JOB_NAME \
		   --job-dir gs://$BUCKET_NAME/$JOB_NAME \
		   --runtime-version 1.0 \
		   --module-name trainer.make_models \
		   --package-path ./trainer \
		   --region $REGION \
           --scale-tier CUSTOM\
           --runtime-version "1.0" \
		   -- \
		   --train-file gs://$BUCKET_NAME/cons_feature.pickle
