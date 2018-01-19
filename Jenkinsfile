#Jenkinsfile

pipeline {
    agent { docker 'python:3.5.1' }
    stages {
        stage('build') {
            steps {
                sh 'python mySysAdd.py 10 7'
            }
        }
    }
}
