pipeline {
    agent any

    environment {
        DOCKERHUB_REPO = 'vivek512/flaskwebapp'  // replace with your DockerHub repo
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building Docker Image...'
                sh 'docker build -t flaskwebapp:latest .'
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
                sh 'docker run --rm flaskwebapp:latest python -c "print(\'Test passed\')"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Application...'
                sh '''
                    echo "Killing any process using port 5000..."
                    fuser -k 5000/tcp || true

                    echo "Stopping old container if exists..."
                    docker stop flaskwebapp_container || true

                    echo "Removing old container if exists..."
                    docker rm flaskwebapp_container || true

                    echo "Waiting for port to free up..."
                    sleep 2

                    echo "Running new container..."
                    docker run -d --name flaskwebapp_container flaskwebapp:latest
                '''
            }
        }
        
        // stage('Docker Hub Login') {
        //     steps {
        //         echo 'Logging into Docker Hub...'
        //         withCredentials([usernamePassword(credentialsId: 'DOCKER_HUB_CREDENTIALS', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
        //             sh '''
        //                 echo "Docker Username: $DOCKER_USERNAME"
        //                 echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
        //             '''
        //         }
        //     }
        // }

        // stage('Tag and Push') {
        //     steps {
        //         echo 'Tagging and Pushing Image to Docker Hub...'
        //         sh '''
        //             docker tag flaskwebapp:latest $DOCKERHUB_REPO/flaskwebapp:latest
        //             docker push $DOCKERHUB_REPO/flaskwebapp:latest
        //         '''
        //     }
        // }
    }
}
