import pywaves as pw

node  = "https://testnode1.wavesnodes.com"
chain = "testnet"

pw.setNode(node = node, chain = chain)


class onWaves:
    def __init__(self, privateKey):
        self.addr = pw.Address(privateKey = privateKey)

    def dataTransaction(self, data):
        """
        make dataTransaction using @data
        """
        return self.addr.dataTransaction(data)

    @staticmethod
    def fieldHTML2dataTrx(form, key, t):
        """
        return element {'type':@t, 'key':@key, 'value':@form[@key]}

        example:  f(request.form, 'identity', 'string')
        """

        # check if type boolean
        value = form[key] == "on" if (t=='boolean') else form[key]
        return {'type':t, 'key':key, 'value': value}
