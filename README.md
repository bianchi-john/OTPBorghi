# OTPBorghi


## To run apache superset:

    docker stop $(docker ps -aq) && docker rm $(docker ps -aq) && docker rmi $(docker images -q) --force
    cd apacheSupersetDocker/incubator-superset
    docker-compose up
    http://localhost:8088
    username: admin
    password: admin

info: https://apache-superset.readthedocs.io/en/latest/installation.html


## To generate dataset data:

    start otp instance
    cd datasetGenerator/main.py
    python3 datasetGenerator/main.py


## To plot graphs:

    plotter.ipynb