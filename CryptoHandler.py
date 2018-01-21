

#ord(char) turns from char to ascii
#chr(int) turns from ascii to char
alphanum = {}
numalpha = {}
for count in range(0, 26):
    alphanum[chr(97+count)] = count
    numalpha[count] = chr(97+count)

class shift_cipher:
    message = ""
    key = 0
    cipher = ""


    def encrypt(self):
       """Starts encryption process by prompting for a message and a key then turning them into a cipher"""
       self.message = input("Please state your message\n")
       self.key = int(input("Please state the shift value\n"))
       for letter in self.message:
           if letter == " ":
               self.cipher += " "
           else:
               self.cipher +=  numalpha[(alphanum[letter]+self.key)%26]
       print(self.cipher)


    def decrypt(self):
        temp_message = ""
        for letter in self.cipher:
            if letter == " ":
                self.cipher += " "
            else:
                temp_message += numalpha[(alphanum[letter]-self.key)%26]
        print(temp_message)

class caesar_cipher:
    message = ""
    key = 3
    cipher = ""


    def encrypt(self):
       """Starts encryption process by prompting for a message then turning it into a cipher"""
       self.message = input("Please state your message\n")
       for letter in self.message:
           if letter == " ":
               self.cipher += " "
           else:
               self.cipher +=  numalpha[(alphanum[letter]+self.key)%26]
       print(self.cipher)


    def decrypt(self):
        temp_message = ""
        for letter in self.cipher:
            if letter == " ":
                self.cipher += " "
            else:
                temp_message += numalpha[(alphanum[letter]-self.key)%26]
        print(temp_message)




sc = shift_cipher()
sc.encrypt()
sc.decrypt()













# handler that calls on different classes
"""
keeps a dictionary that increments in number for each cipher added


#add cipher

#remove cipher

#init
    displays all the ciphers in format   "key:   value"





"""











# init