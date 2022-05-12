import io
import random

import boto3

s3 = boto3.resource('s3')

textractoct = boto3.client("textract")

response = textractoct.detect_document_text(
                        Document=
                        {'S3Object' : {'Bucket': 'textracttestbucket-denishadmin',
                                       'Name': 'ReadableTest.pdf'}})
                       # ClientRequestToken='AKIA25K3R5MWLD2WTWMM')

#jobid = response["JobId"]
#res = textractoct.get_document_text_detection(JobId=jobid)
#print(res)

#print(response)
for item in response["Blocks"]:
    if item["BlockType"] == "LINE":
        print(item["Text"])

