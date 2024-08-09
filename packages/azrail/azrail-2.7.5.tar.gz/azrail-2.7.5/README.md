# SocialAgent

A Python package for generating various user agents.

## Installation

You can install the package using pip:

```bash
pip install azrail

from azrail import azrail

def test_azrail():
    agent = azrail()
    print("Dalvik User Agent:", agent.dalvik())
    print("Chrome User Agent:", agent.chrome())
    print("Threads User Agent:", agent.threads())
    print("Facebook User Agent:", agent.facebook())
    print("Instagram User Agent:", agent.instagram())

if __name__ == "__main__":
    test_azrail()

