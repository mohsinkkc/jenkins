pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat "import sys
        print(sys.version)"
      }
    }
    stage('program') {
      steps {
        bat "python program.py"
      }
    }
  }
}
