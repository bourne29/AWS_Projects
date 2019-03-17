'''
This module is to list the EC2 Instances in different states.
For e.g.
1. Listing all the Instances.
2. Listing all the Instances in RUNNING state.
3. Listing all the Instances in PENDING state.
and so on ....
'''



#importing the boto3 module
import boto3

'''Function to list ALL the Instances in the region'''
def list_all_instances(region):
        # Creating an empty list my_list[]
        my_list=[]

        # creating an EC2 Client
        ec2_client = boto3.client('ec2',region_name=region)

        response = ec2_client.describe_instances()
        # response is a dict with two Keys: Reservations and ResponseMetadata
        # response: Reservations
        #           ResponseMetadata

        x_list=response['Reservations']
        # x_list is a list where each entry in the list is information about 1 instances
        # So if there are 6 instances in the Region, there will be 6 entries.
        #response: Reservations[Instance1,Instance2,Instance3,Instance4,Instance5,Instance6]
        #          ResponseMetadata

        # Now we iterate through every entry of that list which is a dict
        #response: Reservations[Instance1{Groups:Val1,Instances:[{AmiLaunchIndex:0,InstanceId': 'i-0d9eaf2d2f2e005f6'}]},Instance2,Instance3,Instance4,Instance5,Instance6]
        #          ResponseMetadata
        for alpha_dict in x_list:
            for instances in alpha_dict["Instances"]:
                my_list.append(instances["InstanceId"])

        return my_list


'''Function to list all the RUNNING Instances in the Region'''
def list_running_instances(region):
        # Creating an empty list my_running_list[]
        my_running_list=[]

        # creating an EC2 Client
        ec2_client = boto3.client('ec2',region_name=region)

        response = ec2_client.describe_instances(
            Filters=[
                {
                'Name':'instance-state-name',
                'Values':['running']
                }
            ]
        )
        # response is a dict with two Keys: Reservations and ResponseMetadata
        # response: Reservations
        #           ResponseMetadata


        # Now we iterate through every entry of that list which is a dict
        #response: Reservations[Instance1{Groups:Val1,Instances:[{AmiLaunchIndex:0,InstanceId': 'i-0d9eaf2d2f2e005f6'}]},Instance2,Instance3,Instance4,Instance5,Instance6]
        #          ResponseMetadata
        x_list=response['Reservations']
        # x_list is a list where each entry in the list is information about 1 instances
        # So if there are 6 instances in the Region, there will be 6 entries.
        #response: Reservations[Instance1,Instance2,Instance3,Instance4,Instance5,Instance6]
        #          ResponseMetadata

        for alpha_dict in x_list:
            for instances in alpha_dict["Instances"]:
                my_running_list.append(instances["InstanceId"])

        return my_running_list


'''Function to list all the PENDING Instances in the Region'''
def list_pending_instances(region):
        # Creating an empty list my_running_list[]
        my_pending_list=[]

        # creating an EC2 Client
        ec2_client = boto3.client('ec2',region_name=region)

        response = ec2_client.describe_instances(
            Filters=[
                {
                'Name':'instance-state-name',
                'Values':['pending']
                }
            ]
        )
        # response is a dict with two Keys: Reservations and ResponseMetadata
        # response: Reservations
        #           ResponseMetadata


        # Now we iterate through every entry of that list which is a dict
        #response: Reservations[Instance1{Groups:Val1,Instances:[{AmiLaunchIndex:0,InstanceId': 'i-0d9eaf2d2f2e005f6'}]},Instance2,Instance3,Instance4,Instance5,Instance6]
        #          ResponseMetadata
        x_list=response['Reservations']
        # x_list is a list where each entry in the list is information about 1 instances
        # So if there are 6 instances in the Region, there will be 6 entries.
        #response: Reservations[Instance1,Instance2,Instance3,Instance4,Instance5,Instance6]
        #          ResponseMetadata

        for alpha_dict in x_list:
            for instances in alpha_dict["Instances"]:
                my_pending_list.append(instances["InstanceId"])

        return my_pending_list



