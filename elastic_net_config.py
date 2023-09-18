import boto3
import os
# Read AWS credentials and configuration from environment variables
aws_access_key = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
region_name = os.environ.get('AWS_REGION')  # Replace with your preferred region

# Check if all required environment variables are set
if not (aws_access_key and aws_secret_key and region_name):
    raise ValueError("AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_REGION environment variables must be set.")

# Create a Boto3 EC2 client
ec2_client = boto3.client('ec2', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=region_name)

# Describe the Elastic IP to get its allocation ID
response = ec2_client.describe_addresses(PublicIps=[elastic_ip])
allocation_id = response['Addresses'][0]['AllocationId']

# Associate the Elastic IP with the EC2 instance
ec2_client.associate_address(InstanceId=instance_id, AllocationId=allocation_id)

print(f"Associated Elastic IP {elastic_ip} with EC2 instance {instance_id}")
