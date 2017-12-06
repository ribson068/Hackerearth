from __future__ import division
n=int(raw_input())
X=(raw_input()).split()
W=(raw_input()).split()
i=0
sum_X=0
sum_W=0
while i<n:
	sum_X=sum_X+(int(X[i])*int(W[i]))
	sum_W=sum_W+int(W[i])
	i=i+1
mystring = "%.1f" % (sum_X/sum_W)
print mystring