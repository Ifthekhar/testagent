from pathlib import Path
import os

from env import load_env
from openai import OpenAI


def main() -> None:
    env_path = Path(__file__).resolve().parents[1] / ".env"
    load_env(path=env_path, key="OPENAI_API_KEY")

    # If MCP_SERVER_URL exists but is empty in the shell env, replace it from .env.
    if os.environ.get("MCP_SERVER_URL", "") == "":
        os.environ.pop("MCP_SERVER_URL", None)
    load_env(path=env_path, key="MCP_SERVER_URL")

    server_url = os.environ.get("MCP_SERVER_URL")
    if not server_url:
        raise RuntimeError("MCP_SERVER_URL is not set. Provide a public URL to your MCP HTTP server.")

    client = OpenAI()
    response = client.responses.create(
        model="gpt-4.1",
        input="Add two numbers 3 and 8",
        tools=[
            {
                "type": "mcp",
                "server_label": "add_server",
                "server_url": server_url,
                "allowed_tools": ["add"],
            }
        ],
        tool_choice="auto",
    )

    print(response.output_text)


if __name__ == "__main__":
    main()
