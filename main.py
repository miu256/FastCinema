from flask import Flask, render_template, request, redirect
from server import findCinema
from discoverTMDb import takeMovieImage
import datetime

lastUpdate = datetime.datetime(2000, 1, 1, 0, 0, 0)
imageURL = list()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, Nothing at this URL.', 404


@app.route('/findCinema', methods=['POST'])
def do_findCinema() -> str:
    nowLocation = request.form['nowLocation']
    if not nowLocation:
        return redirect("/")
    else:
        theCinema = findCinema(nowLocation)
        return render_template('results.html', theCinema=theCinema)


@app.route('/')
@app.route('/entry')
def entryPage() -> str:
    global imageURL, lastUpdate
    now = datetime.datetime.now()
    if now > lastUpdate + datetime.timedelta(weeks=1):
        lastUpdate = now
        imageURL = takeMovieImage(now)
    return render_template('entry.html', imageURL = imageURL)


if __name__ == '__main__':
    app.run(debug=True)
