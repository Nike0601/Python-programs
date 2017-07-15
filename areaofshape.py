print "Enter shape as rectangle/square/triangle: "
shape=raw_input()
if shape=="rectangle":
  print "Enter length: "
  l=int(input())
  print "Enter breadth: "
  b=int(input())
  area=l*b
  print "Area of rectangle is: "+ str(area)
elif shape=="square":
   print "Enter side: "
   a=int(input())
   area=a**2
   print "Area of square is: "+ str(area)
elif shape=="triangle":
  print "Enter base: "
  b=int(input())
  print "Enter height: "
  h=int(input())
  area=(b*h)/2
  print "Area of rectangle is: "+ str(area)
else:
  print "Invalid input"
