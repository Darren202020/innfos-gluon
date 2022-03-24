import innfos
import time

actuID = [0x01, 0x02, 0x03, 0x04, 0x05]

statusg = innfos.handshake()
data = innfos.queryID(6)

innfos.enableact(actuID)
time.sleep(2)

# tempature = innfos.readacttemp(actuID)
# print(tempature)
# time.sleep(1)

nowpos = innfos.readpos(actuID)
print(nowpos)
time.sleep(2)

innfos.trapposmode(actuID) #梯形模式
limitpos = innfos.readposlimit(actuID) #讀取極限位置設置
print(limitpos)


# innfos.disableact(actuID)