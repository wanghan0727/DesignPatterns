class Book:
    def purchaseWithCreditCard(self, creditCard):
        creditCard.processPayment()
        print("Purchased book")

    def purchaseWithLinePay(self, payPalAccount):
        payPalAccount.processPayment()
        print("Purchased book")

class Electronics:
    def purchaseWithCreditCard(self, creditCard):
        creditCard.processPayment()
        print("Purchased electronics")

    def purchaseWithLine(self, payPalAccount):
        payPalAccount.processPayment()
        print("Purchased electronics")

class CreditCardPayment:
    def processPayment(self):
        print("Processing credit card payment")

class LinePayPayment:
    def processPayment(self):
        print("Processing Line Pay payment")


if __name__ == '__main__':
    book = Book()
    electronics = Electronics()

    creditCardPayment = CreditCardPayment()
    linepayPayment = LinePayPayment()

    book.purchaseWithCreditCard(creditCardPayment)
    electronics.purchaseWithCreditCard(creditCardPayment)
    book.purchaseWithCreditCard(linepayPayment)
    electronics.purchaseWithCreditCard(linepayPayment)
