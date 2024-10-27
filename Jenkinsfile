pipeline {
    agent any

    tools {
        python 'python3' // Ensure this is configured in Jenkins
    }

    environment {
        VENV = 'venv'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/username/python-jenkins-pipeline.git' // Replace with your repo
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                sh 'python3 -m venv $VENV'
                sh '. $VENV/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. $VENV/bin/activate && python -m unittest discover -s tests'
            }
        }

        stage('Archive Results') {
            steps {
                junit '**/tests/*.xml'
                archiveArtifacts artifacts: '**/*.py', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}

