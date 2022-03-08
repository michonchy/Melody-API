import json
import subprocess

# import requests

# import ffmpeg
def convert_movie_to_music(movie_path,music_path): 
    proc = subprocess.run(f'/opt/bin/ffmpeg -i "{movie_path}" -vn -ac 2 -ar 44100 -ab 256k -acodec libmp3lame -f mp3 "{music_path}"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    data = proc.stdout
    return data


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

    proc = subprocess.run('/opt/bin/ffmpeg -i "abc.3gpp" -vn -ac 2 -ar 44100 -ab 256k -acodec libmp3lame -f mp3 "変換後の音声ファイル名.mp3"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    data = proc.stdout


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

        

    return {
        "statusCode": 200,
        "body": json.dumps({
            "help":data
        }),
    }
