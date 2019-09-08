from pytest import mark


@mark.parametrize('num_web_drivers', [2])
def test_do_thing(web_drivers):
    assert len(web_drivers) == 2
