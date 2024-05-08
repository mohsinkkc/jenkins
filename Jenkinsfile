pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('program') {
      steps {
        bat 'python program.py'
      }
    }
  }
}