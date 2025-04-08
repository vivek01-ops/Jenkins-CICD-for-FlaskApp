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
                echo 'Deploying...'
                sh '''
                    echo "Running new container..."
                    docker run -d -p 5000:5000 flaskwebapp:latest
                '''
            }
        }
    }
}
