import sys
first_time = 'true'
print "Type your code in and run it. I will process it."
print "Remeber to save! Hit enter when finished, then type in save to save."
name = raw_input("Before you begin, tell me what you would like your program to be named.")
def get_code():
   number = 0
   user_code = "user_code",number
   user_code = raw_input()
   if user_code == "save":
    sys.exit()
   else:
    if first_time == 'true':
     file = open(name,'a',0)
    file.write(user_code)
    file.write("""
""")
    get_code()
get_code()
