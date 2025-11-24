import json
contactList = []
with open('projects/mini-project-9/contacts.json', 'r') as contactFile:
    contacts = json.load(contactFile)
    print(contacts['contact1'])
    print(contacts['contact2'])