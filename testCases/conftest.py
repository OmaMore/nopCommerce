from __future__ import annotations
from selenium import webdriver
import pytest




@pytest.fixture()
def setup_driver(browser):
    if browser == 'chrome':
        driver=webdriver.Chrome()
    elif browser== 'firefox':
        driver=webdriver.Firefox()
    else:
        driver=webdriver.Ie()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


################## pytest HTML Report Envoronment########

## it is hook for adding Environment info to HTML Report

def pytest_configure(config):
    config._metadata={'ProjectName':'nop commerce',
                      'ModuleName':'Customer',
                      'TesterName':'Chanchal'}


# it is hook for delete/ Modify Environment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)