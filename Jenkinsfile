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
                git branch: 'main', url: 'https://github.com/mohsinkkc/xduce.git'
            }
    }
    stage('program') {
      steps {
        bat "python program.py"
      }
    }
  }
}
