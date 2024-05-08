pipeline {
  agent any
  stages {
    // stage('version') {
    //   steps {
    //     bat 'import sys print(sys.version)'
    //   }
    // }
    stage('checkout') {
      steps {
                git branch: 'main', url: 'https://github.com/mohsinkkc/jenkins.git'
            }
    }
    stage('run python script') {
      steps {
        bat 'dir'
        bat 'python program.py'
      }
    }
  }
}
