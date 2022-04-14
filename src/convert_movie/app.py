import json
import subprocess
import boto3
from urllib.parse import unquote

# import requests

# import ffmpeg
def convert_movie_to_music(movie_path,music_path): 
    proc = subprocess.run(f'/opt/bin/ffmpeg -i "{movie_path}" -vn -ac 2 -ar 44100 -ab 256k -acodec libmp3lame -f mp3 "{music_path}"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    data = proc.stdout
    return data
def download_tmp_path(s3_key: str):
    return "/tmp/"+s3_key.split("/")[-1]

def change_file_extension(s3_key):
    filename = s3_key.split("/")[-1]
    filename_only = filename.split(".")[0]
    return filename_only+".mp3"

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    object = event["Records"][0]["s3"]["object"]
    key: str = object["key"]
    if key.endswith('.mp3'):
        return {
            "statusCode": 400,
            "body": "No event",
        }
    # [Macbook]ヴァンパイア.3gpp => [S3]ヴァンパイア.3gpp
    # ①
    # [S3]ヴァンパイア.3gpp が 音声なのか、動画なのか検証しないといけなくなる
    # [S3] movie/ が頭に付いてると動画として見做したい
    # ②
    # tmp/movie/ヴァンパイア.3gpp に保存させるのではなく tmp/ヴァンパイア.3gpp に変換してあげる

    unquote_key=unquote(object["key"])
    print("unquote_key:" + unquote_key)
    s3 = boto3.resource('s3')
    tmp=download_tmp_path(unquote_key) # tmp/ヴァンパイア.3gpp
    print("tmp:" + tmp)
    tmp_convert="/tmp/"+change_file_extension(unquote_key) # tmp/ヴァンパイア.mp3
    print("tmp_convert:" + tmp_convert)
    bucket = s3.Bucket("melody-api-development-movie-contents")
    result=bucket.download_file(unquote_key,tmp) # ダウンロードするときに、tmpはLambdaのパソコンのフォルダ
    print(f"result:${result}")
    data = convert_movie_to_music(tmp,tmp_convert)
    bucket.upload_file(tmp_convert,"music/"+change_file_extension(unquote_key))
    


    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e
    if event == None:
        return {
        "statusCode": 400,
        "body": "No event",
    }

        
    print(event)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "result":"success",
            "event":event
        }),
    }
