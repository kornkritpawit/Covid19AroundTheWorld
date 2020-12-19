pipeline {
    agent {
          docker {
               image 'openkbs/jdk-mvn-py3' 
               args '-u root:sudo -p 1111:9000 -p 2222:9090 -p 3333:3000' 
          }
     }
     environment {
          HOME = '.'
     }

     stages {
          stage('Source') {
               steps {
                    git branch: 'master',
                        url: 'https://github.com/kornkritpawit/Covid19AroundTheWorld.git'
               }
          }
          stage('Build') {
               steps {
                    sh 'java -jar openapi-generator-cli-4.3.1.jar generate -i openapi/covid-api.yaml -o autogen -g python-flask'
                    sh 'pip3 install -r requirements.txt'
                    sh 'sudo npm install -g openapi-to-graphql-cli'
                    sh 'npm install'

               }
          }
          stage('Test') {
               steps {
                    echo 'testing...'
               }
          }
          stage('Deploy') {
               steps {
                    parallel(
                       backend: {
                        sh 'python3 app.py'
                       },
                       backendgraphql: {
                        sh 'openapi-to-graphql --cors -u http://host.docker.internal:9090/covid-api/v1/ openapi/covid-api.yaml'
                       },
                       frontend: {
                           sh 'npm start'
                       }
                       )
               }
          }
          
     }
}