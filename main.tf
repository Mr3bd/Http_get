 
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
  }
}

provider "docker" {
  host = "npipe:////./pipe/docker_engine"
}

# Build the Docker image using local-exec
resource "null_resource" "build_and_push_image" {
  provisioner "local-exec" {
    command = <<EOT
      docker build -t localhost:5000/http_get_jenkins_nexus:latest .
      docker push localhost:5000/http_get_jenkins_nexus:latest
    EOT
  }
}
