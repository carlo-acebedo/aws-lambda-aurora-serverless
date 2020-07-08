import boto3
import os


client = boto3.client('rds-data')

def lambda_handler(event, context):
    response = client.execute_statement(
    continueAfterTimeout=True,
    database='tutorialsdojo_db',
    resourceArn=os.environ['CLUSTER'],
    schema='',
    secretArn=os.environ['SECRET'],
    sql='SELECT * from tdojo_associate_courses')
    
    
    for record in response['records']:
        courses= record[0]['stringValue']
        description = record[1]['stringValue']
        print(f'Course: {courses} | Description: {description}')