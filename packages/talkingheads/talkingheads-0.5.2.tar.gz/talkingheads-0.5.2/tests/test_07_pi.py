"""Pi test"""

import time
import psutil
import pytest
from talkingheads import PiClient
from utils import get_driver_arguments

def test_start():
    pytest.chathead = PiClient(**get_driver_arguments('pi', incognito=True))
    assert pytest.chathead.ready, "The Client is not ready"


def test_interaction():
    time.sleep(1)
    response = pytest.chathead.interact(
        "Without any explanation or extra information, just repeat the following: book."
    )
    assert (
        "book" in response.lower()
    ), f'response is not "book.", instead it returned {response}'

def test_reset():
    assert pytest.chathead.reset_thread(), "Failed to reset"

# def test_model_selection():
#     assert pytest.chathead.switch_model("SupportPi"), "Model switch failed."


def test_delete_chathead():
    del pytest.chathead
    time.sleep(1)
    assert not any(
        "undetected_chromedriver" in p.name() for p in psutil.process_iter()
    ), "Undetected chromedriver exists"
