/*Jenkins*/
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    pwd
                    ls -l
                    source ./activeaza_venv_jenkins
                '''
            }
        }

        stage('pylint - calitate cod') {
            steps {
                sh '''
                    source ./activeaza_venv
                    # Activăm din nou mediul virtual pentru stadiul pylint.
                    echo '\n\nVerificare app/lib/biblioteca_filme.py cu pylint\n'
                    pylint --exit-zero app/lib/biblioteca_filme.py

                    echo '\n\nVerificare filme.py cu pylint'
                    pylint --exit-zero filme.py
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    source ./activeaza_venv
                    pytest --maxfail=1 --disable-warnings -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                echo "Creare imagine docker"
                sh '''
                    docker build -t filme:v${BUILD_NUMBER} .
                    docker create --name filme${BUILD_NUMBER} -p 8020:5011 filme:v${BUILD_NUMBER}
                '''
            }
        }
    }
}

