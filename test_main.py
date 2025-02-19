"""test_main.py"""

import pytest
from PageObjects.main import Automation
import conftest



url = "https://www.guvi.in/"

dashboard_url = "https://www.guvi.in/sign-in/"

title = "GUVI | Learn to code in your native language"

hari = Automation()

#POSITIVE TEST CASE : VALIDATE URL

def test_positive_url():
    test_url = "https://www.guvi.in/"
    assert url == test_url
    print(f"success: {test_url} is the valid URL")

# NEGATIVE TEST CASE : VALIDATE URL

def test_negative_url():
    test_url = "Google.in"
    assert url == test_url
    print(f"success: {test_url} is the invalid one")

#POSITIVE TEST CASE: VALIDATE TITLE OR NOT

def test_positive_title():
    test_title = "GUVI | Learn to code in your native language"
    assert title == test_title
    print(f"Success:{test_title} is valid title")

# NEGATIVE TEST CASE : VALIDATE TITLE OR NOT

def test_negative_title():
    test_title = "Google, makes faster everything"
    assert title == test_title
    print(f"success:{test_title} is not valid one")


