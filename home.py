import innfos
import time

actuID = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06]

innfos.setpos(actuID, [0, 12, 15, 0, 0])
time.sleep(1)






nowpos = innfos.readpos(actuID)
print(nowpos)
time.sleep(2)

# innfos.setpos(actuID, [0, 12, 15, 15, 10, 0])
# time.sleep(1)