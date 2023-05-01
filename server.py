from flask import Flask, render_template, url_for, request
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_database(data):
    with open("Advanced course/Webdevelopment/web server/database.txt", mode='a') as database:
        email = data["mailbox"]
        name = data["you"]
        message = data["messag"]
        file = database.write(f'\n{email}, {name}, {message}')


def write_to_csv(data):
    with open("Advanced course/Webdevelopment/web server/database.csv", mode='a', newline='') as database2:
        email = data["mailbox"]
        name = data["you"]
        message = data["messag"]
        writer = csv.writer(database2, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([email,name,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return "form submitted"
        except:
            return "did not save to database"
    else:
        return "something went wrong"
