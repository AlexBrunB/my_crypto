from otp import OTP
import cmd


class Requireris(cmd.Cmd):
    def __init__(self, secret="tzrpkbkifasifqfrdfau6sytglad6s6y", account="alexandrebrunepitech@gmail.com"):
        cmd.Cmd.__init__(self)
        self.secret = secret
        self.account = account
        self.counter = 1
    
    def do_geturl(self, line):
        """geturl authtype(hotp/totp) """
        if not line or len(line.split()) < 1:
            print ("Wrong")
        else:
            auth = line.split()[0]
            if auth != "hotp" and auth != "totp":
                print("Wrong auth param")
            else:
                print ("Type this in browser : ", OTP.get_url(self.account, auth, self.secret))
                
    def do_setAccount(self, line):
        "setAccount Account"
        if not line:
            print ("FUCKOFF")
        else:
            self.account = line.split()[0]
            self.counter = 1

    def do_setKey(self, line):
        "setKey KEY(encoded base32)"
        if not line:
            print ("Arrete stp")
        else:
            self.secret = line.split()[0]
            self.counter = 1
    def do_getTOTP(self, line):
        "getTOTP [digits]"
        digits = 6
        if line:
            digits = int(line.split()[0])
        print ("Your TOTP code : ", OTP.generate_totp(self.secret, digits))
        
    def do_getHOTP(self, line):
        "getHOTP [digits]"
        digits = 6
        if line:
            digits = int(line.split()[0])
        print ("Your HOTP code : ", OTP.generate_hotp(self.secret, self.counter, digits))
        self.counter += 1
    
    def do_exit(self, line):
        return True
#     def do_EOF(self, line):
#         return True
    
req = Requireris()
req.cmdloop()
    
# print("mon compte(totp): ", OTP.generate_totp("WR3SRWSNI2L3ZW76MMHOGUYBPBJOI62V"))
# print("mon compte(hotp): ", OTP.generate_hotp("WR3SRWSNI2L3ZW76MMHOGUYBPBJOI62V", 3))
# 
# print (OTP.get_url("alexandrebrunepitech@gmail.com", "hotp"))
