pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat "import sys \n print(sys.version)"
      }
    }
    stage('checkout') {
      steps {
                git branch: 'main', url: 'https://github.com/mohsinkkc/jenkins.git'
            }
    }
    stage('run python script') {
      steps {
        bat script: 'python.exe program.py'
      }
    }
  }
}
