from pytest import fixture

from selenium.webdriver import Firefox

max_web_drivers = 3


@fixture(name='preallocated_web_drivers', scope='session')
def get_preallocated_web_drivers():
    web_drivers = [Firefox() for n in range(max_web_drivers)]

    yield web_drivers

    [web_driver.quit() for web_driver in web_drivers]


@fixture(name='web_driver', scope='function')
def get_web_driver(preallocated_web_drivers):
    return preallocated_web_drivers[0]


@fixture(name='web_drivers', scope='function')
def get_web_drivers(preallocated_web_drivers, num_web_drivers):
    if num_web_drivers > len(preallocated_web_drivers):
        raise ValueError(f'Too many web drivers requested for test, maximum is {max_web_drivers}')

    return preallocated_web_drivers[:num_web_drivers]
