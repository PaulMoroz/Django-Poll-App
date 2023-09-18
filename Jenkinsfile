pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Testing') {
            steps {
                sh 'python3 manage.py test' 
            }
        }

        stage('Removing all instances'){

        }

        stage('Setting up new EC2'){

        }

        stage('Changing IP'){

        }

        stage('Configuring VM via ansible'){

        }
    }
/*  
        stage('Deploy'){
            sh "terraform apply -auto-approve"  
            def instanceIp = sh(script: 'terraform output instance_ip', returnStdout: true).trim()
            writeFile file: 'inventory.ini', text: "[terraform_instance]\n${instanceIp}\n"
            sh "cat inventory.ini"
            sh "chmod 400 my-key.pem"
        }
*/

}
