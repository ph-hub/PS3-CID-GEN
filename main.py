import random,string,os
from os import system
system("cls"if os.name == "nt" else "clear")

cidbase = (
   "00000001008766A39D091E82DCB8",
   "00000001008900071001BA883AFC",
   "00000001008300091003A0C834CA",
   "000000010085001110068A930758",
   "000000010084000D1411683EA8BE",
   "00000001008A000910011FB7AF3F",
   "000000010085000B1014DFC6F4D1",
   "00000001008300111001E23A90A0",
   "000000010085000B14097128FA85",
   "0000000100840006100BCF4D7538",
   "000000010086000814005361B464",
   "0000000100840003101941AE12B8",
   "0000000100840006100BCF4D7538",
   "0000000100840009142539CB327F",
   "000000010083000D140392AF7365",
   "000000010085000D140094BA126D",
   "0000000100847FDB323886F433FE",
   "0000000100895F32324E08615DBF",
   "00000001008FB285FA76017FC958",
   "0000000100840001100e316e74a2",
   "000000010083000F1402365C2495",
   "000000010087000B14068FDD1092",
   "000000010083000B0401010CAE81",
   "0000000100830009100FABD1C5A8",
   "000000010085000C10220F622A62",
   "00000001008800131404B9616FA4"
    )
while True:
    cid = random.choice(cidbase)
    cidall = ('').join(random.choice(string.ascii_uppercase + string.digits)for k in range(4))
    
    cidcomplet = cid + cidall
    print(cidcomplet)
    
    file = open("cid.txt", "a")
    file.write(cidcomplet +"\n")
    file.close
