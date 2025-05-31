pipeline{
    agent any

    environment {
        VENV_DIR = 'venv'
    }
    
    stages{
        stage('Clonning GitHub Repo To Jenkins'){
            steps{
                script{
                    echo 'Clonning GitHub Repo To Jenkins ..........'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/shanks1554/Hotel-Reservation-Prediction.git']])
                }
            }
        }

        stage('Setting up virtual environment and Installing dependancies'){
            steps{
                script{
                    echo 'Setting up virtual environment and Installing dependancies ..........'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }
    }
}