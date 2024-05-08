pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh '--python --version'
      }
    }
    stage('program') {
      steps {
        sh '--python program.py'
      }
    }
  }
}