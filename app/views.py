"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, jsonify, send_file, redirect, send_from_directory, url_for, flash
from werkzeug.utils import secure_filename
import os, datetime
from app.models import Movie
from app.forms import MovieForm


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/v1/movies', methods=['POST'])
def movies():
     # Instantiate form class
    movieform = MovieForm()
    movies_folder = app.config['UPLOAD_FOLDER']
    successmsg = 'Successfully added new movie'

    if request.method == 'POST':
        
        # Validate file upload on submit
        if movieform.validate_on_submit():
            poster = movieform.poster.data
            filename = secure_filename(poster.filename)
            poster.save(os.path.join(movies_folder, filename))

            movie = Movie(
                title=movieform.title.data,
                description=movieform.description.data,
                poster=filename,
                created_at=datetime.datetime.now()
            )

            db.session.add(movie)
            db.session.commit()

            flash('Movie Added', 'success')

            return jsonify(message=successmsg)
        return jsonify(errors=form_errors(movieform))
        


###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404