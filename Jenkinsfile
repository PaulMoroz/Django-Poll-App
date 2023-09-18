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

        stage('Removing all instances'){
            steps{
                sh "python3 merged_test.py"
            }
        }

        stage('Configuring VM via ansible'){
            steps{
                sh "chmod 400 my-key.pem"
                sh 'nohup ansible-playbook -i "16.171.222.150," -u ec2-user -e "ansible_ssh_private_key_file=my-key.pem" setup.yml'
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