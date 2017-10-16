from setuptools import setup, find_packages

setup(name='rna-classifier',
  version='0.1',
  packages=find_packages(),
  description='example to run keras on gcloud ml-engine used from: https://liufuyang.github.io/2017/04/02/just-another-tensorflow-beginner-guide-4.html',
  author='Robert Williams',
  author_email='robertmaxwillams@gmail.com',
  license='MIT',
  install_requires=[
      'keras',
      'h5py',
      'numpy'
  ],
  zip_safe=False)
