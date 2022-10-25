while(1):
    secretPassword = "pineapple"
    passwordAttempt = input("Enter Password: ")
    if passwordAttempt == secretPassword:
        print("Vault Unlocked")
        break
    elif passwordAttempt != secretPassword:
        print("Vault Locked")


 
