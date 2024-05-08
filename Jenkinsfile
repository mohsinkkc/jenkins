pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python3 --version'
      }
    }
    stage('program') {
      steps {
        bat 'python program.py'
      }
    }
  }
}