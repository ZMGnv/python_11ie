import os
os.remove('aste.txt')
if os.path.exists('kaste.txt'):
    os.rename('kasteas.txt')
else:
    print('Fails neeksistē!')