#AKIA25K3R5MWLD2WTWMM
import boto3
import sys
import os
import pandas as pd
import csv
import io
import mimetypes

s3 = boto3.resource('s3')
print(s3)
print(s3)
bucketname = ''
for bucket in s3.buckets.all():
    print(bucket.name)
    bucketname = bucket.name
    for file in bucket.objects.all():
        print(file.key)
        m = mimetypes.guess_type(file.key)
        print(m)




#s3_client =boto3.client('s3')
#s3_bucket_name='filename_prod'
#s3 = boto3.resource('s3',
 #                   aws_access_key_id= 'YOUR_ACCESS_KEY_ID',
 #                   aws_secret_access_key='YOUR_SECRET_ACCESS_KEY')


my_bucket=s3.Bucket(bucketname)
print(my_bucket)
obj = s3.Object(bucketname, "test.pdf")
data=obj.get()["Body"].read()
aaa = io.BytesIO(data)
#aaa.write(data)
#df.append(pd.read_csv(io.BytesIO(data), header=0, delimiter=",", low_memory=False))