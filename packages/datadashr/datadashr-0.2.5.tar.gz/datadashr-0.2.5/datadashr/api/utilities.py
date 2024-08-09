import ollama
from openai import OpenAI
import platform

from ollama import Client as OllamaClient


def get_ollama_model_list(host: str = "http://localhost:11434") -> list:
    """
    Get the list of models.
    :return:
    """
    client = OllamaClient(host=host)
    return client.list()


def get_openai_model_list(api_key) -> list:
    """
    Get the list of models.
    :return:
    """
    client = OpenAI(
        # This is the default and can be omitted
        api_key=api_key,
    )
    return client.models.list()


def get_os() -> str:
    """
    Get the operating system.
    :return:
    """
    return platform.system()


def get_os_version() -> str:
    """
    Get the operating system version.
    :return:
    """
    return platform.version()


print(get_openai_model_list('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'))
