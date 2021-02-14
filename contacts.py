import json
import vobject

file = open('your_address_books.json')

data = json.load(file)
contacts=data['address_book']

vcf = ''
nContacts = 0 ;
for contact in contacts['address_book']:
    for contact_detail in contact['details']:
        
        vCard = vobject.vCard()
        isNameAdded = False
        
        if contact_detail['contact_point'].startswith('+'):
            vCard.add('FN').value = contact['name']
            isNameAdded = True
            vCard.add('TEL').value = contact_detail['contact_point']
            nContacts+=1
        
        if isNameAdded:
            vcf = vcf + vCard.serialize()

with open('contacts.vcf','w',newline='') as writer:
    writer.write(vcf)

print(nContacts,'contacts extracted and saved in contacts.vcf')