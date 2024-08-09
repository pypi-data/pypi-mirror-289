#!/usr/bin/env python3
from argparse import ArgumentParser
from ..auth.types import KMSBearerAuth, MAX_KMS_EXPIRATION_WINDOW

parser = ArgumentParser(description="Get a KMS token to use for registry authentication.")
parser.add_argument("cmd", type=str, help="The command to run.", choices=["token", "config", "env"])
parser.add_argument("--key-id", "-k",  type=str, required=True, help="The KMS key ID to use for token generation.")
parser.add_argument("--time", "-t", type=int, default=MAX_KMS_EXPIRATION_WINDOW, help="The time in seconds until the token expires.")
parser.add_argument("--host", "-H", type=str, help="The hostname of the registry.")
args = parser.parse_args()


def make_token():
    token = KMSBearerAuth.make_token(
        key_id=args.key_id,
        expiration_seconds=args.time
    )

    return token

def make_env_var():
    if not args.host:
        print("No host provided. Specify with the --host/-h flag.")
        exit(1)
    token = make_token()
    hostname = args.host.replace(".", "_").replace("-", "__").lower()
    var = f"TF_TOKEN_{hostname}=\"{token}\""

    return var


def make_config():
    if not args.host:
        print("No host provided. Specify with the --host/-h flag.")
        exit(1)

    token = make_token()
    config = f"""
credentials "{args.host}" {{
    token = "{token}"
}}
""" 
    return config

def main():
    if args.cmd == "token":
        print(make_token())
    elif args.cmd == "config":
        print(make_config())
    elif args.cmd == "env":
        print(make_env_var())

if __name__ == "__main__":
    main()