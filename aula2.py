import random
password = "abcdefghijklmnopqrstuvwxyzABCDEFGHYJKLMNOPQRSTUVWXYZ1234567890-=!@#$%¨&*()?[]"
passnum = int(input("quantos caracteres vc quer na sua senha?"))
pas = ""
for i in range(passnum):
    pas += random.choice(password)
print(pas)
