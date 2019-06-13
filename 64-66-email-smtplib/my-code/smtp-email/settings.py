# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

client = os.environ.get("CLIENT_ID")
secret = os.environ.get("CLIENT_SECRET")


def printenvironment():
    print(f'The client id is: {client}.')
    print(f'The secret id is: {secret}.')


if __name__ == "__main__":
    printenvironment()