from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    first_name = Col('First Name')
    last_name = Col('Last Name')
    gender = Col('Gender')
    race = Col('Race')
    phone = Col('Phone')
    email = Col('Email')
    language = Col('Language')
    services = Col('Services')
    clinic = Col('Clinic Name')
    website = Col('Website')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))