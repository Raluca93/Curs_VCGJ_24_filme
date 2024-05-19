pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub repository
                git 'https://github.com/Raluca93/Curs_VCGJ_24_filme.git'
            }
        }
        
    

        stage('Run tests') {
            steps {
                // Run the test_lotr.py script
                 dir('app/tests/') {
                    sh 'python -m unittest test_Lotr.py'
                }
            }
        }
    }
}

