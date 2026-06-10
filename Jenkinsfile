pipeline {
    agent any

    stages {
        stage('Check enivronment'){
            steps{
                sh ''' 
                    echo 'Checking...'
                    pwd
                    ls -la
                    python3 --version
                    git --version
                '''
            }
        }

        stage('Install dependencies'){
            steps{
                sh'''
                    echo 'Installing...'
                    python3 -m venv .venv
                    source .venv/bin/activate
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run unit tests'){
            steps{
                sh'''
                    echo 'Testing...'
                    source .venv/bin/activate
                    mkdir -p test-results
                    python -m pytest -v --junitxml=test-results/results.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'test-results/*.xml'
        }

    }


}