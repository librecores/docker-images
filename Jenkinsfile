def docker_images = ["librecores/hosting", " librecores/librecores-ci-modules-fpga", "librecores/ci-modules" , "librecores/librecores-ci-riscv", "librecores/librecores-ci"]

def get_stages(docker_image) {
    stages = {
        docker.image(docker_image).inside {
            stage("${docker_image}") {
                echo 'Running in ${docker_image}'
            }
            stage("Build") {
                sh 'sleep 10'
                sh 'echo this is stage Build'
            }
        }
    }
    return stages
}

node('master') {
    def stages = [:]

    for (int i = 0; i < docker_images.size(); i++) {
        def docker_image = docker_images[i]
        stages[docker_image] = get_stages(docker_image)
    }

    parallel stages
}  
