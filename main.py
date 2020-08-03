# main.py

from app import app
from db_setup import init_db, db_session
from forms import MNBIPOCSearchForm, New_ProviderForm
from flask import flash, render_template, request, redirect
from models import MNBIPOC
from tables import Results
from utils import save_changes

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    search = MNBIPOCSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    print(os.getcwd())
    return render_template('index.html', form=search)


@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    #print("Search string: {}".format(search_string))

    if search_string:
        print("Select statement: {}".format(search.data['select']))
        if search.data['select'] == 'race':
            #print("I am inside search string")
            qry = db_session.query(MNBIPOC).filter(
                MNBIPOC.race.contains(search_string))
            #print(qry.all())
            results = qry.all()
        elif search.data['select'] == 'gender':
            qry = db_session.query(MNBIPOC).filter(
                MNBIPOC.gender.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'language':
            qry = db_session.query(MNBIPOC).filter(
                MNBIPOC.language.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'services':
            qry = db_session.query(MNBIPOC).filter(
                MNBIPOC.services.contains(search_string))
            results = qry.all()
    else:
        qry = db_session.query(MNBIPOC)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)


@app.route('/new_provider', methods=['GET', 'POST'])
def new_provider():
    """
    Add a new provider
    """
    form = New_ProviderForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the provider
        mnbipoc = MNBIPOC()
        save_changes(mnbipoc, form, new=True)
        flash('Provider created successfully!')
        return redirect('/')

    return render_template('new_provider.html', form=form)

@app.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    qry = db_session.query(MNBIPOC).filter(
                MNBIPOC.id==id)
    mnbipoc = qry.first()

    if mnbipoc:
        form = New_ProviderForm(formdata=request.form, obj=mnbipoc)
        if request.method == 'POST' and form.validate():
            # save edits
            save_changes(mnbipoc, form)
            flash('Provider updated successfully!')
            return redirect('/')
        return render_template('edit_provider.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    """
    Delete the item in the databa se that matches the specified
    id in the URL
    """
    print("Inside delete function")
    qry = db_session.query(MNBIPOC).filter(
        MNBIPOC.id==id)
    mnbipoc = qry.first()

    if mnbipoc:
        db_session.delete(mnbipoc)
        db_session.commit()

        flash('Provider deleted successfully!')
        return redirect('/')
        return render_template('delete_provider.html', form=form)
    else:
        return 'Error deleting #{id}'.format(id=id)

if __name__ == '__main__':
    import os
    if 'WINGDB_ACTIVE' in os.environ:
        app.debug = False
    app.run(port=5001)
