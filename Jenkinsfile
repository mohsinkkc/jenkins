pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/mohsinkkc/jenkins.git'
            }
        }
        stage('Run Python Script') {
            steps {
                script {
                    // Print out the current directory for debugging
                    bat 'dir'
                    
                    // Execute the Python script directly
                    bat 'python program.py'
                }
            }
        }
    }
}
