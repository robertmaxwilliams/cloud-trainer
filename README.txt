This directory contains files for creating a job for google's cloud based machine learning platforms.

Note that raw_data and data are both missing. create_data.py will take whitespace delimited files from raw_data and output training data as pickled list of [X, y], where X is input array and y is the desired output array.

If everything is configured correctly and the buckets are accesible under your cloudml account, run ./run-cloud.sh to upload code to run. 

TODO:
-update configuration
-increase batch size to more effecient running on huge GPU (only 3x increase with current settings)

How it works:
This directory is a python package, which gets sent to cloudml and has the specified files called with specified arguments, in this case, "make_models.py" is called with the path to a pickle containing training data.
setup.py is ran first, installing Keras and other required packages.
