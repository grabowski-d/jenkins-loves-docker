pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'lesson2', url: 'https://github.com/grabowski-d/jenkins-loves-docker.git'
            }
        }
        stage('Build docker image') {
            steps {
                script {
                    appImage = docker.build('sample-app:latest', '--build-arg SERVER_PORT=9000 .')
                }
            }
        }
        stage('Publish') {
            steps {
                script {
                    docker.withRegistry('https://registry.example.com', 'credentials-id') {
                        appImage.push()
                    }
                }
            }
        }
    }
    post {
        cleanup {
            script {
                cleanWs()
                sh "docker image rm ${appImage.id}"
            }
        }
    }
}
