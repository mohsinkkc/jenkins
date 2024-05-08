pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat "python --version"
      }
    }
    stage('checkout') {
      steps {
                git branch: 'main', url: 'https://github.com/mohsinkkc/jenkins.git'
            }
    }
    stage('run python script') {
      steps {
        bat script: '"C:\\Users\\Mohasin Mohmad\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe" program.py'
      }
    }
  }
}
