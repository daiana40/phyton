# hipoteca.py
# Ejercicio de hipoteca
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
pago_extra = 1000
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
total_pagado = 0.0
mes = 1

while saldo > 0:
    if mes < pago_extra_mes_comienzo or mes > pago_extra_mes_fin:
        pago_mensual_total = pago_mensual
    else:
        pago_mensual_total = pago_mensual + pago_extra

    if saldo < pago_mensual_total:        
        saldo = saldo * (1+tasa/12)
        pago_mensual_total = saldo
        saldo -= pago_mensual_total
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual_total
    
    total_pagado = total_pagado + pago_mensual_total

    print(mes,  round(total_pagado,2), round(saldo,2))
    mes += 1

print('Total pagado:', round(total_pagado, 2))
print('Meses:', mes-1)

