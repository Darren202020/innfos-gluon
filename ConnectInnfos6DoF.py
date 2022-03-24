import sys
sys.path.append('home/pi/')

import innfos

statusg = innfos.handshake()
data = innfos.queryID(6)

if statusg ==1:
    print('Connection is ok')
else:
    print('Connectino is failed')

print(data)




        
