import time
import os


directory = "C:\\ACHReturn\\"
OutDirectory = directory + "Out\\"



if (not os.path.isdir(OutDirectory)):
    os.makedirs(OutDirectory)













allfile = {}

for Filename in os.listdir(directory):
    if Filename.endswith(".txt"):


        f = open(directory+Filename)
        f2 = open(OutDirectory+"Return"+Filename,"w+")
        print(f2.name)

        line = 0  # line counter
        rownum6 = 0
        First = ""
        Secound = ""
        routing=""
        batch=""
        amount6 = 0
        tamount6 = 0
        num8 = 0

        for x in f:
            # For 1 st line
            if line == 0 :
                First = x[4:13]
                Secound = x[13:23]
                length = (len(x))
                f2.write(str(x[0:2]) +str(Secound ) +str(x[3] ) +str(First ) +str(x[23:length-1])+" "+str(x[length-1]))

            elif x[0] == "5"  :

                f2.write(str(x[0:78])+"1"+str(x[79:len(x)]))


            elif x[0] == "6" :
                rownum6 = rownum6 + 1
                amount6= x[29:39]
                tamount6 = tamount6 + int(amount6)

                routing = x[3:11]
                batch = x[79:len(x) - 1]
                #print(routing, batch)
                f2.write("626"+str(x[3:78])+"1"+str(x[79:len(x)]))
                f2.write("799R01"+batch+"      "+routing+"                                            "+batch+"\n")

            elif x[0] == "8":
                    num8 = num8 + 1



                    num = int(x[7:10]) * 2
                    num = "{:03d}".format(num)

                    mrouting = int(rownum6) * int(routing)

                    mrouting = str(mrouting)
                    tamount6 = "{:08d}".format(tamount6)



                    f2.write(str(x[0:7])+str(num)+"00"+str(mrouting[-8:])+"0000"+tamount6+str(x[32:len(x)-1])+"\n")



            elif x[0:2] == "90":
                num8 = "{:02d}".format(num8)

                f2.write(str(x[0:5])+str(num8)+"0000"+str(num8)+"00000"+str(num)+"00"+str(mrouting[-8:])+"0000"+tamount6+str(x[43:len(x)-1])+" ")




            line =line +1

        print("Addition of routining number is-"+str(mrouting))
        print("Number of and 7 records-" + str(num))
        print("Total amount-"+str(tamount6))
        print("Number of 9 and 8 records-"+str(num8))




