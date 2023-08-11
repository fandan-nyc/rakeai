from data_loader import DataLoader
from processor import Processor
from multiprocessing import Pool, Lock
from padelpy import from_smiles
import time
import multiprocessing as mp
import boto3
import json
import urllib.parse
import http.client
import os


import pandas as pd

def calc_descriptor(data):
    try:
        row = data[0]
        smile = data[1]
        print("start {}".format(row))
        start = time.time()
        bothSignal  = from_smiles(smile, descriptors = True, fingerprints =  True, timeout = 10, output_csv='/tmp/descriptors.csv')
        end = time.time()
        print("both {},{}".format(row, end - start))
        print("size:" + str(len(bothSignal)))
    except Exception as e:
        print(e)
        print("{},{}".format(row, "faild !"))

# def lambda_handler(event, context):
if __name__ == "__main__":
    event = json.loads("""{
  "Records": [
    {
      "eventVersion": "2.0",
      "eventSource": "aws:s3",
      "awsRegion": "us-east-1",
      "eventTime": "1970-01-01T00:00:00.000Z",
      "eventName": "ObjectCreated:Put",
      "userIdentity": {
        "principalId": "EXAMPLE"
      },
      "requestParameters": {
        "sourceIPAddress": "127.0.0.1"
      },
      "responseElements": {
        "x-amz-request-id": "EXAMPLE123456789",
        "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
      },
      "s3": {
        "s3SchemaVersion": "1.0",
        "configurationId": "testConfigRule",
        "bucket": {
          "name": "rake.tools-data",
          "ownerIdentity": {
            "principalId": "EXAMPLE"
          },
          "arn": "arn:aws:s3:::rake.tools-data"
        },
        "object": {
          "key": "raw-data%2Fraw_data.csv",
          "size": 1024,
          "eTag": "0123456789abcdef0123456789abcdef"
        }
      }
    }
  ]
}""")
    connection = http.client.HTTPConnection('www.google.com', 80, timeout=10)
    connection.request("GET", "/")
    response = connection.getresponse()
    print("Status: {} and reason: {}".format(response.status, response.reason))

    connection.close()

    os.chdir("/tmp")
    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    response = s3.get_object(Bucket=bucket, Key=key)
    print('/tmp/' + key)
    print(response)
    s3.download_file(bucket, key, '/tmp/test.csv')
    print(mp.cpu_count())
    print("1")
    x = DataLoader()
    x.loadData('/tmp/test.csv')
    y = x.getData()
    print("2")
    # processor = Processor(y)
    data_for_concurrency = []
    for row in range(len(y.index)):
        smile_str = y.loc[row]['SMILES']
        data_for_concurrency.append((row, smile_str))
    print("3")
    data_for_concurrency.reverse()
    #with Pool(2) as p:
    #   p.map(calc_descriptor, data_for_concurrency)
   
    calc_descriptor(data_for_concurrency[0])
    #calc_descriptor(data_for_concurrency[0])
