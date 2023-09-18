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
            steps{
                sh "python3 remove_all_instances.py"
            }
        }

        stage('Setting up new EC2'){
            steps{
                sh "terraform init"

            }
        }

        stage('Validate terraform'){
            steps{
                sh "terraform validate"
            }
        }

        stage('Apply terraform'){
            steps{
                sh "terraform apply"
            }
        }

        stage('Changing IP'){
            steps{
                sh ""
            }
        }

        stage('Configuring VM via ansible'){
            steps{
                sh ""
            }
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