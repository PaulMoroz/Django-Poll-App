import boto3
import os
# Read AWS credentials and configuration from environment variables
aws_access_key = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
region_name = os.environ.get('AWS_REGION')  # Replace with your preferred region

# Check if all required environment variables are set

# Check if all required environment variables are set
if not (aws_access_key):
    raise ValueError("AWS_ACCESS_KEY_ID environment variables must be set.")

if not (aws_secret_key):
    raise ValueError("AWS_SECRET_ACCESS_KEY environment variables must be set.")

if not (region_name):
    raise ValueError("AWS_REGION environment variables must be set.")
# Create a Boto3 EC2 client
ec2_client = boto3.client('ec2', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=region_name)

instance_name = "poll-app"

# Describe instances with the specified name
response = ec2_client.describe_instances(Filters=[{'Name': 'tag:Name', 'Values': [instance_name]}])

# Check if there are instances to terminate
instances = response['Reservations']
if not instances:
    print(f"No instances named {instance_name} found.")
else:
    print(f"Terminating instances with the name {instance_name}:")
    for reservation in instances:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            # Terminate the EC2 instance
            ec2_client.terminate_instances(InstanceIds=[instance_id])
            print(f"Terminated instance: {instance_id}")