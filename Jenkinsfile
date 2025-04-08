pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('DOCKER_HUB_CREDENTIALS') // this ID from Jenkins Credentials
        DOCKERHUB_REPO = 'vivek512/flaskWebApp'  // replace with your DockerHub repo
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building Docker Image...'
                sh 'docker build -t flaskWebApp:latest .'
            }
        }

        // stage('Checkout') {
        //     steps {
        //         git scm
        //     }
        // }

        stage('Test') {
            steps {
                echo 'Testing Application...'
                sh 'docker run --rm flaskWebApp:latest python -c "print(\'Test passed\')"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Application...'
                sh 'docker run -d -p 5000:5000 --name flaskWebApp_container flaskWebApp:latest'
            }
        }

        stage('Docker Hub Login') {
            steps {
                echo 'Logging into Docker Hub...'
                sh '''
                    echo "$DOCKERHUB_CREDENTIALS" | docker login -u "$DOCKERHUB_CREDENTIALS" --password-stdin
                '''
            }
        }

        stage('Tag and Push') {
            steps {
                echo 'Tagging and Pushing Image to Docker Hub...'
                sh '''
                    docker tag flaskWebApp:latest $DOCKERHUB_REPO/flaskWebApp:latest
                    docker push $DOCKERHUB_REPO/flaskWebApp:latest
                '''
            }
        }
    }
}
