from pytest import fixture

from selenium.webdriver import Firefox


@fixture(name='web_driver', scope='session')
def get_web_driver():
    web_driver = Firefox()
    yield web_driver
    web_driver.quit()


@fixture(name='web_drivers', scope='function')
def get_web_drivers(web_driver, num_web_drivers):
    web_drivers = [web_driver]

    for n in range(1, num_web_drivers):
        web_drivers.append(Firefox())

    yield web_drivers

    for n in range(1, num_web_drivers):
        web_drivers[n].quit()
