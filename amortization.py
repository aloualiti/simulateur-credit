print "Amortization shendule calculator - lets you estimate your monthly loan repayments."
c = input("{0:20} : ".format("Loan Amount"))
n = input("{0:20} : ".format("Loan Term in months"))
t = input("{0:20} : ".format("Interest Rate"))
t=float(t)
m=c*(t/1200)/(1-(1+t/1200)**-n)# طريقة الحساب من موقع wikipedia

print "{0:+<42}\n|{1:^41}|\n{0:+<42}".format("","Summary")
print "|{0:22} :{1:15} |".format("Monthly payement", round(m,2))
print "{0:-<42}".format("")
print "|{0:22} :{1:15} |".format("Total of payement", round(m *n,2))
print "{0:-<42}".format("")
print "|{0:22} :{1:15} |".format("Total of interest paid", round(m *n -c,2))
print "{0:+<42}\n".format("")

print "|{0:=<63}|".format("")
print "|{0:^15}|{1:^15}|{2:^15}|{3:^15}|".format("Periode","interest","Principal","Balance")
print "|{0:=<63}|".format("")

balance=c
for i in range(0,n):
    periode=i+1
    interest=balance*t/1200
    principal=m-interest
    balance-=principal
    print "|{0:^15}|{1:^15}|{2:^15}|{3:^15}|".format(periode,round(interest,2),round(principal,2),round(balance,2))
print "|{0:=<63}|".format("")



    





