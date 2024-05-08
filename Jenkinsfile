pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('program') {
      steps {
        sh 'python program.py'
      }
    }
  }
}