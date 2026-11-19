from unittest.mock import Mock
def test_side_effect_list():
    mock = Mock()
    mock.get_data.return_value = [1, 2]
    assert mock.get_data() == 1
    assert mock.get_data() == 2
    assert mock.get_data() == "C"
    print(mock.get_data())