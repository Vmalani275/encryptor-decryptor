class encryptor:
    def __init__(self,choice):
        self.choice=choice
    def main(self):
        if self.choice=="1":
            file=open("orgdata.txt","w")
            data=input("enter your data:")
            file.write(data)
            file.close()
        elif self.choice=="2":
            filename=input("enter the filename to be encrytped")
            file=open(filename,"r")
            data=file.readline()
            offset=int(input("what is your desired offset?"))
            temp=[]
            for i in range(len(data)):
                temp.append(chr(ord(data[i]) + offset))
            b="".join(temp)
            file.close()
            file=open(filename,"w")
            file.write(b)
            file.close()
            print("your file has been encrypted!")
        elif self.choice=="3":
            data=input("enter the data to be encrypted:\n")
            temp=[]
            offset=int(input("what is the offset?"))
            for i in range(len(data)):
                temp.append(chr(ord(data[i]) + offset))
            b="".join(temp)
            print("your data has been encrypted.")
            print(b)
        elif self.choice=="4":
            filename = input("enter the filename to be encrytped")
            file = open(filename, "r")
            data = file.readline()
            offset = int(input("what was the encryption offset?"))
            temp = []
            for i in range(len(data)):
                temp.append(chr(ord(data[i]) - offset))
            b = "".join(temp)
            file.close()
            file = open(filename, "w")
            file.write(b)
            file.close()
            print("your file has been decrypted!")
        elif self.choice=="5":
            data = input("enter the data to be decrypted:\n")
            temp = []
            offset = int(input("what is the offset?"))
            for i in range(len(data)):
                temp.append(chr(ord(data[i]) - offset))
            b = "".join(temp)
            print("your data has been decrypted.")
            print(b)




choice=(input("\nwhat do you want to do?\n1.create a new file \n2.encrypt an existing "
                 "file\n3.encrypt text.\n4.decrypt a file.\n5.decrypt text..\n*.exit the program"))
#first step to create the file
while(choice!='*'):
    request=encryptor(choice)
    request.main()
    choice = (input("\nwhat do you want to do?\n1.create a new file \n2.encrypt an existing "
                    "file\n3.encrypt text.\n4.decrypt a file.\n5.decrypt text..\n*.exit the program"))

