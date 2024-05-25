pipeline {
    agent any
    
    environment {
        FLASK_APP = './app/pipoi_andrei_441d_filme.py'
    }
    
    stages {
        
    stage('install dependencies'){
    	steps{
    		
                echo 'Building...'
                sh '''
                    pip install flask;
                    pip install pytest;
                    pip install pylint;
                    '''
            
    	}
    }

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
