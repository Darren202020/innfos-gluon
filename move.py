import innfos
import time

actuID = [0x01, 0x02, 0x03, 0x04, 0x05]


innfos.setpos(actuID, [-10, -12, -15, -15, 0])
time.sleep(1)

nowpos = innfos.readpos(actuID)
print(nowpos)
time.sleep(2)


# innfos.setpos(actuID, [10, -11, -15, -14, 0])

# innfos.setpos(actuID, [10, -11, 0, 0, -5])
# time.sleep(1)

# innfos.setpos(actuID, [0, -0, -0, 0, 0, 0])
# time.sleep(1)

# innfos.setpos(actuID, [0.0, 3, 2.0, 1.0, 2.0, -0.00396728515625])
# time.sleep(1)

# innfos.setpos(actuID, [5.0, 3, 2.0, 1.0, 2.0, -0.00396728515625])
# time.sleep(1)

# innfos.setpos(actuID, [-5.0, 3, 2.0, 1.0, 2.0, -0.00396728515625])
# time.sleep(1)

# innfos.setpos(actuID, [5.0, 3, 2.0, 1.0, 2.0, -0.00396728515625])
# time.sleep(1)

# innfos.setpos(actuID, [-5.0, -3, 2.0, 1.0, 2.0, -0.00396728515625])
# time.sleep(1)

# innfos.setpos(actuID, [5.0, 3, 2.0, 1.0, 2.0, -0.00396728515625])
# time.sleep(1)


