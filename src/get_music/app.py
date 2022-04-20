import json
import boto3

# import requests

# import ffmpeg
# def convert_movie_to_music(movie_path,music_path): 
#     # 入力
#     stream = ffmpeg.input(movie_path)
#     # 出力
#     stream = ffmpeg.output(stream,music_path) 
#     # 実行
#     ffmpeg.run(stream)

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
    s3 = boto3.resource('s3')
    bucket = s3.Bucket("melody-api-development-movie-contents")
    objects = bucket.objects.all()
    print(objects)
    keys = []
    for object in objects:
        if object.key.startswith("music/"):
            keys.append(object.key)
    
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,GET"
        },        
        "body": json.dumps({"musics":keys}),
    }
