pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = 'skilled-flight-461215-g9'
        GCLOUD_PATH = '/var/jenkins_home/google-cloud-sdk/bin'
    }

    stages {

        stage('Clone GitHub Repository') {
            steps {
                script {
                    echo 'Cloning GitHub Repository...'
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        userRemoteConfigs: [[
                            credentialsId: 'github-token',
                            url: 'https://github.com/shanks1554/Hotel-Reservation-Prediction.git'
                        ]]
                    )
                }
            }
        }

        stage('Install Dependencies in Virtual Environment') {
            steps {
                script {
                    echo 'Setting up virtual environment and installing dependencies...'
                    sh '''
                        python -m venv ${VENV_DIR}
                        . ${VENV_DIR}/bin/activate
                        pip install --upgrade pip
                        pip install -e .
                    '''
                }
            }
        }

        stage('Build and Push Docker Image to GCR') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo 'Building and pushing Docker image to GCR...'
                        sh '''
                            export PATH=${GCLOUD_PATH}:$PATH
                            
                            # Activate GCP service account
                            gcloud auth activate-service-account --key-file="${GOOGLE_APPLICATION_CREDENTIALS}"

                            # Set the project
                            gcloud config set project ${GCP_PROJECT}

                            # Configure Docker to use gcloud credentials
                            gcloud auth configure-docker --quiet

                            # Build the Docker image
                            docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                            # Push the Docker image to GCR
                            docker push gcr.io/${GCP_PROJECT}/ml-project:latest
                        '''
                    }
                }
            }
        }

        stage('Deploy to Google Cloud Run') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo 'Deploy to Google Cloud Run ...'
                        sh '''
                            export PATH=${GCLOUD_PATH}:$PATH
                            
                            # Activate GCP service account
                            gcloud auth activate-service-account --key-file="${GOOGLE_APPLICATION_CREDENTIALS}"

                            # Set the project
                            gcloud config set project ${GCP_PROJECT}

                            gcloud run deploy ml-project \
                                --image=gcr.io/${GCP_PROJECT}/ml-project:latest \
                                --platform=managed \
                                --region=us-central1 \
                                --allow-unauthenticated

                        '''
                    }
                }
            }
        }
    
    }
}
