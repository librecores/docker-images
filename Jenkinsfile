def docker_images = ["librecores/hosting", " librecores/librecores-ci-modules-fpga", "librecores/ci-modules" , "librecores/librecores-ci-riscv", "librecores/librecores-ci"]

def get_stages(docker_image) {
    stages = {
        docker.image(docker_image).inside {
            stage("${docker_image}") {
                echo 'Running in ${docker_image}'
            }
            stage("Build") {
                sh 'echo this is stage Build'
                container = docker.build('docker_image')
            }
            /* TO DO : Add some test automation 
            stage("Test") {
                sh 'echo this is stage Test'
                sh 'export GOSS_FILES_STRATEGY=cp && /usr/local/bin/dgoss  run --name jenkins-docker-dgoss-test --rm -ti docker_image'
            }*/
        }
    }
    return stages
}

node('master') {
    properties([buildDiscarder(logRotator(numToKeepStr: '50', daysToKeepStr: '10')), disableConcurrentBuilds()])  
    def stages = [:]

    for (int i = 0; i < docker_images.size(); i++) {
        def docker_image = docker_images[i]
        stages[docker_image] = get_stages(docker_image)
    }

    parallel stages
}  
