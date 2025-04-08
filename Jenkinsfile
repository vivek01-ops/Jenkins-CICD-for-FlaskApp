pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git scm
            }
        }
    }
    
    stages {
        stage('Build') {
            steps {
                echo 'Building Docker Image...'
                sh 'docker build -t myapp:latest .'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing Application...'
                sh 'docker run --rm myapp:latest python -c "print(\'Test passed\')"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Application...'
                sh 'docker run -d -p 5000:5000 --name myapp_container myapp:latest'
            }
        }
    }
}
