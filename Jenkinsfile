pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
				echo "Checkout"
				//git branch: 'master', url: 'https://github.com/AlmosovM/UdemyFlaskAppUTest/blob/master/Jenkinsfile'
				sh 'ls -l'
            }
        }
     stage('Unit Tests') {
           steps {
				echo "Unit Tests"
				//sh(returnStatus: true, script: '. ~/.bashrc \n pyenv version')
				//sh('chmod +x ./jenkinsscript.sh')
				sh('bash ./jenkinsscript.sh')
          }
        }
	stage("Publish Junit report") {
            steps{
				echo "Publish Junit"
				junit skipMarkingBuildUnstable: true, testResults: 'xmlReport/output.xml'
            }
        }
	stage ("Publish Code Coverage") {
            steps{
				echo "Publish code coverage"
				recordCoverage(
						    tools: [[
						        parser: 'COBERTURA',
						        pattern: 'coverage.xml'
						    ]]
						)
            }
        }
    }
}
