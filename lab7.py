# Kendra Ludwig (kel334)
# Dayra Quinonez (dq53)


def new_contact_store():
    contacts = {}
    return contacts

def add_new_contact(contacts, first_name, last_name, email, phone_number, birthday):
    contacts[""] = first_name, last_name, email, phone_number, birthday


def has_contact(contacts, first_name, last_name):
    contacts.get(first_name)
    contacts.get(last_name)


def get_contact_string(contacts, first_name, last_name):
    contacts.get(first_name)
    contacts.get(last_name)


def remove_contact(contacts, first_name, last_name):
   contacts.remove(first_name)
   contacts.remove(last_name)


def update_contact_first_name(contacts, first_name, last_name, new_field_value):
   first_name = new_field_value
   contacts.update(first_name)
   return first_name

def update_contact_last_name(contacts, first_name, last_name, new_field_value):
   last_name = new_field_value
   contacts.update(last_name)
   return last_name

def update_contact_email(contacts, first_name, last_name, new_field_value):
   email = new_field_value
   contacts.update(email)
   return email

def update_contact_phone_number(contacts, first_name, last_name, new_field_value):
   phone_number = new_field_value
   contacts.update(phone_number)
   return phone_number
def update_contact_birthday(contacts, first_name, last_name, new_field_value):
   birthday = new_field_value
   contacts.update(birthday)
   return birthday
