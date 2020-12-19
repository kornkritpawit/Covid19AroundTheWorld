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
                        url: 'https://github.com/kornkritpawit/covidSoftpro.git'
               }
          }
          stage('Build-backend') {
               steps {
                   parallel(
                       backend: {
                    sh 'java -jar openapi-generator-cli-4.3.1.jar generate -i openapi/covid-api.yaml -o autogen -g python-flask'
                    sh 'pip3 install -r requirements.txt'
                    sh 'python3 app.py'
                       },
                       backendgraphql: {
                    sh 'sudo npm install -g openapi-to-graphql-cli'
                    sh 'openapi-to-graphql --cors -u http://localhost:9090/covid-api/v1/ openapi/covid-api.yaml'
                       },
                       frontend: {
                           sh 'npm install'
                           sh 'npm start'
                       }
                       )

               }
          }
     }
}