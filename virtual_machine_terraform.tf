# Define the provider for AWS
provider "aws" {
  region = "eu-north-1" # Set your desired AWS region
}

# Generate a new SSH key pair
resource "aws_key_pair" "my_key" {
  key_name   = "my-key"
  public_key = tls_private_key.my_key.public_key_openssh
}

resource "tls_private_key" "my_key" {
  algorithm = "RSA"
  rsa_bits  = 2048
}

# Output the private key to a file
resource "local_file" "private_key" {
  filename = "my-key.pem" # Specify the desired file name
  content  = tls_private_key.my_key.private_key_pem
}

# Define a security group for SSH access
resource "aws_security_group" "ssh" {
    name        = "allow-all-traffic"
  description = "Allow all inbound and outbound traffic"

  // Ingress rule to allow all inbound traffic
  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  // Ingress rule to allow all inbound ICMP traffic (ping, etc.)
  ingress {
    from_port   = -1
    to_port     = -1
    protocol    = "icmp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  // Egress rule to allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  // Egress rule to allow all outbound ICMP traffic
  egress {
    from_port   = -1
    to_port     = -1
    protocol    = "icmp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Define the EC2 instance with the security group
resource "aws_instance" "example" {
  ami           = "ami-0b0d560d43e65a601" # Your desired AMI ID
  instance_type = "t3.micro" # Choose an appropriate instance type
  key_name      = aws_key_pair.my_key.key_name

  vpc_security_group_ids = [aws_security_group.ssh.id] # Attach the security group to the instance

  tags = {
    Name = "poll-app"
  }
}

# resource block for ec2 and eip association #
resource "aws_eip" "my_eip" {
  instance = aws_instance.example.id # Associate EIP with the EC2 instance
}

# Output the instance's public IP for convenience
output "instance_ip" {
    value = aws_instance.example.public_ip
}