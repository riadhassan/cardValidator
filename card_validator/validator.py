def get_issuer(cardNumber: str) -> str :
    cardNumber = "".join(cardNumber.split())
    if cardNumber.startswith('4') and len(cardNumber) == 16:
        return 'Visa'

    if (cardNumber.startswith('34') or cardNumber.startswith('37')) and len(cardNumber) == 15:
        return 'American Express'

    masterCard_condation = (cardNumber.startswith('51') or cardNumber.startswith('52') or cardNumber.startswith(
        '53') or cardNumber.startswith('54') or cardNumber.startswith('55')) and len(cardNumber) == 16
    if masterCard_condation:
        return 'MasterCard'

    raise ValueError("Invalid Card Number")