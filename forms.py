# forms.py

from wtforms import Form, StringField, SelectField, validators

class MNBIPOCSearchForm(Form):
    choices = [ ('race', 'Race'),
                ('gender', 'Gender'),
                ('language', 'Language')]
    select = SelectField('Search for providers according to:', choices=choices)
    search = StringField('')

class New_ProviderForm(Form):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    gender = StringField('Gender')
    race = StringField('Race')
    phone = StringField('Phone')
    email = StringField('Email')
    language = StringField('Language Spoken Other Than English')
    services = StringField('Services')
    clinic = StringField('Clinic Name')
    website = StringField('Website')