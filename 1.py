name = (input("enter your name:"))
age = int(input("enter your age:"))
h = [165,170,150]#int(input("height(in cm):"))
w = [60,85,45]#int(input("weight(in kg):"))
for i in range(len(h)):
    h[i] = h[i]/100
    sqroot = pow(h[i],2)
    BMI = float(w[i]/sqroot)
    print("your BMi:",BMI)
    if BMI < 18.5: print("underweight")
    elif 18.5 <= BMI < 25:print("normal")
    elif 25 <= BMI < 30:print("overweight")
    else :print("obese")


