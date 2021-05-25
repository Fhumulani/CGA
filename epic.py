import epics

p = epics.PV('bmag1q:put-I')

p.put(27.)

print(p.get())
