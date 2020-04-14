#---- License ----
"""
This code is the property of David Sinfield (dsinfield6@gmail.com) It is  released under The GNU public license the short version of which is you may copy, 
distribute, amend but this section of header should remain intact.

The long version is at https://www.gnu.org/licenses/gpl-3.0.html
"""

#------------------------------------------------------------------------------------------------------------------------------
# This is a Transmissibility generator v1.0
# The parameters are prompted for on the command line. It takes no command line parameters.
#------------------------------------------------------------------------------------------------------------------------------

#usage
print ("This program models the number of people infected in over a number of days for a given R value.")
print ()
print ("Day Zero are the number of infections on Day 0")
print("The R value is the number of people each infected person can transmit to.")
print(" R may be a decimal value. The result on day N will be rounded up to an integer.")
print("The program assumes that R declines linearly with the number of infections as the chance of contacting R uninfected declines")
print ("the chance parameter calculation may be a little simplistic but is calculated as (population-infected)/population ")
print ("The definition of R does not include a time element so this assumes one iteration a day.")
#functions
#all the get functions require validity checking for input type numeric.
def getpopulation():
    ipopulation=input("Population(default 70m) - ")
    if len(ipopulation) > 0:
        population=int(ipopulation)
    else:
        print("70m used")
        population=70000000
        return population
    
def getdayzero():
    idayzero=input("Day Zero infections (default =1) - ")
    if len(idayzero)>0:
        dayzero=int(idayzero)
    else:
        print ("1 used")
        dayzero=int(1)
    return dayzero
    #ToDo validty check/default
def getdays():
    return int(input("Days - "))
      #ToDo validty check/default
def getrvalue():
    return float(input("R Value - "))
def gettarget():
    itarget=input("Target value (leave blank for population=target) - ")
    if len(itarget)>0:
        target=int(itarget)
    else:
        print(str(population)+" used")
        target=population
    return target
#end functions

#start procedural
population=getpopulation()
dayzero=getdayzero()
days=getdays()
rvalue=getrvalue()
target=gettarget()

infected=dayzero
newcases=dayzero
csv=["day,infected,todaysinfections, opportunityfactor\n"]
for day in range (1, days):
    # calculations
    chance=((population+1)-infected)/population
    todayscases=float((newcases*rvalue)*chance)
    infected=infected+todayscases
    newcases=float(todayscases)
    #show results
    print ("Chance: "+str(chance)+" Day number: " + str(day) + " - Infected: " + str(int(infected))+" Newcases today:"+str(int(todayscases+0.9)))
    csv.append(str(day)+","+str(infected)+","+str(todayscases)+","+str(chance)+"\n")
    #exit conditions
    if target > 0:
        if infected > target: 
            break
    if newcases<1:
        print("No new cases")
        break
print("Program end")

#Option to write a file of data
dofile=input("Enter y to write a result file: ")
if dofile=="y" or dofile== "Y":
    filename=input("Filename (exension .csv will be added): ")
    if len(filename)==0:
        print ("No Filename results.csv will be used")
        f=open("results.csv","a")
    else:
        f=open(filename+".csv", "a")
    print ("Writing "+ f.name)
    for x in csv:
        f.write(x)
    f.close
# end procedural
    


