from flask import render_template, request, redirect, url_for
from flask.ext.login import current_user
from werkzeug import secure_filename
from app import app
import string
import random
import os
import subprocess

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/contracten_company', methods=['GET', 'POST'])
def contracten_company():
    r_string = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
    if request.method == 'POST':
    # Get the name of the uploaded files
        name = request.form.getlist('name')[0]
        email = request.form.getlist('email')[0]
        uploaded_files = request.files.getlist("documents")
        filenames = []
        directory = os.path.join(app.config['UPLOAD_COMPANY_FOLDER'], name, r_string)
        if not os.path.exists(directory):
            os.makedirs(directory)
        for file in uploaded_files:
            # Check if the file is one of the allowed types/extensions
            if file and allowed_file(file.filename):
                # Make the filename safe, remove unsupported chars
                filename = secure_filename(file.filename)
                # Move the file form the temporal folder to the upload
                # folder we setup
                file.save(os.path.join(directory, filename))
                # Save the filename into a list, we'll use it later
                filenames.append(filename)
                # Redirect the user to the uploaded_file route, which
                # will basicaly show on the browser the uploaded file
        # Load an html page with a link to each uploaded file
        template = current_user.template1
        subprocess.Popen(['python', '/script', name, email, filenames[0], template], stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
        return render_template('index.html')
    return render_template('contracten_company.html')

@app.route('/contracten_lawyer', methods=['GET', 'POST'])
def contracten_lawyer():
    customer_query = current_user.followed.all()
    customers = []
    for customer_q in customer_query:
        customers.append(customer_q.name)
    r_string = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
    if request.method == 'POST':
    # Get the name of the uploaded files
        #name = request.form.getlist('name')[0]
        #email = request.form.getlist('email')[0]
        uploaded_files = request.files.getlist("documents")
        filenames = []
        directory = os.path.join(app.config['UPLOAD_LAWYER_FOLDER'], name, r_string)
        if not os.path.exists(directory):
            os.makedirs(directory)
        for file in uploaded_files:
            # Check if the file is one of the allowed types/extensions
            if file and allowed_file(file.filename):
                # Make the filename safe, remove unsupported chars
                filename = secure_filename(file.filename)
                # Move the file form the temporal folder to the upload
                # folder we setup
                file.save(os.path.join(directory, filename))
                # Save the filename into a list, we'll use it later
                filenames.append(filename)
                # Redirect the user to the uploaded_file route, which
                # will basicaly show on the browser the uploaded file
        # Load an html page with a link to each uploaded file
        subprocess.Popen(['touch', '/home/jens/datatatat'], stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
        return render_template('index.html')
    return render_template('contracten_lawyer.html', customers=customers)
