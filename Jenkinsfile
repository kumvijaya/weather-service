node {
   echo 'Docker CI Pipeline Started'
   withCredentials([usernamePassword(credentialsId: 'DOCKERHUB_USER', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_TOKEN')]) {
        String serviceName = 'weather-service'
        String imageName = "${DOCKERHUB_USERNAME}/${serviceName}"
        String tagVerison = 'v1'
        stage('checkout') {
            checkout scm
        }
        stage('docker login') {
            powershell "echo ${DOCKERHUB_TOKEN} | docker login --username ${DOCKERHUB_USERNAME} --password-stdin"
        }
        stage('docker build') {
            powershell "docker build -f Dockerfile -t ${imageName}:${tagVerison} -t ${imageName}:latest ."
        }
        stage('docker publish') {
            powershell "docker push ${imageName} --all-tags"
            // powershell """
            //     docker rmi $(docker images --format "{{.Repository}}:{{.Tag}}"|findstr "${imageName}")
            // """
        }
    }
}