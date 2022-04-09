import csv
from flask import Flask, render_template, url_for, request, redirect

app = Flask('__name__')


@app.route('/')
def my_home():
    '''
    Info: This function returns a index.html template
    '''
    return render_template('index.html')


@app.route('/<string:page>')
def html_page(page):
    '''
    Info: This function returns a html template
    '''
    return render_template(page)


def write_to_file(data):
    '''
    Info: Write Data to file
    '''
    with open('./database.txt', encoding="utf8", mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    '''
    Info: Write Data to csv file
    '''
    with open('./database.csv', newline='', encoding="utf8", mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',',
                                quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    '''
    Info: This function returns a reply to user on form submit
    '''
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # print(data)
            # write_to_file(data)
            write_to_csv(data)
            # return 'form submitted'
            return redirect('thankyou.html')
        except:
            return 'did not stored to database'
    else:
        return 'something went wrong'

# @app.route('/index.html')
# def index():
#     return render_template('index.html')


# @app.route('/about.html')
# def about():
#     return render_template('about.html')


# @app.route('/work.html')
# def work():
#     return render_template('work.html')


# @app.route('/works.html')
# def works():
#     return render_template('works.html')


# @app.route('/components.html')
# def Components():
#     return render_template('components.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
