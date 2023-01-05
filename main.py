####WE WILL BE USING STRING FUNCTION TO CREATE THIS EMAIL VALIDTAIOR #################
email = input('Enter Your Email : ')
 #  MIN LENGTH ODF EMAIL g@g.in 6 charachters #########
d,j,k = 0,0,0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    elif i == i.isalpha():
                        if i == i.upper():
                            j = 1                            
                    else:
                        d = 1
                if j==1 or k==1 or d==1:
                        print('Wrong Email')
                        
            else:
                print("Wrong Email , Characters After Point Not Satisfied")
        else:
            print('Wrong Email , There should Be Only One @ Operator')
            
    else:
        print("Worng Email , The First Letter Should Be An Alphabet")
        

else:
    print('Worng Email , Not Satisfying Minimun Words Requirements...')
    
