pipeline {
    agent any
    
    environment {
        FLASK_APP = 'filme.py' 
    }
    
    stages {     
    
        stage('Run tests') {
            steps {
             script{   
                    def testResult = sh(script: 'flask test', returnStatus: true)
                    
                    
                    if (testResult == 0) {
                        echo "Tests were successful!"
                    } else {
                        echo "Tests failed!"
                        error "There are test failures."
                    }
            }
                }
            }
        }
    }


