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

        stage('Database Setup') {
            steps {
                // Set up your database (e.g., migrate and create a test database)
                //sh 'python manage.py migrate'
                sh 'python3 manage.py test' // Run Django tests
            }
        }
    }

}
