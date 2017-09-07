import random

def get_random_id():
    # generate a random unique integer to be used as ID
    random_id = random.randrange(1, 10000000)
    return random_id

#this method extracts class attributes and store in a dic for easier rendering of table in thml
def get_class_attributes(instance_of_class):
    members = [attr for attr in dir(instance_of_class) if
               not callable(getattr(instance_of_class, attr)) and not attr.startswith("__")]

    attributes_dict = dict()
    for member in members:
        attributes_dict[member] = getattr(instance_of_class, member)

    return attributes_dict

