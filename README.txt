This directory contains files for creating a job for google's cloud based machine learning platforms.

Important files:


/run-cloud.sh	script to train model on cloudml
/setup.py		sets up python once code is on the cloud, so we can use keras
/raw_data/ 		delimited files with training data

/trainer/					python package that gets ran on the cloud
		/cloudml-gpu.yaml	yaml describing how model should work
        /__init__.py  		causes this directory to become a python package

/local/						files to be ran locally to create models and digest data into appropriate numpy arrays then pickle
      /make_models.py		creates models for training on first level data
      /combine_models.py 	combines models so they can be trained on second level data 
      /data_to_array.py		converts data to pickled dic of filename -> array


Commands to run:

export BUCKET_NAME=informatics-neural-network-data
export JOB_NAME="make_models_train$(date +%Y%m%d_%H%M%S)"
export JOB_DIR=gs://$BUCKET_NAME/$JOB_NAME
export REGION=us-west1-b

gcloud ml-engine jobs submit training $JOB_NAME \ 
--module-name trainer.make_models\ 
--job-dir gs://$BUCKET_NAME/$JOB_NAME \ 
--runtime-version 1.0 \ 
--package-path ./trainer \ 
--region $REGION \ 
--config=trainer/cloudml-gpu.yaml \ 
-- \ 
--train-file gs://informatics-neural-network-data/cons_feature.pickle


gcloud ml-engine jobs submit training $JOB_NAME 
--module-name trainer.make_models
--job-dir gs://$BUCKET_NAME/$JOB_NAME 
--runtime-version 1.0 
--package-path ./trainer 
--region $REGION 
--config=trainer/cloudml-gpu.yaml 
-- 
--train-file gs://informatics-neural-network-data/cons_feature.pickle
