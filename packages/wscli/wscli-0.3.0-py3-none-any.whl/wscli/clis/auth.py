from dataclasses import asdict, dataclass
from typing import ClassVar

import click
from pydantic import TypeAdapter

from wscli.auth import SigninDetails
from wscli.auth.cognito import AwsRegion, LoginCognito
from wscli.auth.keycloak import LoginKeyCloak
from wscli.auth.profiles import get_login, get_names
from wscli.config import WsConfig, pass_config
from wscli.utils import pprint, yprint


@dataclass
class AuthConfig:
    login_handler: LoginCognito | LoginKeyCloak | None = None
    enabled: bool = False  # if disabled this will ignore logins
    Key_: ClassVar[str] = "auth"


pass_auth = click.make_pass_decorator(
    AuthConfig,
    ensure=True,
)


@click.group()
@click.pass_context
@pass_config
def cli(config: WsConfig, context: click.Context):
    adapter = TypeAdapter(AuthConfig)
    try:
        context.obj = adapter.validate_python(
            config.storer.get_key(AuthConfig.Key_)
        )
    except TypeError as err:
        click.echo(
            f"error loading the store key '{AuthConfig.Key_}'\n"
            f"Error:\n    {err}\n"
            "please use the wscli config commands to fix the issue"
        )
        raise click.Abort()


@cli.group()
def configure():
    """Configure the cli auth"""
    pass


@configure.command()
@click.option("--client-id", prompt=True)
@click.option("--region", default="us-east-1")
@click.option("--enabled/--not-enabled", default=True)
@pass_config
@pass_auth
def cognito(
    auth: AuthConfig,
    config: WsConfig,
    client_id: str,
    region: AwsRegion = "us-east-1",
    enabled: bool = True,
):
    """
    Set your client_id for cognito
    """
    config.login = None
    config.store()
    adapter = TypeAdapter(AuthConfig)
    auth.login_handler = LoginCognito(
        client_id=client_id,
        aws_region=region,
    )
    auth.enabled = enabled
    config.storer.set_key(auth.Key_, adapter.dump_python(auth))


@configure.command()
@pass_config
@pass_auth
def keycloak(auth: AuthConfig, config: WsConfig):
    """
    Set your client_id for cognito
    """
    click.echo("keycloack not implemented yet...")
    raise click.Abort


@configure.command()
@click.argument("name", type=click.Choice(get_names()))
@click.option("--enabled/--not-enabled", default=True)
@pass_config
@pass_auth
def set_profile(
    auth: AuthConfig, config: WsConfig, name: str, enabled: bool = True
):
    """
    Set your client_id for cognito
    """
    config.login = None
    config.store()
    adapter = TypeAdapter(AuthConfig)
    auth.login_handler = get_login(name)
    auth.enabled = enabled
    config.storer.set_key(auth.Key_, adapter.dump_python(auth))


@configure.command()
def profiles():
    click.echo(pprint(get_names()))


@configure.command()
@pass_auth
def show(auth):
    """print the auth configuration"""
    click.echo(pprint(asdict(auth)))


@cli.command()
@click.option("--username", prompt=True)
@click.option("--code", prompt=True)
@pass_auth
def confirm(auth: AuthConfig, username: str, code: str):
    """signup confirmation using the code"""
    click.echo(f"sign up confirm {auth}, {code} not implemented")
    raise click.Abort


@cli.command()
@click.option("--username", prompt=True)
@pass_auth
def reset(auth: AuthConfig, username: str):
    """request a password reset"""
    click.echo("password reset...")
    raise click.Abort


@cli.command()
@click.option("--username", prompt=True)
@click.option("--password", prompt=True, hide_input=True)
@pass_config
@pass_auth
def login(
    login_config: AuthConfig, config: WsConfig, username: str, password: str
):
    """login into the WS platform"""
    if login_config.login_handler is None:
        click.echo(
            "Your Login Details have not been Set. Please reset your client id"
        )
        raise click.Abort
    click.echo("logging in...")
    click.echo(f"username: {username}")
    click.echo("Fetching Token")
    config.login = login_config.login_handler.login(
        SigninDetails(username=username, password=password)
    )
    config.store()
    click.echo("Token updated")


@cli.command()
@pass_config
def logout(config: WsConfig):
    config.login = None
    config.store()


@cli.command()
@pass_config
@pass_auth
def refresh(login_config: AuthConfig, config: WsConfig):
    """refresh your id token"""
    click.echo("refresh logging...")
    config.login = login_config.login_handler.refresh(config.login)
    config.store()
    click.echo("Id Token has been refreshed")


@cli.command(name="show")
@click.option("--no-claims", is_flag=True, default=False)
@click.option("--value", is_flag=True, default=False)
@click.option("--remaining", is_flag=True, default=False)
@pass_config
def show_token(
    config: WsConfig,
    no_claims: bool = True,
    value: bool = False,
    remaining: bool = False,
):
    """show the current claims"""
    if config.login is None:
        click.echo("no login available!")
        raise click.Abort
    token = config.login.access_token
    if not token:
        click.echo("No token available!")
        raise click.Abort
    out_data = {"valid": bool(token.is_valid)}
    if remaining:
        out_data["remaining"] = int(token.remaining)
    if not no_claims:
        out_data["claims"] = token.claims
    if value:
        out_data["value"] = str(token.value)
    click.echo(yprint(out_data))
