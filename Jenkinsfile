pipeline{
    agent any
    
    stages{
        stage('Clonning GitHub Repo To Jenkins'){
            steps{
                script{
                    echo 'Clonning GitHub Repo To Jenkins ..........'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/shanks1554/Hotel-Reservation-Prediction.git']])
                }
            }
        }
    }
}