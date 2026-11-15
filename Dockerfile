# https://docs.docker.com/reference/dockerfile/
FROM docker.io/python:3.9

COPY saludar.py saludar.py
COPY test_saludar.py test_saludar.py

ENTRYPOINT ["python3", "-m", "saludar"]

