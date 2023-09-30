import boto3


SRC_RGN = 'us-east-1'
FILTER = [
    {
        'Name': 'tag:Copy',
        'Values': ['yes']
    }
]
client = boto3.client('ec2')
resource = boto3.resource('ec2')

# Create Images
image_ids = []
instances = resource.instances.filter(Filters=FILTER)
for instance in instances:
    image = instance.create_image(Name='Demo Boto')
    image_ids.append(image.id)

# Wait for image to exit
waiter = client.get_waiter('image_available')
waiter.wait(Filters=[{'Name': 'image-id', 'Values': image_ids}])

# Copy images to other regions
dest_region = 'us-east-2'
client2 = boto3.client('ec2', region_name=dest_region)
for image in image_ids:
    client2.copy_image(Name='CopiedBoto', SourceImageId=image, SourceRegion='us-east-1')