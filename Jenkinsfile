
pipeline {
    agent any

    environment {
        PYTHON_ENV = 'venv'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'dev', url: 'https://github.com/your-repo/your-project.git'
            }
        }
        stage('Setup Python Environment') {
            steps {
                sh 'python3 -m venv ${PYTHON_ENV}'
                sh '. ${PYTHON_ENV}/bin/activate'
                sh 'pip install -r requirements.txt'
                sh 'pip install pytest-html'
            }
        }
        stage('Run API Tests') {
            steps {
                sh '. ${PYTHON_ENV}/bin/activate'
                sh 'pytest QA_Auto_API/HW_15/test --html=report.html'
            }
        }
        stage('Publish HTML Report') {
            steps {
                publishHTML(target: [
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'API Test Report'
                ])
            }
        }
    }

    post {
        always {
            sh 'deactivate || true'
            cleanWs()
        }
    }
}
