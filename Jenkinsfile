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
                    . ./activeaza_venv_jenkins
                    '''
            }
        }
        
        // stage('pylint - calitate cod') {
        //     agent any
        //     steps {
        //         sh '''
        //             . ./activeaza_venv;
        //             echo '\n\nVerificare lib/*.py cu pylint\n';
        //             pylint --exit-zero lib/*.py;

        //             echo '\n\nVerificare tests/*.py cu pylint';
        //             pylint --exit-zero tests/*.py;

        //             echo '\n\nVerificare filme.py cu pylint';
        //             pylint --exit-zero filme.py;
        //         '''
        //     }
        // }

        // stage('Unit Testing cu pytest') {
        //     agent any
        //     steps {
        //         echo 'Unit testing with Pytest...'
        //         sh '''
        //             . ./activeaza_venv;
        //             flask --app sysinfo test;
                    
        //         '''
        //     }
        // }
        
    }
}