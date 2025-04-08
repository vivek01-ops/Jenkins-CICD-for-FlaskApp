pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials-id') // Jenkins Credentials ID
        DOCKERHUB_REPO = 'yourdockerhubusername/yourappname'
    }

    triggers {
        pollSCM('* * * * *')  // Poll GitHub every minute for changes
    }

    stages {
        stage('Clone repository') {
            steps {
                git branch: 'main', url: 'https://github.com/yourusername/your-repo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKERHUB_REPO}:${BUILD_NUMBER}")
                }
            }
        }

        stage('Login to DockerHub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials-id') {
                        echo 'Logged in to DockerHub'
                    }
                }
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials-id') {
                        dockerImage.push()
                    }
                }
            }
        }
    }

    post {
        success {
            echo '✅ Build and Push successful!'
        }
        failure {
            echo '❌ Build or Push failed.'
        }
    }
}
