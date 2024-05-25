/*Jenkins*/
pipeline {
    agent none

    stages {
        stage('Build') {
            agent any
            steps {
                echo 'Building...'
                sh '''
                    pwd;
                    ls -l;
                    python3 -m venv .venv
                    . .venv/bin/activate   
                    pip install -r quickrequirements.txt
                    '''
            }
        }
        
        stage('pylint - calitate cod') {
            agent any
            steps {
                sh '''
                    . .venv/bin/activate  
                    echo '\n\nVerificare lib/*.py cu pylint\n';
                    pylint --exit-zero lib/*.py;

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
                    flask --app filme test;
                    
                '''
            }
        }
        
    }
}