# komparasi (true false)
# > < >= <= == != is is-not
x = 25
y = 72

print ("========== lebih dari (>)")
hasil = x > 15
print (x, ">" , 70, "=", hasil)
hasil = x > 30
print (x, ">" , 30, "=", hasil)


print ("========== kurang dari (<)")
hasil = y < 89
print (y, "<", 89, "=", hasil)
hasil = y <  60
print (y, "<", 60, "=", hasil)


print ("========== lebih dari sama dengan (>=)")
hasil = x >= 72
print (x, ">=", 72, "=", hasil)
  
  
print ("========== kurang dari sama dengan (<=)")
hasil = y <= 25
print(y, "<=", 25, "=", hasil)

print ("========= sama dangan sama dengan (==)")
hasil = x == 72
print (x, "==", 72, "=", hasil)

print ("========== tidak sama dengan (!=)")
hasil = y != 25
print(y, "!=", 25, "=", hasil)

print ("========== is (is)")
hasil = x is 72
print(x, "is", 72, "=", hasil)

print ("========== is-not (is not)")
hasil = 25 is not y
print(25, "is-not", y, "is not", hasil)

