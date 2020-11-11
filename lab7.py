# Kendra Ludwig (kel334)
# Dayra Quinonez (dq53)


def new_contact_store():
    return {}


def add_new_contact(contacts, first_name, last_name, email, phone_number, birthday):
    key = first_name + last_name
    contacts[key] = { "First Name" : first_name,
                      "Last Name" : last_name,
                      "Email" : email,
                      "Phone Number" : phone_number,
                      "Birthday" : birthday
                      }
    return contacts


def has_contact(contacts, first_name, last_name):
    key = first_name + last_name
    if key in contacts:
        return True
    else:
        return False


def get_contact_string(contacts, first_name, last_name):
    key = first_name + last_name
    return contacts.get(key)


def remove_contact(contacts, first_name, last_name):
    key = first_name + last_name
    del contacts[key]
    return contacts


def update_contact_first_name(contacts, first_name, last_name, new_field_value):
    key = first_name + last_name
    new_key = new_field_value + last_name
    contacts[key]["First Name"] = new_field_value
    contacts[new_key] = contacts[key]

    return contacts


def update_contact_last_name(contacts, first_name, last_name, new_field_value):
    key = first_name + last_name

    updated = contacts.update(last_name)
    return updated

def update_contact_email(contacts, first_name, last_name, new_field_value):
    key = first_name + last_name

    updated = contacts.update(email)
    return updated

def update_contact_phone_number(contacts, first_name, last_name, new_field_value):
    key = first_name + last_name

    phone_number = new_field_value
    updated = contacts.update(phone_number)
    return updated

def update_contact_birthday(contacts, first_name, last_name, new_field_value):
    key = first_name + last_name

    updated = contacts.update(birthday)
    return updated
