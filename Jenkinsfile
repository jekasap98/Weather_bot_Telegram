pipeline {
    agent none
    
    stages {
        stage('Build Docker Image') {
            agent {
                label 'docker'
            }
            steps {
                sh 'docker rmi -f ${DOCKER_IMAGE_NAME}'
                sh "docker build -t ${DOCKER_IMAGE_NAME} ." 
            }
        }
        stage('Push Docker Image') {
            agent {
                label 'docker'
            }
            steps {
                sh "docker push ${DOCKER_IMAGE_NAME}"
            }
        }
        stage('Deploy Dev') {
            agent {
                label 'dev'
                }
                steps {
                    input(message: 'Please confirm Deploy Prod', ok: 'Proceed?')
                    script {
                        sh 'docker rmi -f ${DOCKER_IMAGE_NAME}'
                        sh 'docker run -e TOKEN_TELEGRAM=${TOKEN_TEL} -e TOKEN_API_WEATH=${TOKEN_API} -d ${DOCKER_IMAGE_NAME}'
                    }
                }
            }

    }
}


