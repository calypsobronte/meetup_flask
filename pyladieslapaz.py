from flask import Flask, render_template
pyladieslapaz = Flask(__name__)


@pyladieslapaz.route('/', strict_slashes=False)
def hola_mundo():
    comunidad = 'Pyladies la Paz'
    return 'Hola Mundo de {}'.format(comunidad)

@pyladieslapaz.route('/python/<text>', strict_slashes=False)
def python_view(text):
    return 'Python {}'.format(text).replace('_', ' ')

@pyladieslapaz.route('/template/', strict_slashes=False)
def my_template():
    return render_template('template.html')

if __name__ == '__main__':
    pyladieslapaz.run(host='0.0.0.0', port=80)
