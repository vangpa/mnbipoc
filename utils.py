from models import MNBIPOC
from forms import New_ProviderForm
from db_setup import db_session

def add_to_db(filename):
    import xlrd
    loc = (filename)
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    for i in range(1, sheet.nrows):
        x = []
        for j in range(0, sheet.ncols):
            x.append(sheet.cell_value(i, j))

        print(x)

        mnbipoc = MNBIPOC()
        new_form = New_ProviderForm()
        new_form.first_name.data = x[0]
        new_form.last_name.data = x[1]
        new_form.gender.data = x[2]
        new_form.race.data = x[3]
        new_form.phone.data = x[4]
        new_form.email.data = x[5]
        new_form.language.data = x[6]
        new_form.services.data = x[7]
        new_form.clinic.data = x[8]
        new_form.website.data = x[9]

        save_changes(mnbipoc, new_form, new=True)

def save_changes(mnbipoc, form, new=True):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object

    mnbipoc.first_name = form.first_name.data
    mnbipoc.last_name = form.last_name.data
    mnbipoc.gender = form.gender.data
    mnbipoc.clinic = form.clinic.data
    mnbipoc.website = form.website.data
    mnbipoc.email = form.email.data
    mnbipoc.phone = form.phone.data
    mnbipoc.race = form.race.data
    mnbipoc.language = form.language.data
    mnbipoc.services = form.services.data

    if new:
        # Add the new provider to the database
    db_session.add(mnbipoc)
