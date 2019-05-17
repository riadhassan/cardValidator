from bottle import route, run, template, request,view

from card_validator.validator import get_issuer


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/')
@view('index')
def test():
    return {
        "message": "Hello world"
    }

@route('/validate')
@view('validate')
def validate():
    cardNumber = request.query.get("cardNumber","").strip()
    if cardNumber:
        try:
            issuer = get_issuer(cardNumber)
            return {
               "cardNumber" : cardNumber, "issuer" : issuer, "message": "It is a {}".format(issuer)
            }

        except ValueError:
            return {
               "cardNumber" : "n/a", "issuer" : "n/a", "message": "Card number is invalid"
            }

    return {
         "cardNumber" : "n/a", "issuer" : "n/a","message" : "welcome to card validator"
    }

run(host='localhost', port=8080)