pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'zealous_wing'
        DOCKER_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull code from the GitHub repository
                git branch: 'main', url: 'https://github.com/jyoti-nikumbe04/Dockerfiles.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using the Dockerfile in the repository
                    docker.build("${DOCKER_IMAGE_NAME}:${DOCKER_TAG}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container in detached mode
                    docker.run("${DOCKER_IMAGE_NAME}:${DOCKER_TAG}")
                }
            }
        }
    }

    post {
        always {
            // Clean up after the build is done
            cleanWs()
        }
    }
}
