node {
   echo 'Docker CI Pipeline Started'
   withCredentials([usernamePassword(credentialsId: 'DOCKERHUB_USER', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_TOKEN')]) {
        String serviceName = 'weather-service'
        String imageName = DOCKERHUB_USERNAME + '/' + serviceName
        String imageName = DOCKERHUB_USERNAME + '/' + serviceName
        String tagVerison = 'v1'
        stage('checkout') {
            checkout scm
        }
        stage('docker login') {
            powershell getLogInCmd()
        }
        stage('docker build') {
            powershell getBuildCmd('Dockerfile', imageName, ['v1', 'latest'])
        }
        stage('docker publish') {
            powershell getPushCmd(imageName)
            // powershell """
            //     docker rmi $(docker images --format "{{.Repository}}:{{.Tag}}"|findstr "${imageName}")
            // """

        }
    }
}

String getLogInCmd() {
    def cmd = 'docker login'
    cmd <<= ' --username ' + DOCKERHUB_USERNAME
    cmd <<= ' --password ' + DOCKERHUB_TOKEN
    return cmd.toString()
}

String getBuildCmd(dockerFile, imageName, tagVersions) {
    def cmd = 'docker build'
    cmd <<= ' -f ' + dockerFile
    for (tagVersion in tagVersions) {
        cmd <<= ' -t ' + imageName + ':' + tagVerison
    }
    cmd <<= ' .'
    return cmd.toString()
}

String getPushCmd(imageName) {
    def cmd = 'docker push'
    cmd <<= ' ' + imageName
    cmd <<= ' --all-tags'
    return cmd.toString()
}