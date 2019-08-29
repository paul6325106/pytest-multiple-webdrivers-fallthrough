from pytest import fixture

from selenium.webdriver import Firefox


@fixture(name='web_driver', scope='session')
def get_web_driver():
    web_driver = Firefox()
    yield web_driver
    web_driver.quit()


@fixture(name='web_driver_1', scope='session')
def get_web_driver_1(web_driver):
    return web_driver


@fixture(name='web_driver_2', scope='session')
def get_web_driver_2():
    web_driver = Firefox()
    yield web_driver
    web_driver.quit()
