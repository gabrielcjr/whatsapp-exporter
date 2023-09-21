from message import Message
from dataclasses import is_dataclass
import pytest



@pytest.fixture
def message():
    return Message("01/01/2000", "+55 11 99999-9999", "message test")

@pytest.fixture
def message_with_date_error():
    return Message("01/01/200", "+55 11 99999-9999", "message test")

@pytest.fixture
def message_with_phone_number_error():
    return Message("01/01/2000", "+55 11 99999-99990", "message test")

def test_if_is_a_dataclass():
    assert is_dataclass(Message) == True

def test_creating_message_instance(message):
    print(message)
    assert message.date == "01/01/2000"
    assert message.phone_number == "+55 11 99999-9999"
    assert message.text == "message test"

def test_creating_message_with_date_format_error(message_with_date_error):
    with pytest.raises(Exception) as assert_error:
        message_with_date_error.validate_date()
    assert assert_error.value.args[0] == "Date format is wrong"

def test_creating_message_with_phone_number_format_error(message_with_date_error):
    with pytest.raises(Exception) as assert_error:
        message_with_date_error.validate_phone_number()
    assert assert_error.value.args[0] == "Phone number format is wrong"

def test_changing_instance_values(message):
    with pytest.raises(Exception) as assert_error:
        message.date = "02/01/2000"
    assert assert_error.value.args[0] == "cannot assign to field 'date'"
    with pytest.raises(Exception) as assert_error:
        message.phone_number = "+55 11 99999-9991"
    assert assert_error.value.args[0] == "cannot assign to field 'phone_number'"
    with pytest.raises(Exception) as assert_error:
        message.text = "message test2"
    assert assert_error.value.args[0] == "cannot assign to field 'text'"