def main():
    welc = " welcom the the email spliter program "
    

    print(f"{welc:*^88}")
    print("")

    email_input = input("enter your email : ")
    (username, domain) = email_input.split("@")
    (domain, com) = domain.split(".")
    

    print(f"username is : {username}")
    print(f"domain is :{domain}")
    print(f"extintion is : {com}")

main()
