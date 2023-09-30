import boto3
from datetime import datetime, timedelta, timezone


FILTER = [
    {
        'Name': 'tag:Backup',
        'Values': ['yes']
    }
]

ec2 = boto3.resource('ec2')

for instance in ec2.instances.filter(Filters=FILTER):
    for vol in instance.volumes.all():
        vol.create_snapshot(Description='Created by Boto3')


snapshots = ec2.snapshots.filter(OwnerIds=['self'])

for snapshot in snapshots:
    snapshot_start = snapshot.start_time
    delete_time = datetime.now(tz=timezone.utc) - timedelta(days=14.16666666666) #weird number makes up for utc
    if delete_time > snapshot_start:
        snapshot.delete()
