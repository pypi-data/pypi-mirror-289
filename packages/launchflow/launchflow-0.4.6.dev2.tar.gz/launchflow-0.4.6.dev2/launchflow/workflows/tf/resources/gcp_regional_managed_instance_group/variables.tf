#
# LaunchFlow global tofu variables
#
variable "gcp_project_id" {
  type = string
}

variable "gcp_region" {
  type = string
}

variable "resource_id" {
  type = string
}

variable "artifact_bucket" {
  type = string
}

variable "environment_service_account_email" {
  type = string
}

#
# Managed instance group tofu variables
#

variable "base_instance_name" {
  type = string
}

variable "target_size" {
  type = number
}

variable "region" {
  type = string
}
