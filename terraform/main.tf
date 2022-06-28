terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region     = var.aws_region
  access_key = var.access_key
  secret_key = var.secret_key
}

# Resource for Apache Airflow, Elastic Beanstalk
resource "aws_elastic_beanstalk_application" "bug_sense_main" {
  name = "bug_sense_main"
}

# Create elastic beanstalk Environment

resource "aws_elastic_beanstalk_environment" "bug-sense-main-env" {
  name                = "bug-sense-main-env"
  application         = aws_elastic_beanstalk_application.bug_sense_main.name
  solution_stack_name = "64bit Amazon Linux 2 v3.3.15 running Python 3.8"
  tier                = "WebServer"

  setting {
    namespace = "aws:autoscaling:launchconfiguration"
    name      = "IamInstanceProfile"
    value     = "aws-elasticbeanstalk-ec2-role"
  }

  setting {
    namespace = "aws:autoscaling:launchconfiguration"
    name      = "RootVolumeSize"
    value     = 8
  }

  setting {
    namespace = "aws:autoscaling:asg"
    name      = "MaxSize"
    value     = 1
  }

  setting {
    namespace = "aws:ec2:instances"
    name      = "InstanceTypes"
    value     = "t2.micro"
  }
}