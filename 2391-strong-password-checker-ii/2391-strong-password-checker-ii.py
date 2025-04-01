class Solution(object):
    def strongPasswordCheckerII(self, password):
        
        n = len(password)
        hasLower = False
        hasUpper = False
        hasDigit = False
        specialChar = False
        spcl_char= "!@#$%^&*()-+"
        for i in range(n):
            if password[i].islower():
                hasLower = True
            if password[i].isupper():
                hasUpper = True
            if password[i].isdigit():
                hasDigit = True
            if password[i] in spcl_char:
                specialChar = True
        for i in range(1,n):
            if(password[i-1]==password[i]):
                return False
            
        if (hasLower and hasUpper and hasDigit and specialChar and n >= 8):
            return True
        else:
            return False