'''Function to list all the SHUTTING-DOWN Instances in the Region'''
def list_shutting_down_instances(region):
        # Creating an empty list my_running_list[]
        my_shutting_down_list=[]

        # creating an EC2 Client
        ec2_client = boto3.client('ec2',region_name=region)

        response = ec2_client.describe_instances(
            Filters=[
                {
                'Name':'instance-state-name',
                'Values':['shutting-down']
                }
            ]
        )
        # response is a dict with two Keys: Reservations and ResponseMetadata
        # response: Reservations
        #           ResponseMetadata


        # Now we iterate through every entry of that list which is a dict
        #response: Reservations[Instance1{Groups:Val1,Instances:[{AmiLaunchIndex:0,InstanceId': 'i-0d9eaf2d2f2e005f6'}]},Instance2,Instance3,Instance4,Instance5,Instance6]
        #          ResponseMetadata
        x_list=response['Reservations']
        # x_list is a list where each entry in the list is information about 1 instances
        # So if there are 6 instances in the Region, there will be 6 entries.
        #response: Reservations[Instance1,Instance2,Instance3,Instance4,Instance5,Instance6]
        #          ResponseMetadata

        for alpha_dict in x_list:
            for instances in alpha_dict["Instances"]:
                my_shutting_down_list.append(instances["InstanceId"])

        return my_shutting_down_list


'''Function to list all the TERMINATED Instances in the Region'''
def list_terminated_instances(region):
        # Creating an empty list my_running_list[]
        my_terminated_list=[]

        # creating an EC2 Client
        ec2_client = boto3.client('ec2',region_name=region)

        response = ec2_client.describe_instances(
            Filters=[
                {
                'Name':'instance-state-name',
                'Values':['terminated']
                }
            ]
        )
        # response is a dict with two Keys: Reservations and ResponseMetadata
        # response: Reservations
        #           ResponseMetadata


        # Now we iterate through every entry of that list which is a dict
        #response: Reservations[Instance1{Groups:Val1,Instances:[{AmiLaunchIndex:0,InstanceId': 'i-0d9eaf2d2f2e005f6'}]},Instance2,Instance3,Instance4,Instance5,Instance6]
        #          ResponseMetadata
        x_list=response['Reservations']
        # x_list is a list where each entry in the list is information about 1 instances
        # So if there are 6 instances in the Region, there will be 6 entries.
        #response: Reservations[Instance1,Instance2,Instance3,Instance4,Instance5,Instance6]
        #          ResponseMetadata

        for alpha_dict in x_list:
            for instances in alpha_dict["Instances"]:
                my_terminated_list.append(instances["InstanceId"])

        return my_terminated_list


'''Function to list all the STOPPING Instances in the Region'''
def list_stopping_instances(region):
        # Creating an empty list my_running_list[]
        my_stopping_list=[]

        # creating an EC2 Client
        ec2_client = boto3.client('ec2',region_name=region)

        response = ec2_client.describe_instances(
            Filters=[
                {
                'Name':'instance-state-name',
                'Values':['stopping']
                }
            ]
        )
        # response is a dict with two Keys: Reservations and ResponseMetadata
        # response: Reservations
        #           ResponseMetadata


        # Now we iterate through every entry of that list which is a dict
        #response: Reservations[Instance1{Groups:Val1,Instances:[{AmiLaunchIndex:0,InstanceId': 'i-0d9eaf2d2f2e005f6'}]},Instance2,Instance3,Instance4,Instance5,Instance6]
        #          ResponseMetadata
        x_list=response['Reservations']
        # x_list is a list where each entry in the list is information about 1 instances
        # So if there are 6 instances in the Region, there will be 6 entries.
        #response: Reservations[Instance1,Instance2,Instance3,Instance4,Instance5,Instance6]
        #          ResponseMetadata

        for alpha_dict in x_list:
            for instances in alpha_dict["Instances"]:
                my_stopping_list.append(instances["InstanceId"])

        return my_stopping_list


'''Function to list all the STOPPED Instances in the Region'''
def list_stopped_instances(region):
        # Creating an empty list my_running_list[]
        my_stopped_list=[]

        # creating an EC2 Client
        ec2_client = boto3.client('ec2',region_name=region)

        response = ec2_client.describe_instances(
            Filters=[
                {
                'Name':'instance-state-name',
                'Values':['stopped']
                }
            ]
        )
        # response is a dict with two Keys: Reservations and ResponseMetadata
        # response: Reservations
        #           ResponseMetadata


        # Now we iterate through every entry of that list which is a dict
        #response: Reservations[Instance1{Groups:Val1,Instances:[{AmiLaunchIndex:0,InstanceId': 'i-0d9eaf2d2f2e005f6'}]},Instance2,Instance3,Instance4,Instance5,Instance6]
        #          ResponseMetadata
        x_list=response['Reservations']
        # x_list is a list where each entry in the list is information about 1 instances
        # So if there are 6 instances in the Region, there will be 6 entries.
        #response: Reservations[Instance1,Instance2,Instance3,Instance4,Instance5,Instance6]
        #          ResponseMetadata

        for alpha_dict in x_list:
            for instances in alpha_dict["Instances"]:
                my_stopped_list.append(instances["InstanceId"])

        return my_stopped_list


if __name__ == '__main__':
    list_instances('us-east-1')
