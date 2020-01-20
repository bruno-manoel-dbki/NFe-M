from nfelib.v4_00 import leiauteNFe as parser
import pandas as pd

nota = parser.parse("NFe550000032835 35191060642774000148550010000328351973074167.xml",True)


print(nota.infNFe.emit.CNPJ)


