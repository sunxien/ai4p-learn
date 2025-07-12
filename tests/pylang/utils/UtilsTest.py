from pylang.utils import Utils

def test_repeat_star():
    result = Utils.repeat_star(3)
    assert result == "***"