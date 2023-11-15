#Configure AWS Provider
provider "aws" {
  #version = "~> 3.74.2"
  region = "us-east-1"
  access_key = "AKIA3UYKQGOHJQKA7YRC"
  secret_key = "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"
}

#Configure an EC2 Resource
resource "aws_instance" "myfirst_terraform_ec2" {
  ami = "ami-0fc5d935ebf8bc3bc"
  instance_type = "t2.micro"
}



