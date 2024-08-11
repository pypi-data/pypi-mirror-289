import os

from dotenv import load_dotenv

load_dotenv()


def get_env_variable(name, default):
    return os.getenv(name, default)


# Use production servers as fallbacks
WEB_SERVER_URL = get_env_variable("WEB_SERVER_URL", "https://digifoam.ai")
CLI_PROXY_SERVER_URL = get_env_variable(
    "CLI_PROXY_SERVER_URL", "https://digifoam-cli-server.up.railway.app"
)
