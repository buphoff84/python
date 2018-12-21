import sys
import math

account = raw_input("Please insert Accountnumber: ").zfill(10)
bankCode = raw_input("Please insert bank Code: ")
ibanBase = bankCode + account + "131400"
crc1 = int(ibanBase) % 97
crc2 = 98 - crc1

print("Your IBAN is: ", "DE" + str(crc2) + bankCode + account)