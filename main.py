from flask import Flask, render_template, request, url_for
from server import findCinema

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, Nothing at this URL.', 404


@app.route('/findCinema', methods=['POST'])
def do_findCinema() -> str:
    nowLocation = request.form['nowLocation']
    theCinema = findCinema(nowLocation)
    return render_template('results.html', theCinema=theCinema)


@app.route('/')
@app.route('/entry')
def entryPage() -> str:
    return render_template('entry.html')


app.run()
