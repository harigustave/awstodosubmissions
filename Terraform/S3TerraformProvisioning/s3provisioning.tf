#Configure AWS Provider
provider "aws" {
  region = "us-west-2"
  access_key = "AKIA3UYKQGOHJQKA7YRC"
  secret_key = "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"
}

#Configure an s3 Resource(s)
resource "aws_s3_bucket" "adventuretech" {
  bucket = "adventuretech-gh-bucket"
  acl = "private"
}

resource "aws_s3_bucket" "natureescape" {
  bucket = "natureescape-gh-bucket"
  acl = "private"
}

resource "aws_s3_bucket" "datasummit" {
  bucket = "datasummit-gh-bucket"
  acl = "private"
}



