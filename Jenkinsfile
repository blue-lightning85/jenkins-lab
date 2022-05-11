pipeline {
  agent any
  stages {
    stage('Run') {
      steps {
        git(url: 'https://github.com/mvieira424/jenkins-lab.git', branch: 'main')
        sh 'python3 test.py'
      }
    }

    stage('Test') {
      steps {
        sh 'python3 unit-test.py'
      }
    }

  }
}