# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 14:41:21 2023
lines 8 to 12, 201 to 205, and 216 to 220 have commented out code to make a switch 
usable with this program instead of using input 
@author: Erik Bailey
"""
#import RPi.GPIO as GPIO#allows the use of the switch through gpio ports
#import time#used to assure switch bounce isn't a problem
#ButtonPin = 4  # switch is connected to gpio4
#GPIO.setwarnings(False)#disable warnings
#GPIO.setup(ButtonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)#used to set up the button pin for later use
from random import randint
#srows are used to show a board and eventually change to show player position
#along with the snakes and ladders beginning and ending points
srowOne = ['1','2','3','4','5','6','7','8','9','10']
srowTwo = ['20','19','18','17','16','15','14','13','12','11']
srowThree = ['21','22','23','24','25','26','27','28','29','30']
srowFour = ['40','39','38','37','36','35','34','33','32','31']
srowFive = ['41','42','43','44','45','46','47','48','49','50']
srowSix = ['60','59','58','57','56','55','54','53','52','51']
srowSeven = ['61','62','63','64','65','66','67','68','69','70']
srowEight = ['80','79','78','77','76','75','74','73','72','71']
srowNine = ['81','82','83','84','85','86','87','88','89','90']
srowTen = ['100','99','98','97','96','95','94','93','92','91']
sboard=[srowTen,srowNine,srowEight,srowSeven,srowSix,srowFive,srowFour,srowThree,srowTwo,srowOne]
ladderStart = [1,4,8,21,28,50,71,80]#used to make player go up to ladder end value
sladderStart = ["1","4","8","21","28","50","71","80"]#used to display
ladderEnd = [38,14,30,42,76,67,92,99]#tells where the player will end up after landingon ladder
sladderEnd = ['38','14','30','42','76','67','92','99']
snakeStart = [32,36,48,62,88,95,97]#same kind of thing as ladder only going down now
ssnakeStart = ['32','36','48','62','88','95','97']
snakeEnd = [10,6,26,18,24,56,78]
ssnakeEnd = ['10','6','26','18','24','56','78']
def setsBoard(new):#refresh board so it has only numeric value in string 
    srowOne = ['1','2','3','4','5','6','7','8','9','10']
    srowTwo = ['20','19','18','17','16','15','14','13','12','11']
    srowThree = ['21','22','23','24','25','26','27','28','29','30']
    srowFour = ['40','39','38','37','36','35','34','33','32','31']
    srowFive = ['41','42','43','44','45','46','47','48','49','50']
    srowSix = ['60','59','58','57','56','55','54','53','52','51']
    srowSeven = ['61','62','63','64','65','66','67','68','69','70']
    srowEight = ['80','79','78','77','76','75','74','73','72','71']
    srowNine = ['81','82','83','84','85','86','87','88','89','90']
    srowTen = ['100','99','98','97','96','95','94','93','92','91']
    new=[srowTen,srowNine,srowEight,srowSeven,srowSix,srowFive,srowFour,srowThree,srowTwo,srowOne]
    return new
sboard=setsBoard(sboard)
def ladderCheck(playerSpace):#after dice roll checks for ladder
    i=0#first place in list
    while(playerSpace>=ladderStart[i]):#checks until no more possible ladders to go up
        if(playerSpace==ladderStart[i]):#if player on a ladder
            playerSpace=ladderEnd[i]#go to space at end of ladder
            return playerSpace#only one ladder move per turn
        i=i+1#next ladder value will be checked
        if(i==8):#no more ladders in list 
            return playerSpace#return uneffected player space
    return playerSpace#just in case the loop fails

#essentially the same as laddercheck except it looks at snakes
def snakeCheck(playerSpace):#after dice roll checks for snake
    i=0#first place in list
    while(playerSpace>=snakeStart[i]):#checks until no more possible snkae to go down
        if(playerSpace==snakeStart[i]):
            playerSpace=snakeEnd[i]#go down snake
            return playerSpace
        i=i+1
        if(i==7):
            return playerSpace
    return playerSpace

def move(playerSpace):#moves player 1 to 6 spaces at random
    dice=randint(1,6)#pick an integer from 1 to 6 at random
    if(playerSpace+dice<=100):#game won't be won unless landing on exactly 100        
        playerSpace=playerSpace+dice#initial move before check for snake or ladder
        #in order to not go up a ladder and down a snake multiple times in one turn
        if(ladderCheck(playerSpace)==playerSpace):#no ladder
            playerSpace = snakeCheck(playerSpace)# no ladder then check for snake
        else:#yes ladder
            playerSpace = ladderCheck(playerSpace)
    return playerSpace

def xfindRow(playerSpace):#used to find numeric value of playerspace row
    rowSpace= int(playerSpace)-1#in case multiple of 10
    rowSpace2=int(rowSpace/10)#no decimals
    rowSpace2=9-rowSpace2#reverse the order as the first list is highest
    return rowSpace2
def specialBoard(nBoard, listspace, s, slList):#board, 7or8 depending on snake or ladder
        #ls le ss or se, ladderStart ladderEnd snakeStart or snakeEnd
    while(listspace>=0):#get each value in slList
        row=xfindRow(slList[listspace])#used to find what row in nBoard slList is
        x=0#used to compare to row 
        for a in nBoard:#searched the lists inside nBoard
            if row==x:#finds the right list in nBoard
                for i in range(len(a)):#look for the right string in a
                    if a[i]==slList[listspace]:#finds the number that will be changed 
                        nBoard[x][i]=s+str(listspace+1)
                        #changes specific spot to be called s + a number
                        #based on where it was found in slList
            x=x+1#look at next list 
        listspace=listspace-1#go onto next value in slList
    return nBoard#return the board when done changing any unnocupied tile from slList 

def sfindRow(playerSpace):#used to get the row player space is in without any other pieces
    rowSpace= playerSpace-1#in case multiple of 10
    rowSpace=int(rowSpace/10)#determines the number of row starting with 0
    if rowSpace==0:#first row at bottom
        srowOne = ['1','2','3','4','5','6','7','8','9','10']#no special tiles
        return srowOne#return clean row
    if rowSpace==1:
        srowTwo = ['20','19','18','17','16','15','14','13','12','11']
        return srowTwo
    if rowSpace==2:
        srowThree = ['21','22','23','24','25','26','27','28','29','30']
        return srowThree
    if rowSpace==3:
        srowFour = ['40','39','38','37','36','35','34','33','32','31']
        return srowFour
    if rowSpace==4:
        srowFive = ['41','42','43','44','45','46','47','48','49','50']
        return srowFive
    if rowSpace==5:
        srowSix = ['60','59','58','57','56','55','54','53','52','51']
        return srowSix
    if rowSpace==6:
        srowSeven = ['61','62','63','64','65','66','67','68','69','70']
        return srowSeven
    if rowSpace==7:
        srowEight = ['80','79','78','77','76','75','74','73','72','71']
        return srowEight
    if rowSpace==8:
        srowNine = ['81','82','83','84','85','86','87','88','89','90']
        return srowNine
    if rowSpace==9:#last row at top
        srowTen = ['100','99','98','97','96','95','94','93','92','91']
        return srowTen

def changeRow(new,rowNum1,row1,playerOne,rowNum2,row2,playerTwo):#change playerSpace to a string in if
    #(board to be changed, numerical value of player 1s row, player 1s row, player1s space,
    #numerical value of player 1s row, player 1s row, player1s space)
    new=setsBoard(sboard)#clear the board of last player spaces
    if rowNum1==rowNum2:#if the rows are the same
        x=0#used to find row to change
        rowNum=rowNum1#so that things are simpler both rowNum1 and 2 are the same
        for a in new:#find row to change
            if rowNum==x:#checks row to be the same
                row=row1#so that things are simpler both row1 and 2 are the same
                for i in range(len(row)):#look for the playerspaces to change
                    if(playerTwo==playerOne):#if both players on the same space
                        if row[i]==str(playerOne):#finds place of both players
                            new[x][i]="1&2"#locks the piece down to be told as 1&2
                    elif row[i]==str(playerOne):#finds player one when not p2
                        new[x][i]="pl1"#locks the piece down to be told as pl1
                    elif row[i]==str(playerTwo):#finds playertwo when not p1
                        new[x][i]="pl2"#locks the piece down to be told as pl2
            x=x+1#look at next row
        return new#returns the board when finished changing it
    else:#if the players are on different rows
        a=0#same purpose as x was used above
        for x in new:#find row to change
            if row1==x:#finds player 1s row
                for i in range(len(row1)):#finds where in row player 1 is
                    if row1[i]==str(playerOne):#when true changes spot on board
                        new[a][i]="pl1"
            elif row2==x:#same as if statement above just with player one instead of two
                for i in range(len(row2)):
                    if row2[i]==str(playerTwo):
                        new[a][i]="pl2"
            a=a+1#look at next row
        return new#returns the board when finished changing it
            
def displayBoard(sboardTemp):#displays sboardTemp and makes it pretty
    ki=0#used with shi to format each individual spot on the board
    for x in sboardTemp:#formats all in sboardtemp
        shi=0#ki is used for row while shi is used for column
        for i in x:#formats all in row
            try:#if it is numeric it will be formatted to have 3 characters with any extra being 
                #0s attached at the front
                sboardTemp[ki][shi]=("{:03d}".format((int(sboardTemp[ki][shi]))))
            except:#in case it hits a special tile that isn't numeric such as pl1
                pass
            shi=shi+1#next column
        ki=ki+1#next row
    for x in sboardTemp:#print all rows on the board
        print(x)#row
        print()#space
    print()#space to give way for next board
       
def snewBoard(playerOne,playerTwo):#after player moves a new board will need to be made
    new =sboard#clear board of previous moves
    rowtemp1= xfindRow(playerOne)#gets numeric value of row
    row1=sfindRow(playerOne)#gets list of row
    rowtemp2= xfindRow(playerTwo)#gets numeric value of row
    row2=sfindRow(playerTwo)#gets list of row
    new=changeRow(new,rowtemp1,row1,playerOne,rowtemp2,row2,playerTwo)#change the board
    return new #return the board 
playerOne =0#player1 spot
playerTwo =0#player 2 spot
while((playerOne!=100)&(playerTwo!=100)):#goes until someone hits 100 and wins
    input("press enter to roll dice")#gets player input
    #an alternate version of input for when a pi is available
    #print("press switch to roll dice")
    #while (0 == GPIO.input(ButtonPin)):#will not continue unil button is pressed
    #    pass#doesn't have anything done while in the loop
    #time.sleep(.08)#used to account for switch bounce
    
    playerOne = move(playerOne)#player 1 moves
    sboard=setsBoard(sboard)#clear the board 
    sboard= snewBoard(playerOne,playerTwo)#sets up new board
    sboard= specialBoard(sboard,7,"ls",sladderStart)#adds ladder start
    sboard= specialBoard(sboard,7,"le",sladderEnd)#adds ladder end
    sboard= specialBoard(sboard,6,"ss",ssnakeStart)#adds snake start
    sboard= specialBoard(sboard,6,"se",ssnakeEnd)#adds snake end
    displayBoard(sboard)#displays board
    input("press enter to roll dice")#gets player input
    #an alternate version of input for when a pi is available
    #print("press switch to roll dice")
    #while (0 == GPIO.input(ButtonPin)):#will not continue unil button is pressed
    #    pass#doesn't have anything done while in the loop
    #time.sleep(.08)#used to account for switch bounce
    
    playerTwo = move(playerTwo)#player 2 moves
    sboard=setsBoard(sboard)#clear the board 
    sboard= snewBoard(playerOne,playerTwo)#sets up new board
    sboard= specialBoard(sboard,7,"ls",sladderStart)#adds ladder start
    sboard= specialBoard(sboard,7,"le",sladderEnd)#adds ladder end
    sboard= specialBoard(sboard,6,"ss",ssnakeStart)#adds snake start
    sboard= specialBoard(sboard,6,"se",ssnakeEnd)#adds snake end
    displayBoard(sboard)#displays board
if(playerOne==100):#tells who wins 
    print("player one wins!!!")
if(playerTwo==100):#tells who wins 
    print("player two wins!!!")
