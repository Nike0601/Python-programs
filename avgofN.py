print "Enter no. of numbers:"
sum=0
n=input()
print "Enter " + str(n)+ " numbers:\n"
for i in range(0,n):
   a=float(input())
   sum=sum+a
avg=(sum)/float(n)
print "Average is: "+str(avg)
