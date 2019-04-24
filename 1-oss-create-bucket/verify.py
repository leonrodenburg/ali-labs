import sys
import oss2
import json
from colorama import Fore
from pathlib import Path


def verify(bucket_name):
    profile = _get_active_profile()

    try:
        auth = oss2.Auth(profile["access_key_id"], profile["access_key_secret"])
        endpoint = "https://oss-%s.aliyuncs.com" % (profile["region_id"])
        bucket = oss2.Bucket(auth, endpoint, bucket_name)
        file = bucket.get_object("file.txt").read()
        local_file = open('file.txt', 'rb').read()

        if str(file) == str(local_file):
            succeed("You successfully passed lab 2!")
        else:
            fail("Contents of file 'test.txt' in bucket do not match local file, please try again")
    except oss2.exceptions.RequestError:
        fail("Could not connect to the bucket, is the internet connection working?")
    except oss2.exceptions.AccessDenied:
        fail("Could not authenticate with the bucket, is the name correct?")
    except Exception as e:
        fail("An unknown error occurred while checking your bucket, please check all steps and try again")
        raise e

def succeed(msg):
    print(Fore.GREEN + msg)
    sys.exit(0)


def fail(msg):
    print(Fore.RED + msg)
    sys.exit(1)


def _get_active_profile():
    config = _get_config_file_contents()
    active_profile_name = config["current"]
    active_profile = next(
        filter(lambda p: p["name"] == active_profile_name, config["profiles"])
    )
    return active_profile


def _get_config_file_contents():
    home = Path.home()
    config_dir = home / ".aliyun"
    config_file = config_dir / "config.json"
    with config_file.open() as f:
        config = f.read()
    return json.loads(config)


if __name__ == "__main__":
    from colorama import init

    init()

    args = sys.argv
    if len(args) < 2:
        fail("Please specify your bucket name, like 'python.py verify my-bucket'")

    bucket_name = sys.argv[1]
    if bucket_name is None or len(bucket_name) < 1:
        fail("Please specify your bucket name, like 'python.py verify my-bucket'")

    verify(bucket_name)
