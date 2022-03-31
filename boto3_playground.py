import boto3

s3 = boto3.resource('s3')
s3.Bucket("music-converter-bucket").download_file("movie/ヴァンパイア.3gpp","ヴァンパイア.3gpp")