# main.tf
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "b" {
  bucket = "my-devsecops-project-bucket-dp"
  # This is a security risk: Public access is not blocked!
}

resource "aws_s3_bucket_public_access_block" "example" {
  bucket = aws_s3_bucket.b.id

  block_public_acls       = false # SECURITY RISK
  block_public_policy     = false # SECURITY RISK
  ignore_public_acls      = false
  restrict_public_buckets = false
}