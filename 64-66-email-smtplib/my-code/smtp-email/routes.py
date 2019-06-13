from dotenv import load_dotenv
import os

load_dotenv()

client = os.getenv("CLIENT_ID")
secret = os.getenv("CLIENT_SECRET")


def printenvironment():
    print(f'The client id is: {client}.')
    print(f'The secret id is: {secret}.')


if __name__ == "__main__":
    printenvironment()