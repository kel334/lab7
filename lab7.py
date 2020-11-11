# Kendra Ludwig (kel334)
# Dayra Quinonez (dq53)


# Create the dictionary for the program to store data in
def new_contact_store():
    return {}


# Create a nested dictionary, add contact information
# Uses key values for later reference
def add_new_contact(contacts, first_name, last_name,
                    email, phone_number, birthday):
    key = first_name + last_name
    contacts[key] = {"First Name": first_name,
                     "Last Name": last_name,
                     "Email": email,
                     "Phone Number": phone_number,
                     "Birthday": birthday
                     }
    return contacts


# Checks to see if the contact exists
def has_contact(contacts, first_name, last_name):
    key = first_name + last_name
    if key in contacts:
        return True
    else:
        return False


# Retrives the contact to check for the right input
def get_contact_string(contacts, first_name, last_name):
    key = first_name + last_name
    return contacts.get(key)


# This one removes the bad contacts
def remove_contact(contacts, first_name, last_name):
    key = first_name + last_name
    del contacts[key]
    return contacts


# Updates the first name with a new input
def update_contact_first_name(contacts, first_name,
                              last_name, new_field_value):
    key = first_name + last_name
    new_key = new_field_value + last_name
    contacts[key]["First Name"] = new_field_value
    contacts[new_key] = contacts[key]
    return contacts


# Updates the last name with a new input
def update_contact_last_name(contacts, first_name, last_name, new_field_value):
    key = first_name + last_name
    new_key = first_name + new_field_value
    contacts[key]["Last Name"] = new_field_value
    contacts[new_key] = contacts[key]
    return contacts


# Upates the email with a new input
def update_contact_email(contacts, first_name, last_name, new_field_value):
    key = first_name + last_name
    contacts[key]["Email"] = new_field_value
    return contacts


# Updates the phone number with a new input
def update_contact_phone_number(contacts, first_name,
                                last_name, new_field_value):
    key = first_name + last_name
    contacts[key]["Phone Number"] = new_field_value
    return contacts


# Updates the birthday with a new input
def update_contact_birthday(contacts, first_name, last_name, new_field_value):
    key = first_name + last_name
    contacts[key]["Birthday"] = new_field_value
    return contacts
