// Fetching file from github and providing its output

// pipeline {
//     agent any
    
//     stages {
//         stage('Clone Repository') {
//             steps {
//                 git branch: 'main', url: 'https://github.com/mohsinkkc/jenkins.git'
//             }
//         }
//         stage('Run Python Script') {
//             steps {
//                 script {
//                     // Print out the current directory for debugging
//                     bat 'dir'
                    
//                     // Execute the Python script directly
//                     bat 'python program.py'
//                 }
//             }
//         }
//     }
// }


// using Docker running image and container and afterwards fetching Output from program



pipeline {
    agent any

    stages {
        stage('scm') {
            steps {
                git branch: 'main', url: 'https://github.com/mohsinkkc/jenkins.git'
            }
        }
        stage('docker build & push') {
            steps {
                script {
                    bat 'docker build -t mohsinkkc/mohsin:tag123 .'
                }
            }
        }
        stage('push docker image') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'mohsinkkc', variable: 'dockerhubpwd')]) {
                        bat "docker login -u mohsinkkc -p ${dockerhubpwd}"
                    }
                    bat 'docker push mohsinkkc/mohsin:tag123'
                }
            }
        }
        stage('run Python image') {
            steps {
                script {
                    bat 'docker run mohsinkkc/mohsin:tag123 python program.py'
                }
            }
        }
    }
}
