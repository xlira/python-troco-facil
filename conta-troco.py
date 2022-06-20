from decimal import Decimal

valores = (0.01, 0.05, 0.10, 0.25, 0.50, 1, 2, 5, 10, 20, 50, 100) #tuple to specific the value cedules#
i = len(valores) - 1
valoresd = Decimal(valores[i])



valor = Decimal(input ("Qual o valor da compra?"))
pago = Decimal(input ("Qual o valor pago?"))
trocosrt = pago - valor
troco = Decimal(trocosrt)
sobra = 0
troco_total = 0

print(type(valoresd))
print(troco_total)
#print(i)
#print(valores[i])
while (troco > 0.00):
    if troco / valores[i] >= 1.00:
        sobra = troco / valores[i]
        sobra = int(sobra)
        troco = troco - (sobra * valores [i])
        troco_total = troco
        print(troco)
        i = i - 1
    else:
        i = i - 1








