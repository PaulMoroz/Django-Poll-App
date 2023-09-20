import boto3
import time
import os
import secrets
import string

# Define your AWS region and other configuration options
aws_region = 'eu-north-1'
instance_type = 't3.micro'
ami_id = 'ami-0b0d560d43e65a601'

# Read AWS credentials and configuration from environment variables
aws_access_key = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

# Check if all required environment variables are set
if not (aws_access_key and aws_secret_key):
    raise ValueError("AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables must be set.")

# Initialize the AWS clients
ec2_client = boto3.client('ec2', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)

# Generate a random key name and check if it already exists
while True:
    key_name = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(10))
    existing_key_names = [key['KeyName'] for key in ec2_client.describe_key_pairs()['KeyPairs']]
    if key_name not in existing_key_names:
        break

# Create an SSH key pair
response = ec2_client.create_key_pair(KeyName=key_name)
private_key = response['KeyMaterial']

# Save the private key to a file\
os.remove(f'my-key.pem')

with open(f'my-key.pem', 'w') as key_file:
    key_file.write(private_key)
    print('key is created')
# Generate a random security group name and check if it already exists
while True:
    security_group_name = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(10))
    existing_security_groups = [group['GroupName'] for group in ec2_client.describe_security_groups()['SecurityGroups']]
    if security_group_name not in existing_security_groups:
        break

# Create a security group
security_group = ec2_client.create_security_group(
    GroupName=security_group_name,
    Description='Allow all inbound and outbound traffic'
)

# Define ingress rules for the security group
ec2_client.authorize_security_group_ingress(
    GroupId=security_group['GroupId'],
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': 0,
            'ToPort': 65535,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        },
        {
            'IpProtocol': 'icmp',
            'FromPort': -1,
            'ToPort': -1,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        },
    ]
)

# Define egress rules for the security group
ec2_client.authorize_security_group_egress(
    GroupId=security_group['GroupId'],
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': 0,
            'ToPort': 65535,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        },
        {
            'IpProtocol': 'icmp',
            'FromPort': -1,
            'ToPort': -1,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        },
    ]
)

# Launch an EC2 instance with the specified security group
instance = ec2_client.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    MinCount=1,
    MaxCount=1,
    KeyName=key_name,
    SecurityGroupIds=[security_group['GroupId']],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'poll-app'}]
        }
    ]
)

# Wait for the instance to be running
instance_id = instance['Instances'][0]['InstanceId']
ec2_client.get_waiter('instance_running').wait(InstanceIds=[instance_id])

# Get the public IP address of the instance
instance = ec2_client.describe_instances(InstanceIds=[instance_id])
public_ip = instance['Reservations'][0]['Instances'][0]['PublicIpAddress']

elastic_ip = '16.170.20.103'  # Replace with your Elastic IP address


print(f'Instance ID: {instance_id}')
print(f'Public IP Address: {public_ip}')

response = ec2_client.describe_addresses(PublicIps=[elastic_ip])
allocation_id = response['Addresses'][0]['AllocationId']

# Associate the Elastic IP with the EC2 instance
ec2_client.associate_address(InstanceId=instance_id, AllocationId=allocation_id)

print(f"Associated Elastic IP {elastic_ip} with EC2 instance {instance_id}")




