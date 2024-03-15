imp = float(input())
if 0 <= imp <= 2000:
    print('Isento')
elif 2000.01 <= imp <= 3000:
    print('R$ {:0.2f}'.format((imp - 2000) * 0.08))
elif 3000.01 <= imp <= 4500:
    print('R$ {:0.2f}'.format((1000 * 0.08) + ((imp - 3000) * 0.18)))
else:
    print('R$ {:0.2f}'.format((1000 * 0.08) + (1500 * 0.18) + ((imp - 4500) * 0.28)))
