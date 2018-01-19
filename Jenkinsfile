#Jenkinsfile

pipeline {
    agent { docker 'python:3.5.1' }
    stages {
        stage('build') {
            steps {
                sh 'python 20180113python.py 10 7'
            }
        }
    }
}
