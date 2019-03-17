'''
This module is to take the Snapshot of the all the Volumes attached to an EC2 Instance.
'''

import boto3
import list_ec2_instances
import ec2_instance_actions
import time


'''Function to take the Snapshot of all the Volumes attached to an EC2 Instance.'''
def take_snapshot(instance_id,region):

    # Making Call to Stop the EC2 Instance before taking the Snapshot.
    print("Stopping the EC2 Instance for the Snapshot to be Taken")
    instance_state=ec2_instance_actions.stop_instance(instance_id,region)
    print(instance_state)

    #Creating a resource for EC2 Service
    ec2 = boto3.resource('ec2',region_name=region)

    #Creating a Sub-resource for the EC2 Instance
    instance = ec2.Instance(instance_id)

    #Storing all the Volumes attached to the instance in a List.
    volumes = instance.volumes.all()

    #Iterating through different Volumes attached to the Instance.
    for v in volumes:
        # Here snapshot_resource is the name of the Snapshot Resource.
        snapshot_resource = ec2.create_snapshot(VolumeId=v.id)

        #Once the Snapshot Creation is initiated checking the status of Snapshot till it is "completed"
        print("Snapshot creation for Volume-ID:{0} initiated".format(v.id))
        snapshot_resource.load()
        while snapshot_resource.state != 'completed':
            print("Snapshot creation is in progress")
            time.sleep(10)
            snapshot_resource.load()
        print("The Snapshot is ready.Snapshot ID is {0}".format(snapshot_resource.id))

    print("SnapShots for all the Volumes have been taken.Starting the EC2 Instance")
    instance_state=ec2_instance_actions.start_instance(instance_id,region)
    print(instance_state)
