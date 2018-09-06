class User:
    ID = 'default'
    __password = '000000'
    count = 0

    def setpassword(self, pswd):
        self.__password = pswd

    def setID(self, id):
        self.ID = id

    def checkPassword(self, pswd):
        if pswd == self.__password:
            self.count = 0
            print('Login Successful~')
            return 1
        else:
            self.count += 1
            print('Wrong Password!')
            return 0


user = {}

userinfo = open("user.txt", 'r')
password = {}
for i in userinfo.readlines():
    userid = i.split()[0]
    user['%s' % userid] = User()
    user['%s' % userid].setID(userid)
    passwd = i.split()[1]
    user['%s' % userid].setpassword(passwd)
    password[userid] = passwd
userinfo.close()

blacklist = {}
count = 0
test = open('blacklist.txt', 'r')
for i in test.readlines():
    x1 = i.split('\n')[0]
    blacklist[x1] = x1
test.close()
username = 'default'
while (1):
    while user[username].count < 3:
        username = input('Please input your ID: ')
        if username not in user.keys():
            print("User doesn't exist！\n")
            username = 'default'
            continue
        elif username in blacklist.keys():
            print("This user has been blocked!\n")
        else:
            pwd = input('Please input your password: ')
            flag = user[username].checkPassword(pwd)
            if flag == 1:
                break
            else:
                continue
    if user[username].count >= 3:
        blacklist[username] = '%s' % username
        print('You are blocked!\n')
        bl = open("blacklist.txt", 'a+')
        bl.write(username + '\n')
        break
