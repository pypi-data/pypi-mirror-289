from typing import TypedDict


class Info(TypedDict):
    productVersion: str


class Config(TypedDict):
    info: Info
