pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Check out your Git repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python and Django dependencies
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Testing') {
            steps {
                sh 'python3 manage.py test' 
            }
        }

        stage('Deploy'){
            sh "terraform apply -auto-approve"  
            def instanceIp = sh(script: 'terraform output instance_ip', returnStdout: true).trim()
            writeFile file: 'inventory.ini', text: "[terraform_instance]\n${instanceIp}\n"
            sh "cat inventory.ini"
            sh "chmod 400 my-key.pem"
        }

        post{
            success{
                
            }
        }
    }

}
