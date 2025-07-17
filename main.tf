terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {
  host = "npipe:////./pipe/docker_engine" # For Windows
}

# Build the image with the registry tag from the start
resource "docker_image" "my_app_image" {
  name = "192.168.20.231:5000/http_get_by_terra:latest"

  build {
    context    = "./docker-build"
    dockerfile = "./Dockerfile"
  }

  # Force Terraform to not use the cached image
  keep_locally = false
}

# Push the image to registry
resource "docker_registry_image" "my_app_registry_image" {
  name = docker_image.my_app_image.name
  
  insecure_skip_verify = true
  
  # Optional: If your registry requires authentication
  auth_config {
     address = "http://192.168.20.231:5000"
     username     = "admin"
     password     = "P@ssw0rd1"
  }

}

output "docker_image_name" {
  description = "The full name of the Docker image pushed to Nexus."
  value       = docker_image.my_app_image.name
}