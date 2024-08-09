# Projektarbeit in Softwareentwicklung 2

- Python package: [ensemble_package](ensemble_package)
  - The package is deployed at pypi
  - The url is the following: (https://pypi.org/project/ensemble-package/)
- Docker commands (Dockerfile)
  - docker build -t my-flask-app .
  - docker run -d -P 5000:5000 my-flask-app:latest
- The local API test is available at [request_api.http](request_api.http)
  - Possile regressors are: ['linear_regressor', 'nearest_neighbor_regressor', 'ridge_regressor']
- The testing is available at [unit_testing.py](ensemble_package/unit_testing.py)