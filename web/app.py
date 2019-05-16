from bottle import route, run, template, request

from card_validator.validator import get_issuer


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/')
def test():
    return "Hello world"

@route('/validate')
def validate():
    cardNumber = request.query.get("cardNumber","").strip()
    if cardNumber:
        try:
            issuer = get_issuer(cardNumber)
            return "Issuer: {}".format(issuer)

        except ValueError:
            return "Your card number is invalid"

    return "I am card validator page"

run(host='localhost', port=8080)