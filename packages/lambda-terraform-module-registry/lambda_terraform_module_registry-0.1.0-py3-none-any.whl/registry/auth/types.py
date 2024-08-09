#!/usr/bin/env python3
from hashlib import sha256
from os import environ
from random import choice
from string import ascii_letters, digits

from boto3 import resource


TABLE_NAME = environ.get("TABLE_NAME", "terraform-modules")
TABLE = resource("dynamodb").Table(TABLE_NAME) 


class BearerAuth:
    min_token_length = 64

    def __init__(self, token: str, tenant: str):
        if token < self.min_token_length:
            raise ValueError(f"Token must be at least {self.min_token_length} characters long")

        self.token = token
        self.tenant = tenant
        self.hash = sha256(self.token.encode()).hexdigest()


    @classmethod
    def make_token(cls):
        letters = ascii_letters + digits
        return "".join(choice(letters) for _ in range(cls.min_token_length))


    def get_db_key(self):
        key = {
            "pk": self.tenant,
            "sk": f"BEARERAUTH~{self.hash}"
        }

        return key


    def make_item(self, permissions: dict[str, dict] = {}):
        key = self.get_db_key()
        item = {
            **key,
            "tenant": self.tenant,
            "hash": self.hash,
            "permissions": permissions
        }

        return item


    @property
    def item(self):
        key = self.get_db_key()
        try:
            res = TABLE.get_item(Key=key).get("Item")
        except TABLE.meta.client.exceptions.ResourceNotFoundException:
            res = None

        if res is None:
            res = self.make_item()

        return res


    def put(self, permissions: dict[str, dict] = {}):
        item = self.item
        perms = {}

        for namespace, ns_perms in permissions.items():
            perm = {
                "download": ns_perms.get("download", False),
                "upload": ns_perms.get("upload", False)
            }
            perms[namespace] = perm           

        item = self.make_item(permissions=perms)
        print(item)
        TABLE.put_item(Item=item)
        return self.item

    @property
    def permissions(self):
        return self.item.get("permissions", {})

    def can_download(self, namespace: str):
        return self.item.get("permissions", {}).get(namespace, {}).get("download", False)

    def can_upload(self, namespace: str):
        return self.item.get("permissions", {}).get(namespace, {}).get("upload", False)


    @property
    def namespaces(self):
        return list(self.permissions.keys())


if __name__ == "__main__":
    auth = BearerAuth(
        token="test-token",
        tenant="hh"
    )
    auth.put({
        "seciam": {
            "download": True,
            "upload": False
        }
    })
    print(auth.can_download("seciam"))