from src.task4 import (
    parse_input,
    add_contact,
    change_contact,
    find_number_by_username,
    output_all_contacts,
)


def test_parse_input():
    assert parse_input("add John 12345") == ("add", "John", "12345")
    assert parse_input("  phone   Alice ") == ("phone", "Alice")


def test_add_contact():
    contacts = {}
    result = add_contact(["Alice", "12345"], contacts)
    assert result == "Contact added."
    assert contacts == {"Alice": "12345"}


def test_change_contact_existing():
    contacts = {"Bob": "11111"}
    result = change_contact(["Bob", "22222"], contacts)
    assert result == "Contact changed."
    assert contacts["Bob"] == "22222"


def test_change_contact_missing():
    contacts = {}
    result = change_contact(["Charlie", "33333"], contacts)
    assert (
        result
        == "There was no contact created for Charlie. Make sure \
            you added it before and you spell it right."
    )


def test_find_number_by_username_found():
    contacts = {"Daisy": "44444"}
    result = find_number_by_username(["Daisy"], contacts)
    assert result == "Phone number of Daisy: 44444."


def test_find_number_by_username_not_found():
    contacts = {}
    result = find_number_by_username(["Eve"], contacts)
    assert result == "There is not phone number saved for Eve."


def test_output_all_contacts_non_empty():
    contacts = {"Frank": "55555"}
    result = output_all_contacts(contacts)
    assert result == "Here's all added contacts:\n{'Frank': '55555'}."


def test_output_all_contacts_empty():
    contacts = {}
    result = output_all_contacts(contacts)
    assert result == "No contacts added so far."
