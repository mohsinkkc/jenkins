pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat "import sys \n print(sys.version)"
      }
    }
    stage('program') {
      steps {
        bat "sys program.py"
      }
    }
  }
}
