from flask import render_template, request, redirect, url_for, flash
from flask.ext.login import current_user
from werkzeug import secure_filename
from app import app
import string
import random
import os
import subprocess

from .models import User

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
            if file:
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
        admin = User.query.filter_by(email=app.config['ADMINS'][0]).first()
        folder = os.path.join(app.config['TEMPORARY_FOLDER'], r_string)
        if not os.path.exists(folder):
            os.makedirs(folder)
        good = os.path.join(folder, 'good.txt')
        bad = os.path.join(folder, 'bad.txt')
        open(good,'w').write(admin.template3)
        open(bad,'w').write(admin.template2)
        command = ['python', '/home/jens/ccheck/checker/check.py', name, User.query.filter_by(email=app.config['ADMINS'][0]).first().name, email, os.path.join(app.config['UPLOAD_COMPANY_FOLDER'], name, r_string, filenames[0]), good, bad]
        subprocess.Popen(command, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
        flash('Upload successful, you will recieve an e-mail shortly', 'success')
        return redirect(url_for('contracten_company'))
    return render_template('contracten_company.html')

@app.route('/contracten_lawyer', methods=['GET', 'POST'])
def contracten_lawyer():
    if not User.query.filter_by(email=app.config['ADMINS'][0]).first().is_following(current_user) and not current_user.is_admin():
        return redirect(url_for('contracten_company'))
    files = {}
    if current_user.is_admin():
        customer_query = current_user.followed.all()
        customers = []
        for customer_q in customer_query:
            customers.append(customer_q.name)
        for customer in customers:
            folder = os.path.join(app.config['UPLOAD_LAWYER_FOLDER'], customer)
            try:
                files[customer] = sorted([f[:-11] for f in os.listdir(folder)],reverse=True)
            except FileNotFoundError:
                files[customer] = []
    else:
        customers = False
        try:
            files[current_user.name] = sorted([f[:-11] for f in os.listdir(os.path.join(app.config['UPLOAD_LAWYER_FOLDER'], current_user.name))],reverse=True)
        except FileNotFoundError:
            files[current_user.name] = []
    r_string = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
    if request.method == 'POST':
        customer = request.form.getlist('customer')
        if customer:
            customer = User.query.filter_by(name=customer[0]).first()
            name = customer.name
            email = customer.email
        else:
            name = current_user.name
            email = current_user.email
        uploaded_files = request.files.getlist("documents")
        filenames = []
        directory = os.path.join(app.config['UPLOAD_LAWYER_FOLDER'], name)
        if not os.path.exists(directory):
            os.makedirs(directory)
        for file in uploaded_files:
            # Check if the file is one of the allowed types/extensions
            if file:
                # Make the filename safe, remove unsupported chars
                filename = secure_filename(file.filename) + '-' + r_string
                # Move the file form the temporal folder to the upload
                # folder we setup
                file.save(os.path.join(directory, filename))
                # Save the filename into a list, we'll use it later
                filenames.append(filename)
                # Redirect the user to the uploaded_file route, which
                # will basicaly show on the browser the uploaded file
                admin = User.query.filter_by(email=app.config['ADMINS'][0]).first()
                folder = os.path.join(app.config['TEMPORARY_FOLDER'], r_string)
                if not os.path.exists(folder):
                    os.makedirs(folder)
                good = os.path.join(folder, 'good.txt')
                bad = os.path.join(folder, 'bad.txt')
                open(good,'w').write(admin.template3)
                open(bad,'w').write(admin.template2)
                command = ['python', '/home/jens/ccheck/checker/check.py', name, User.query.filter_by(email=app.config['ADMINS'][0]).first().name, email, os.path.join(directory, filename), good, bad]
                subprocess.Popen(command, stdout=subprocess.PIPE,
                                            stderr=subprocess.STDOUT)
        flash('Your files have been uploaded', 'success')
        return redirect(url_for('contracten_lawyer'))
    return render_template('contracten_lawyer.html', customers=customers, files=files)
