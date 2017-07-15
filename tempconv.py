print "Enter input unit as Celsius/Fahrenheit: "
unit=raw_input()
if unit=="Celsius":
  print "Enter temperature in Celsius: "
  temp=float(input())
  temp_F=((9/5.0)*temp)+32
  print "Temperature in Fahrenheit is: "+str(temp_F)+"°F"
elif unit=="Fahrenheit":
  print "Enter temperature in Fahrenheit: "
  temp=float(input())
  temp_C=(temp-32)*(5/9.0)
  print "Temperature in Celcius is: "+str(temp_C)+"°C"
else:
  print "Invalid input. Enter input unit only as Celsius/Fahrenheit"

