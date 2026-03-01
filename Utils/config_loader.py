import yaml
import os


def load_config():

    try:
        with open("Config/config.yaml", "r") as f:
            config = yaml.safe_load(f)
        return config
    except FileNotFoundError:
        print("Config file not found.")
        return None

