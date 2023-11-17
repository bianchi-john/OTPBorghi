# OTPBorghi


## To install apache superset:

cd apacheSupersetDocker/superset
git clone https://github.com/apache/superset.git
cd superset
git checkout 3.0.0
TAG=3.0.0 docker compose -f docker-compose-non-dev.yml up -d
docker compose
http://localhost:8088
user:admin passw:admin


## To run apache superset:

docker compose
http://localhost:8088
user:admin passw:admin


## To generate dataset data:

    start otp instance
    cd datasetGenerator/main.py
    python3 datasetGenerator/main.py


## To plot graphs:

    plotter.ipynb