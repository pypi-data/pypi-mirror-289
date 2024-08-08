provider "google" {
  project = var.gcp_project_id
  region  = var.gcp_region
}


resource "google_compute_region_instance_template" "template" {
  # We make this a tiny vm since it will be replaced when the user deploys
  machine_type = "e2-micro"
  disk {
    boot         = true
    source_image = "cos-cloud/cos-stable-109-17800-147-54"
  }
  labels = {
    container-vm = "cos-stable-109-17800-147-54"
  }
  metadata = {
    google-logging-enabled    = "true"
    google-monitoring-enabled = "true"
    gce-container-declaration = jsonencode({
      spec = {
        containers    = [{ image = "httpd" }]
        volumes       = []
        restartPolicy = "Always"
      }
    })
  }

  service_account {
    email  = var.environment_service_account_email
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral IP
    }
  }
  tags = [var.resource_id]
}

resource "google_compute_region_instance_group_manager" "mig" {
  base_instance_name = var.base_instance_name
  region             = var.region
  name               = var.resource_id
  target_size        = var.target_size
  version {
    instance_template = google_compute_region_instance_template.template.self_link
  }

  lifecycle {
    # We ignore changes to version since that will change as things are depoyed
    ignore_changes = [version]
  }
}

output "gcp_id" {
  value = google_compute_region_instance_group_manager.mig.id
}
