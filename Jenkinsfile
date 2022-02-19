pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/grabowski-d/jenkins-loves-docker.git', branch: 'lesson5'
            }
        }
        stage('Run app') {
            steps {
                dir('app') {
                    sh 'docker-compose up --build -d'
                }
            }
        }
        stage('Run tests') {
            steps {
                script {
                    env.DATABASE_PASSWORD = readFile 'app/db/password.txt'
                    docker.build('test-runner', 'tests').inside('--network=host') {
                        sh 'pytest --junit-xml=pytest.xml .'
                    }
                }
            }
            post {
                always {
                    junit testResults: '**/*pytest.xml'
                }
            }
        }
    }
    post {
        cleanup {
            dir('app') {
                sh 'docker-compose down'
            }
            cleanWs()
        }
    }
}