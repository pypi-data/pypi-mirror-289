"""ChatGPT test"""

import psutil
import pytest
from selenium.webdriver.common.by import By
from talkingheads.model_library import ChatGPTClient

from utils import get_driver_arguments

def test_start():
    pytest.chathead = ChatGPTClient(**get_driver_arguments('chatgpt', incognito=True))
    assert pytest.chathead.ready, "The Client is not ready"


def test_interaction():
    response = pytest.chathead.interact(
        "Without any explanation or extra information, just repeat the following: book."
    )
    assert (
        "book" in response.lower()
    ), f'response is not "book.", instead it returned {response}'


def test_reset():
    assert pytest.chathead.reset_thread()
    assert (
        len(
            pytest.chathead.browser.find_elements(
                By.XPATH, pytest.chathead.markers.chatbox_xq
            )
        )
        == 0
    ), "Chat is not empty"


def test_regenerate():
    first_response = pytest.chathead.interact(
        "Without any explanation or extra information, type three animal names."
    ).lower()
    second_response = pytest.chathead.regenerate_response()
    assert first_response != second_response, "The regenerated response is the same."


def test_custom_interactions():
    mod_text = "Lorem ipsum dolor sit amet"
    info_text = "consectetur adipiscing elit"
    pytest.chathead.set_custom_instruction("modulation", mod_text)
    applied_mod_text = pytest.chathead.get_custom_instruction("modulation")
    assert (
        applied_mod_text == mod_text
    ), f"Modulation text is different: {applied_mod_text}"
    pytest.chathead.set_custom_instruction("extra_information", info_text)
    applied_extra_text = pytest.chathead.get_custom_instruction("extra_information")
    assert (
        applied_extra_text == info_text
    ), f"Info text is different {applied_extra_text}"


def test_delete_chathead():
    del pytest.chathead
    assert not any(
        "undetected_chromedriver" in p.name() for p in psutil.process_iter()
    ), "Undetected chromedriver exists"
