import re # imports regex module

email_conditions = "^[a-z] + [\._]?[a-z 0-9] + [@]\w + [.]\w{2,3}$" 
#  here \ defines that we are giving charachters.. 
#  ? defines that we want only one charachter
#  \w used for special charchters
#  $ sign is used to search from the back and {2,3} is the position at we want the dot to be present
useremail = input(' Enter Your Email :')