# Flask Web App Deployment using Jenkins and Docker

Foobar is a Python library for dealing with word pluralization.

## Project Overview

This project demonstrates how to automatically build, dockerize, and deploy a Flask web application using Jenkins pipelines integrated with Docker.

## Prerequisites
- Jenkins installed and running

- Docker installed on the Jenkins host machine

- GitHub repository containing:

- DockerHub account and credentials configured in Jenkins


## Project Structure

```bash
.
├── app.py             # Flask application
├── Dockerfile         # Dockerfile to containerize the app
├── Jenkinsfile        # Jenkins pipeline configuration
└── requirements.txt   # Python dependencies

```

## How to Verify Jenkins is Using Updated Jenkinsfile?
- Make sure Jenkins is pulling the latest code from GitHub.

- Push the updated Jenkinsfile to your repository.

- Manually trigger a new build in Jenkins or configure GitHub Webhooks for automatic build triggers.

- Check the Console Output in Jenkins to confirm it’s using the new pipeline steps.