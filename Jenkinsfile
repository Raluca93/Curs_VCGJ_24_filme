/*Jenkins*/
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                    echo 'Building...'
                    sh '''
                        pwd;
                        ls -l;
                        . ./activeaza_venv_jenkins
                        '''
            }
        }
        
        stage('pylint - calitate cod') {
            steps {
                    sh '''
                        . ./activeaza_venv
                        echo '\n\nVerificare tests/*.py cu pylint';
                        pylint --exit-zero tests/*.py;

                        echo '\n\nVerificare filme.py cu pylint';
                        pylint --exit-zero filme.py;
                    '''
                
            }
        }

        stage('Unit Testing cu pytest') {
            steps {
                    echo 'Unit testing with Pytest...'
                    sh '''
                        . ./activeaza_venv
                        pytest --maxfail=1
                    '''
            }
        }
        
        stage('Deploy Docker Container') {
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                echo "Creare imagine docker"
                sh '''
                    docker build -t movieimage:v${BUILD_NUMBER} .
                    docker create --name moviecontainer${BUILD_NUMBER} -p 8020:5011 movieimage:v${BUILD_NUMBER}
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                        withCredentials([string(credentialsId: 'dockerhubpwd-id', variable: 'dockerhubpwd')]) {
                        sh '''
                            docker login -u octaviant16 -p ${dockerhubpwd}
                            docker tag movieimage:v${BUILD_NUMBER} octaviant16/movieimage:v${BUILD_NUMBER}
                            docker push octaviant16/movieimage:v${BUILD_NUMBER}
                        '''
                    }
                }
            }
        }
    }
}