def loose_change():
    dinero = 70
    cambio = dict.fromkeys(['nickels', 'pennies', 'dimes', 'quarters'], 0)

    Dinero = str(dinero)
    for monedas in Dinero:
        if dinero <= 0:
            print(cambio)
            return cambio


loose_change()


#     monedasde25 = 0
#     if dinero > 25:
#         monedasde25 += 1
#     print(monedasde25)


# loose_change(70)
