import yaml
from appium import webdriver


def read_config(path):
    with open(path, 'r', encoding='utf-8') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config


def read_locator(path):
    with open(path, 'r', encoding='utf-8') as f:
        locator = yaml.load(f, Loader=yaml.FullLoader)
    return locator


