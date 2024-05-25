/*Jenkins*/
pipeline {
    agent any

    stages {
        stage('Build') {
            agent any
            steps {
                echo 'Building...'
                sh '''
                    pwd;
                    ls -l;
                    python3 -m venv .venv
                    echo "Activating virtual environment"
                    . .venv/bin/activate
                    echo "Installing the dependencies"
                    pip install -r quickrequirements.txt
                    '''
            }
        }
        
        stage('pylint - calitate cod') {
            agent any
            steps {
                sh '''
                    . .venv/bin/activate

                    echo '\n\nVerificare tests/*.py cu pylint';
                    pylint --exit-zero tests/*.py;

                    echo '\n\nVerificare filme.py cu pylint';
                    pylint --exit-zero filme.py;
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            agent any
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    . .venv/bin/activate  
                    pytest --maxfail=1
                '''
            }
        }
        
        stage('Deploy Docker Container') {
            agent any
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