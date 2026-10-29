
pipeline {
    agent any

    stages {
        stage('Verify Environment') {
            steps {
                bat 'python --version'
                bat 'git --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Application') {
            steps {
                bat '.venv\\Scripts\\python.exe hello.py'
            }
        }

        stage('Run Pytest') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                bat '.venv\\Scripts\\python.exe monitor.py'
            }
        }
    }

    post {
        success {
            echo 'UAT DRY RUN PASSED'
        }

        failure {
            echo 'UAT DRY RUN FAILED - CHECK CONSOLE OUTPUT'
        }

        always {
            archiveArtifacts artifacts: 'reports/*.html',
                             allowEmptyArchive: true
        }
    }
}
