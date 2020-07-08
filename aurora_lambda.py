import boto3
import os


client = boto3.client('rds-data')

def lambda_handler(event, context):
    response = client.execute_statement(
    continueAfterTimeout=True,
    database= ## INSERT Database Name ##,
    resourceArn= ## INSERT DB Cluster Arn Here ##,
    schema='',
    secretArn= ## INSERT secret Arn from Secret Manager Here ##,
    sql='SELECT * from tdojo_associate_courses')
    
    
    for record in response['records']:
        courses= record[0]['stringValue']
        description = record[1]['stringValue']
        print(f'Course: {courses} | Description: {description}')
