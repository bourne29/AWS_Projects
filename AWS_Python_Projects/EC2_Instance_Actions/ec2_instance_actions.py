'''
This module is perform actions on EC2 Instances.
For example:
1. Getting the state of the Instance like Running,Stopped etc.
2. Starting the EC2 Instance.
3. Stopping the EC2 Instance.
4. Terminating the EC2 Instance.
and so on ...
'''



import time
import boto3


'''Function to get the instance state like if the instance is Running, Stopped etc.'''
def get_instance_state(instance_id,region):

    ec2_client = boto3.client('ec2',region_name=region)
    response=ec2_client.describe_instances(InstanceIds=[instance_id])
    x_list=response['Reservations']

    for alpha_dict in x_list:
        for instances in alpha_dict["Instances"]:
            instance_state=instances['State']['Name']

    return instance_state


'''Function to Start the Instances'''
def start_instance(instance_id,region):
    ec2 = boto3.resource('ec2', region_name=region)
    instance = ec2.Instance(instance_id)
    instance.start()
    instance_state=get_instance_state(instance_id,region)
    while instance_state != 'running':
        time.sleep(10)
        instance_state=get_instance_state(instance_id,region)
    return "Instance {0} is Running!!!".format(instance_id)



'''Function to Stop the Instances'''
def stop_instance(instance_id,region):
    ec2 = boto3.resource('ec2', region_name=region)
    instance = ec2.Instance(instance_id)
    instance.stop()
    instance_state=get_instance_state(instance_id,region)
    while instance_state != 'stopped':
        time.sleep(10)
        instance_state=get_instance_state(instance_id,region)
    return "Instance {0} has Stopped!!!".format(instance_id)



'''Function to Reboot the Instances'''
def reboot_instance(instance_id,region):
    ec2 = boto3.resource('ec2', region_name=region)
    instance = ec2.Instance(instance_id)
    instance.reboot()
    instance_state=get_instance_state(instance_id,region)
    time.sleep(5)
    while instance_state != 'running':
        time.sleep(10)
        instance_state=get_instance_state(instance_id,region)
    return "Instance {0} has Rebooted!!!".format(instance_id)


'''Function to Terminate the Instances'''
def terminate_instance(instance_id,region):
    ec2 = boto3.resource('ec2', region_name=region)
    instance = ec2.Instance(instance_id)
    instance.terminate()
    instance_state=get_instance_state(instance_id,region)
    while instance_state != 'terminated':
        time.sleep(10)
        instance_state=get_instance_state(instance_id,region)
    return "Instance {0} has Terminated!!!".format(instance_id)
