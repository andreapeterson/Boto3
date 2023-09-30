import boto3
import time

client = boto3.client("ec2")


# Launch EC2 and get it's ID
response1 = client.run_instances(ImageId='ami-04c4add5d719e434e', InstanceType='t2.micro', MinCount=1, MaxCount=1)

new_instance = (response1['Instances'][0]['InstanceId'])
print(new_instance)


# Stop that EC2 instance
time.sleep(45) # Wait for instance to get in running state
response2 = client.stop_instances(InstanceIds=[new_instance])
print(f"The instance is {response2['StoppingInstances'][0]['CurrentState']['Name']}")


# Re-start that EC2 instance
time.sleep(30)
response3 = client.start_instances(InstanceIds=[new_instance])
print(f"The instance is {response3['StartingInstances'][0]['CurrentState']['Name']}")


# Terminate that instance
time.sleep(30)
response4 = client.terminate_instances(InstanceIds=[new_instance])
print(f"The instance is {response4['TerminatingInstances'][0]['CurrentState']['Name']}")

# Return ids of all terminated instances in account
response5 = client.describe_instances(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['terminated']
}])

print("The terminated instances are:")
for reservation in response5['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'])