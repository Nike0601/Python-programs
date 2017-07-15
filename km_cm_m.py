print "Enter distance/length in km: "
l_km=float(input())
print "Do you want to convert to cm/m: "
unit=raw_input()
if unit=="cm":
  l_cm=(10**5)*l_km
  print "Length in cm is: "+str(l_cm)
elif unit=="m":
  l_m=(10**3)*l_km
  print "Length in m is: "+str(l_m)
else:
  print "Invalid input. Enter only cm or m"
