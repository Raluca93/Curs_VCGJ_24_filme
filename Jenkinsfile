pipeline {
    agent any
    
    environment {
        FLASK_APP = './app/pac441d.py'
    }
    
    stages {
        
    stage('install dependencies'){
    	steps{
    		
                echo 'Building...'
                sh '''
                    pip install flask;
                    pip install pytest;
                    pip install pylint;
                    pip list
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
