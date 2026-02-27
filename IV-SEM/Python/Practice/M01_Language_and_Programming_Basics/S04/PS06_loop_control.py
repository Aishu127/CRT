p1 = "abc123"
for i in range(3):
    p2 = input()
    if p1==p2:
        print("Login Successful")
        break
else:
    print("Account Locked")