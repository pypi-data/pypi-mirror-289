from typing import List, Tuple

from .cognito import LoginCognito
from .login import Login

Profiles: List[Tuple[str, Tuple[Login, Tuple]]] = [
    (
        "production",
        (
            LoginCognito,
            ("4s5hlfn2ckp381el2lqmvfg5b7", "USER_PASSWORD_AUTH", "us-east-1"),
        ),
    ),
    (
        "develop",
        (
            LoginCognito,
            ("728ps8a06bq01dvfsnctateqjr", "USER_PASSWORD_AUTH", "us-east-1"),
        ),
    ),
    (
        "digital-ecology",
        (
            LoginCognito,
            ("728ps8a06bq01dvfsnctateqjr", "USER_PASSWORD_AUTH", "us-east-1"),
        ),
    ),
]


def get_names() -> List[str]:
    return [name for name, _ in Profiles]


def get_login(profile_name: str) -> Login:
    cls, conf = dict(Profiles)[profile_name]
    return cls(*conf)
