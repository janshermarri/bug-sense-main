variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-west-2"
}

variable "access_key" {
  description = "AWS Access Key"
  type        = string
  default        = ""
}

variable "secret_key" {
  description = "AWS Secret Key"
  type        = string
  default        = ""
}

# variable "security_group" {
#   description = "Security Group"
#   type        = string
# }

# variable "security_group_name" {
#   description = "Security Group"
#   type        = string
# }
