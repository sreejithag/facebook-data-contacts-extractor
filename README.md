# Facebook Data Contacts Extractor

Recover lost contacts from contacts data collected by Facebook 
Extracts contacts as a vcf file from data downloaded from Facebook.

Facebook saves the phone contacts acquired from different services like WhatsApp and messenger.\
Data collected by Facebook can be downloaded in HTML or JSON formats.

## Usage 

* Head over to this [link](https://www.facebook.com/dyi/?referrer=yfi_settings)
* Select all date as 'all my data' format as 'JSON'
* Deselect and check only 'About You' (can select everything too but it will take a lot of time to generate file)
* Click on 'create file' and wait to get it generated.
* Download the zip file and extract it to get folder 'about_you' which contains 'your_address_books.json' having the contacts.
* Copy 'your_address_books.json' file to the location containing the python script.
* Install the requirements by `pip install -r requirements.txt`
* Run the script by `python contacts.py`
* 'contacts.vcf' file will be genarated

VCF file can be used to load the contacts back to any phone.


