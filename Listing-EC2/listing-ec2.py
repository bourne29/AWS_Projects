#importing the boto3 module
import boto3

# creating an EC2 Client
ec2_client = boto3.client('ec2')

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
    y_list=alpha_dict['Instances']
    print(y_list[0]['InstanceId'])
