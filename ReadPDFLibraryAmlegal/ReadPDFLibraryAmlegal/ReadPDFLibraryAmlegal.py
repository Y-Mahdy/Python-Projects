import PyPDF2
import time
from collections import OrderedDict
import datetime
import os
import urllib
import selenium
from selenium import webdriver
import sys
import re
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
#import roman;
PreIndexType = -2
CurrIndexType = -2
lstOfPreIndexTypes = []
lstOfLevel = []
lstOfNumbersBrackets= [0, 0, 0, 0, 0, 0, 0, 0, 0]
lstOfNumbersSquare= [0, 0, 0, 0, 0, 0, 0, 0, 0]
nCurrArrNumbers = 0
nCurrSmallLetters = 0
nCurrCAPLetters = 0
nCurrSmallDoubleLetters = 0
nCurrCAPDoubleLetters = 0
nCurrsmallLatinLetters = 0
nCurrCAPLatinLetters = 0
nCurrNumber = 1
nCurrDoubleDash = 1
nCurrSubNumberDash = 1
nCurrSubNumber = 1
nCurrHSpacing = 0
nCurrHHSpacing = 0
nCurrhSpacing = 0
nCurrhhSpacing = 0
nCurruSpacing = 0
nCurrUSpacing = 0
nCurrwSpacing = 0
nCurrWSpacing = 0
nCurrwwSpacing = 0
nCurrWWSpacing = 0
nCurrZeroSpacingbrackets = 0
nCurrZeroSpacingSquare = 0
nISpace = 0
isZeroStart = 0
OutputPathothingNothing = ''
arrayOfNumbers              = ['11','22','33','44','55','66','77','88','99']
arrayOfSmallLetters         = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
arrayOfCAPLetters           = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
arrayOfDoubleSmallLetters   = ['aa','bb','cc','dd','ee','ff','gg','hh','ii','jj','kk','ll','mm','nn','oo','pp','qq','rr','ss','tt','uu','vv','ww','xx','yy','zz']
arrayOfDoubleCAPLetters     = ['AA','BB','CC','DD','EE','FF','GG','HH','II','JJ','KK','LL','MM','NN','OO','PP','QQ','RR','SS','TT','UU','VV','WW','XX','YY','ZZ']
arraySmallofLatinNumbering  = ['i', 'ii', 'iii', 'iv' , 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi', 'xii', 'xiii', 'xiv', 'xv', 'xvi', 'xvii', 'xviii','xix', 'xx']
arrayCapofLatinNumbering    = ['I', 'II', 'III', 'IV' , 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII','XIX', 'XX']
def WorkOnSectionPartFn(csvFile, stLineBeforeStrip, structreNumberMain):
    stLine = stLineBeforeStrip.strip().replace("â€œ", '“').replace("â€","”")
    global PreIndexType
    global CurrIndexType
    global lstOfPreIndexTypes
    global lstOfLevel
    global lstOfNumbersBrackets
    global nCurrSmallLetters 
    global nCurrArrNumbers
    global nCurrCAPLetters 
    global nCurrSmallDoubleLetters 
    global nCurrCAPDoubleLetters
    global nCurrsmallLatinLetters
    global nCurrCAPLatinLetters
    global nCurrNumber
    global nCurrDoubleDash
    global nCurrSubNumber
    global nCurrSubNumberDash
    global nCurrHSpacing
    global nCurrHHSpacing
    global nCurrhSpacing 
    global nCurrhhSpacing
    global nCurruSpacing 
    global nCurrUSpacing
    global nCurruuSpacing 
    global nCurrUUSpacing
    global nCurrwSpacing
    global nCurrWSpacing
    global nCurrwwSpacing
    global nCurrWWSpacing
    global nCurrZeroSpacingbrackets
    global nCurrZeroSpacingSquare
    global isZeroStartbrackets
    global isZeroStartSquare
    isNumberingFormating(stLineBeforeStrip)
    if CurrIndexType > -1 or ( CurrIndexType == -1 and len(lstOfLevel) != 0):
    #if stLine.startswith('--') or stLine.startswith('-') or stLine.startswith('(1)') or stLine.startswith('(0)') or   stLine.startswith('[1]') or stLine.startswith('(1.'+str(nCurrSubNumber)+')') or stLine.startswith('(1.1)') or stLine.startswith('('+str(nCurrNumber - 1)+'.'+str(nCurrSubNumber) +')') or stLine.startswith('('+str(nCurrNumber - 1)+'.1)')  or stLine.startswith('(a)') or stLine.startswith('(A)') or stLine.startswith('(aa)') or stLine.startswith('(AA)') or stLine.startswith('(i)') or stLine.startswith('(I)') or stLine.startswith('('+str(nCurrNumber)+ ')') or stLine.startswith('['+str(nCurrNumber)+ ']') or stLine.startswith('(' + arrayOfNumbers[nCurrArrNumbers] + ')') or stLine.startswith('[' + arrayOfNumbers[nCurrArrNumbers] + ']') or stLine.startswith(str('(' + arrayOfSmallLetters[nCurrSmallLetters] + ')')) or stLine.startswith(str('(' + arrayOfCAPLetters[nCurrCAPLetters] + ')')) or stLine.startswith(str('(' + arrayOfDoubleSmallLetters[nCurrSmallDoubleLetters] + ')')) or stLine.startswith(str('(' + arrayOfDoubleCAPLetters[nCurrCAPDoubleLetters] + ')')) or stLine.startswith(str('(' + arraySmallofLatinNumbering[nCurrsmallLatinLetters] + ')')) or stLine.startswith(str('(' + arrayCapofLatinNumbering[nCurrCAPLatinLetters] + ')')):
        isLatin = 0
        lengthOfi = 0
        isZeroStartbrackets = 0
        isZeroStartSquare = 0
        PartOfStructureNumber = ''
        #CurrIndexType = detectNumberingType(stLine.strip())
        if CurrIndexType > -1:
            if (stLine.startswith('(i)')):
                arrayOfText = []
                arrayOfText = stLineBeforeStrip.split('(i)')
                lengthOfi = len(arrayOfText[0])
                if (lengthOfi != nCurrhSpacing):
                    isLatin = 1
                else:
                    nCurrhSpacing = 0
            elif (stLine.startswith('(I)')):
                arrayOfText = []
                arrayOfText = stLineBeforeStrip.split('(I)')
                lengthOfi = len(arrayOfText[0])
                if (lengthOfi != nCurrHSpacing):
                    isLatin = 2
                else:
                    nCurrHSpacing = 0
            elif (stLine.startswith('(ii)')):
                arrayOfText = []
                arrayOfText = stLineBeforeStrip.split('(ii)')
                lengthOfi = len(arrayOfText[0])
                if (lengthOfi != nCurrhhSpacing):
                    isLatin = 1
                else:
                    nCurrhhSpacing = 0
            elif (stLine.startswith('(II)')):
                arrayOfText = []
                arrayOfText = stLineBeforeStrip.split('(II)')
                lengthOfi = len(arrayOfText[0])
                if (lengthOfi != nCurrHHSpacing):
                    isLatin = 2
                else:
                    nCurrHHSpacing = 0
            elif (stLine.startswith('(v)')):
                arrayOfText = []
                arrayOfText = stLineBeforeStrip.split('(v)')
                lengthOfv = len(arrayOfText[0])
                if (lengthOfv != nCurruSpacing):
                    isLatin = 1
                else:
                    nCurruSpacing = 0
            elif (stLine.startswith('(V)')):
                arrayOfText = []
                arrayOfText = stLineBeforeStrip.split('(V)')
                lengthOfV = len(arrayOfText[0])
                if (lengthOfV != nCurrUSpacing):
                    isLatin = 2
                else:
                    nCurrUSpacing = 0
            elif (stLine.startswith('(vv)')):
                arrayOfText = []
                arrayOfText = stLineBeforeStrip.split('(vv)')
                lengthOfv = len(arrayOfText[0])
                if (lengthOfvv != nCurruuSpacing):
                    isLatin = 1
                else:
                    nCurruuSpacing = 0
            elif (stLine.startswith('(VV)')):
                arrayOfText = []
                arrayOfText = stLineBeforeStrip.split('(VV)')
                lengthOfVV = len(arrayOfText[0])
                if (lengthOfVV != nCurrUUSpacing):
                    isLatin = 2
                else:
                    nCurrUUSpacing = 0
            elif (stLine.startswith('(x)')):
                arrayOfText = []
                arrayOfText = stLineBeforeStrip.split('(x)')
                lengthOfx = len(arrayOfText[0])
                if (lengthOfx != nCurrwSpacing):
                    isLatin = 1
                else:
                    nCurrwSpacing = 0
            elif (stLine.startswith('(X)')):
                arrayOfText = []
                arrayOfText = stLineBeforeStrip.split('(X)')
                lengthOfX = len(arrayOfText[0])
                if (lengthOfX != nCurrWSpacing):
                    isLatin = 2
                else:
                    nCurrWSpacing = 0
            elif (stLine.startswith('(xx)')):
                arrayOfText = []
                arrayOfText = stLineBeforeStrip.split('(xx)')
                lengthOfxx = len(arrayOfText[0])
                if (lengthOfxx != nCurrwwSpacing):
                    isLatin = 1
                else:
                    nCurrwwSpacing = 0
            elif (stLine.startswith('(XX)')):
                arrayOfText = []
                arrayOfText = stLineBeforeStrip.split('(XX)')
                lengthOfXX = len(arrayOfText[0])
                if (lengthOfXX != nCurrWWSpacing):
                    isLatin = 2
                else:
                    nCurrWWSpacing = 0
            elif (stLine.startswith('(1)')):
                arrayOfText = []
                arrayOfText = stLineBeforeStrip.split('(1)')
                length = len(arrayOfText[0])
                if (length == nCurrZeroSpacingbrackets):
                    isZeroStartbrackets = 1
            elif (stLine.startswith('[1]')):
                arrayOfText = []
                arrayOfText = stLineBeforeStrip.split('[1]')
                length = len(arrayOfText[0])
                if (length == nCurrZeroSpacingSquare):
                    isZeroStartSquare = 1
            if isLatin == 1:
                CurrIndexType = 5
            elif isLatin == 2:
                CurrIndexType = 6

            PartOfStructureNumber = DetectLevelOfNumbering (stLine) 
            AddTextToFile(csvFile, structreNumberMain + PartOfStructureNumber , stLine)
        else:
            PartOfStructureNumber = ''
            for i in range(len(lstOfLevel)):
                    PartOfStructureNumber += '_' + str(lstOfLevel[i])
            AddTextToFile(csvFile, structreNumberMain + PartOfStructureNumber + '_1', stLine)
        if ('(I)   Amendments to a certificate of appropriateness.' in stLine):
            lstOfLevel.pop()
            PartOfStructureNumber1 =''
            lstOfLevel.pop()
            lstOfLevel.append(7)
            lstOfPreIndexTypes.pop()
            ResetIndex ()
            nCurrCAPLetters = 0
            nCurrNumber = 8
            CurrIndexType = 0
            PreIndexType = 0
            for i in range(len(lstOfLevel)):
                    PartOfStructureNumber1 += '_' + str(lstOfLevel[i])
            AddTextToFile(csvFile, structreNumberMain + PartOfStructureNumber1 , 'No Data There') 
        elif ('(58)   VEHICULAR SIGN means any sign on a vehicle moving along the ground or on any vehicle parked' in stLine):
            lstOfLevel.pop()
            PartOfStructureNumber1 =''
            lstOfLevel.pop()
            lstOfLevel.append(59)
            lstOfPreIndexTypes.pop()
            ResetIndex ()
            nCurrCAPLetters = 0
            nCurrNumber = 60
            CurrIndexType = 0
            PreIndexType = 0
            for i in range(len(lstOfLevel)):
                    PartOfStructureNumber1 += '_' + str(lstOfLevel[i])
            AddTextToFile(csvFile, structreNumberMain + PartOfStructureNumber1 , 'No Data There') 
        print('>>>>>>>>>> '+structreNumberMain + PartOfStructureNumber)
    else:
        # Section doesn't contain any numbering
        print('>>>>>>>> Text is: '+ stLine)
        print('>>>>>>>>>> Type: Nothing')
        structreNumber = structreNumberMain + '_1'
        AddTextToFile(csvFile, structreNumber, stLine.strip())
        print('>>>>>>>>>> '+structreNumber)
        
def detectNumberingType(st):
    global arrayOfNumbers
    global arrayOfCAPLetters
    global arrayOfSmallLetters
    global arrayOfDoubleCAPLetters
    global arrayOfDoubleSmallLetters
    global arrayCapofLatinNumbering
    global arraySmallofLatinNumbering
    global nCurrSmallLetters 
    global nCurrArrNumbers
    global nCurrCAPLetters 
    global nCurrSmallDoubleLetters 
    global nCurrCAPDoubleLetters
    global nCurrsmallLatinLetters
    global nCurrCAPLatinLetters
    global nCurrNumber
    global nCurrSubNumber
    if  st.startswith('(1)') or st.startswith('('+str(nCurrNumber)+')') or st.startswith('[1]') or st.startswith('['+str(nCurrNumber)+']') or  st.startswith('(1)'):
        CurrIndexType = 0
    elif st.startswith('(a)') or st.startswith('('+arrayOfSmallLetters[nCurrSmallLetters]+')'):
        CurrIndexType = 1
    elif  st.startswith('(A)') or st.startswith('('+arrayOfCAPLetters[nCurrCAPLetters]+')'):
        CurrIndexType = 2
    elif  st.startswith('(aa)') or st.startswith('('+arrayOfDoubleSmallLetters[nCurrSmallDoubleLetters]+')'):
        CurrIndexType = 3
    elif  st.startswith('(AA)') or st.startswith('('+arrayOfDoubleCAPLetters[nCurrCAPDoubleLetters]+')'):
        CurrIndexType = 4
    elif  st.startswith('(i)') or st.startswith('('+arraySmallofLatinNumbering[nCurrsmallLatinLetters]+')'):
        CurrIndexType = 5
    elif  st.startswith('(I)') or st.startswith('('+arrayCapofLatinNumbering[nCurrCAPLatinLetters]+')'):
        CurrIndexType = 6
    elif st.startswith('--'):
        CurrIndexType = 7
    elif st.startswith('(1.'+str(nCurrSubNumber)+')') or st.startswith('(1.1)') or st.startswith('('+str(nCurrNumber - 1)+'.'+str(nCurrSubNumber) +')') or st.startswith('('+str(nCurrNumber - 1)+'.1)'):
        CurrIndexType = 8
    elif st.startswith('-'):
        CurrIndexType = 9
    elif st.startswith('(11)') or st.startswith('('+arrayOfNumbers[nCurrArrNumbers]+')') or st.startswith('[11]') or st.startswith('['+arrayOfNumbers[nCurrArrNumbers]+']'):
        CurrIndexType = 10
    else:
        CurrIndexType = -1
    return CurrIndexType
def DetectLevelOfNumbering (text):
    #Deal with the new data
    global PreIndexType
    global CurrIndexType
    global lstOfPreIndexTypes
    global lstOfLevel
    global lstOfNumbersBrackets
    global nCurrSmallLetters 
    global nCurrCAPLetters 
    global nCurrSmallDoubleLetters 
    global nCurrCAPDoubleLetters
    global nCurrsmallLatinLetters
    global nCurrCAPLatinLetters
    global nCurrNumber
    global nCurrDoubleDash
    global nCurrSubNumber
    global nCurrSubNumberDash
    global nCurrArrNumbers
    PartOfStructureNumber = ''
    #Two Cases
    #1- The same level
    if CurrIndexType == PreIndexType:
        if PreIndexType == 0:# Numerical
            if (text.startswith('(0)')):
                lstOfLevel.append(0)
                lstOfPreIndexTypes.append(CurrIndexType)
                nCurrNumber = 0
            elif ( text.startswith('(1)')) or ( text.startswith('[1]')):
                if text.startswith('(1)') and isZeroStartbrackets == 0:
                    lstOfLevel.append(1)
                    lstOfPreIndexTypes.append(CurrIndexType)
                    nCurrNumber = 1
                if text.startswith('[1]') and isZeroStartSquare == 0:
                    lstOfLevel.append(1)
                    lstOfPreIndexTypes.append(CurrIndexType)
                    nCurrNumber = 1
            else:
                lstOfLevel.pop()
                lstOfLevel.append(nCurrNumber)
                lstOfPreIndexTypes.pop()
                lstOfPreIndexTypes.append(CurrIndexType)
                nCurrNumber += 1
                if (text == '(2) thru (5)   Reserved.'):
                    nCurrNumber = 6
        elif PreIndexType == 1: # Alphapetical small
            if (not text.startswith('(a)')):
                lstOfLevel.pop()
                lstOfLevel.append(nCurrSmallLetters + 1)
                lstOfPreIndexTypes.pop()
                lstOfPreIndexTypes.append(CurrIndexType)
                ResetIndex ()
                if (nCurrSmallLetters == 26):
                    nCurrSmallLetters = 0
            else:
                lstOfLevel.append(1)
                lstOfPreIndexTypes.append(CurrIndexType)
                nCurrSmallLetters = 0
        elif PreIndexType == 2: # Alphapetical Big
            if (not text.startswith('(A)')):
                lstOfLevel.pop()
                lstOfLevel.append(nCurrCAPLetters + 1)
                lstOfPreIndexTypes.pop()
                lstOfPreIndexTypes.append(CurrIndexType)
                ResetIndex ()
            else:
                lstOfLevel.append(1)
                lstOfPreIndexTypes.append(CurrIndexType)
                nCurrCAPLetters = 0
        elif PreIndexType == 3: # Double Alphapetical Small
            if (not text.startswith('(aa)')):
                lstOfLevel.pop()
                lstOfLevel.append(nCurrSmallDoubleLetters + 1)
                lstOfPreIndexTypes.pop()
                lstOfPreIndexTypes.append(CurrIndexType)
                ResetIndex ()
            else:
                lstOfLevel.append(1)
                lstOfPreIndexTypes.append(CurrIndexType)
                nCurrSmallDoubleLetters = 0
        elif PreIndexType == 4: # Double Alphapetical Big
            if (not text.startswith('(AA)')):
                lstOfLevel.pop()
                lstOfLevel.append(nCurrCAPDoubleLetters + 1)
                lstOfPreIndexTypes.pop()
                lstOfPreIndexTypes.append(CurrIndexType)
                ResetIndex ()
            else:
                lstOfLevel.append(1)
                lstOfPreIndexTypes.append(CurrIndexType)
                nCurrCAPDoubleLetters = 0
        elif PreIndexType == 5: # Latin Small
            if (not text.startswith('(i)')):
                lstOfLevel.pop()
                lstOfLevel.append(nCurrsmallLatinLetters + 1)
                lstOfPreIndexTypes.pop()
                lstOfPreIndexTypes.append(CurrIndexType)
                ResetIndex ()
            else:
                lstOfLevel.append(1)
                lstOfPreIndexTypes.append(CurrIndexType)
                nCurrsmallLatinLetters = 0
        elif PreIndexType == 6: # Latin Big
            if (not text.startswith('(I)')):
                lstOfLevel.pop()
                lstOfLevel.append(nCurrCAPLatinLetters + 1)
                lstOfPreIndexTypes.pop()
                lstOfPreIndexTypes.append(CurrIndexType)
                ResetIndex ()
            else:
                lstOfLevel.append(1)
                lstOfPreIndexTypes.append(CurrIndexType)
                nCurrCAPLatinLetters = 0
        elif PreIndexType == 7:
            lstOfLevel.pop()
            lstOfLevel.append(nCurrDoubleDash)
            lstOfPreIndexTypes.pop()
            lstOfPreIndexTypes.append(CurrIndexType)
            ResetIndex ()
        elif PreIndexType == 8:
            lstOfLevel.pop()
            lstOfLevel.append(nCurrSubNumber)
            lstOfPreIndexTypes.pop()
            lstOfPreIndexTypes.append(CurrIndexType)
            ResetIndex ()
        elif PreIndexType == 9:
            lstOfLevel.pop()
            lstOfLevel.append(nCurrSubNumberDash)
            lstOfPreIndexTypes.pop()
            lstOfPreIndexTypes.append(CurrIndexType)
            ResetIndex ()
        if PreIndexType == 10:# Numerical
            if (not text.startswith('(11)')) and (not text.startswith('[11]')):
                lstOfLevel.pop()
                lstOfLevel.append(nCurrArrNumbers + 1)
                lstOfPreIndexTypes.pop()
                lstOfPreIndexTypes.append(CurrIndexType)
                ResetIndex ()
            else:
                lstOfLevel.append(1)
                lstOfPreIndexTypes.append(CurrIndexType)
                nCurrArrNumbers = 2
    else:
    #2- Different Level
        if CurrIndexType > 0 and CurrIndexType < 7: #Current is ALpha or Latin
            if text.startswith('(a)') or text.startswith('(A)') or text.startswith('(aa)') or text.startswith('(AA)') or (text.startswith('(i)') and CurrIndexType == 5) or (text.startswith('(I)')  and CurrIndexType == 6):
                lstOfLevel.append(1)
                lstOfPreIndexTypes.append(CurrIndexType)
                ResetIndex()
            else:
                while True:
                    lstOfLevel.pop()
                    lstOfPreIndexTypes.pop()
                    nLastLevel = lstOfLevel[len(lstOfLevel) - 1]
                    arrayTocheck = []
                    nPrePreIndex = lstOfPreIndexTypes[len(lstOfPreIndexTypes) - 1]
                    if nPrePreIndex == 1:
                        arrayTocheck = arrayOfSmallLetters
                    elif nPrePreIndex == 2:
                        arrayTocheck = arrayOfCAPLetters
                    elif nPrePreIndex == 3:
                        arrayTocheck = arrayOfDoubleSmallLetters
                    elif nPrePreIndex == 4:
                        arrayTocheck = arrayOfDoubleCAPLetters
                    elif nPrePreIndex == 5:
                        arrayTocheck = arraySmallofLatinNumbering
                    elif nPrePreIndex == 6:
                        arrayTocheck = arrayCapofLatinNumbering
                    if nPrePreIndex > 0  and nPrePreIndex < 7 and nPrePreIndex == CurrIndexType:
                        lstOfLevel.pop()
                        lstOfLevel.append(nLastLevel + 1)
                        lstOfPreIndexTypes.pop()
                        lstOfPreIndexTypes.append(CurrIndexType)
                        ResetIndex ()
                        break
        elif CurrIndexType == 0: #current is Numerical
            if (text.startswith('(1)') or text.startswith('[1]')) and isZeroStartbrackets == 0 and isZeroStartSquare == 0:
                lstOfLevel.append(1)
                lstOfPreIndexTypes.append(CurrIndexType)
                nCurrNumber = 2
            elif (text.startswith('(0)') or text.startswith('[0]')):
                lstOfLevel.append(0)
                lstOfPreIndexTypes.append(CurrIndexType)
                nCurrNumber = 1
            else:
                while True:
                    lstOfLevel.pop()
                    lstOfPreIndexTypes.pop()
                    nLastLevel = lstOfLevel[len(lstOfLevel) - 1]
                    nPrePreIndex = lstOfPreIndexTypes[len(lstOfPreIndexTypes) - 1]
                    if nPrePreIndex == 0 and (text.startswith('('+str(nLastLevel + 1)+')') or text.startswith('['+str(nLastLevel + 1)+']')):
                        lstOfLevel.pop()
                        lstOfPreIndexTypes.pop()
                        lstOfLevel.append(nLastLevel + 1)
                        lstOfPreIndexTypes.append(CurrIndexType)
                        ResetIndex ()
                        break
        elif CurrIndexType == 7: #Current is --
            if text.startswith('--'):
                lstOfLevel.append(1)
                lstOfPreIndexTypes.append(CurrIndexType)
                nCurrDoubleDash = 2
        elif CurrIndexType == 8: #Current is SubNumbering
           arrayOfText = []
           arrayOfText = text.split(' ')
           if (arrayOfText[0].endswith('.1)')):
                lstOfLevel.append(1)
                lstOfPreIndexTypes.append(CurrIndexType)
                nCurrSubNumber = 2
           else:
               last1stNumber = 0
               last2ndNumber = 0
               while True:
                   lstOfLevel.pop()
                   lstOfPreIndexTypes.pop()
                   nLastLevel = lstOfLevel[len(lstOfLevel) - 1]
                   nlastType = lstOfPreIndexTypes[len(lstOfPreIndexTypes) - 1]
                   if nlastType == 8 and arrayOfText[0].endswith('.' + str(nLastLevel + 1)+')'):
                    last2ndNumber = nLastLevel + 1
                   if nlastType == 0 and arrayOfText[0].startswith('(' + str(nLastLevel)+'.'):
                    last1stNumber = nLastLevel
                   if text.startswith('(' + str(last1stNumber)+'.'+str(last2ndNumber)+')'):
                     lstOfLevel.append(last2ndNumber)
                     lstOfPreIndexTypes.append(CurrIndexType)
                     nCurrSubNumber  = last2ndNumber + 1
                     ResetIndex ()
                     break
        elif CurrIndexType == 9: #Current is -
            if text.startswith('-'):
                lstOfLevel.append(1)
                lstOfPreIndexTypes.append(CurrIndexType)
                nCurrSubNumberDash = 2
        elif CurrIndexType == 10: #current is Numerical
            if text.startswith('(11)') or text.startswith('[11]'):
                lstOfLevel.append(1)
                lstOfPreIndexTypes.append(CurrIndexType)
                nCurrArrNumbers = 1
            else:
                while True:
                    lstOfLevel.pop()
                    lstOfPreIndexTypes.pop()
                    nLastLevel = lstOfLevel[len(lstOfLevel) - 1]
                    nPrePreIndex = lstOfPreIndexTypes[len(lstOfPreIndexTypes) - 1]
                    if nPrePreIndex == 10 and (text.startswith('('+arrayOfNumbers[nLastLevel + 1]+')') or text.startswith('['+arrayOfNumbers[nLastLevel + 1]+']')):
                        lstOfLevel.pop()
                        lstOfPreIndexTypes.pop()
                        lstOfLevel.append(nLastLevel + 1)
                        lstOfPreIndexTypes.append(CurrIndexType)
                        nCurrArrNumbers  = nLastLevel + 2
                        ResetIndex ()
                        break
        else:
            lstOfLevel.append(1)
            lstOfPreIndexTypes.append(CurrIndexType)
            if (CurrIndexType == 0):
                nCurrNumber  = 2
            else:
               if CurrIndexType == 1:
                nCurrSmallLetters += 1
               elif CurrIndexType == 2:
                nCurrCAPLetters += 1
               elif CurrIndexType == 3:
                nCurrSmallDoubleLetters += 1
               elif CurrIndexType == 4:
                nCurrCAPDoubleLetters += 1
               elif CurrIndexType == 5:
                nCurrsmallLatinLetters += 1
               elif CurrIndexType == 6:
                nCurrCAPLatinLetters += 1 
        PreIndexType = CurrIndexType
    for i in range(len(lstOfLevel)):
        PartOfStructureNumber += '_' + str(lstOfLevel[i])
    return PartOfStructureNumber
def AddTextToFile (csvFile,structure ,Text):
    csvFile.write("\"" + structure.replace("\"", "\"\"") + "\"" + ',' + "\"" + Text.replace("\"", "\"\"") + "\"" + '\n')
def isNumberingFormating (textBeforeStrip):
    global CurrIndexType
    text = textBeforeStrip.strip()
    CurrIndexType = -1
    formatNumber = text.strip().split(' ')[0]
    if (formatNumber.startswith('(')):
        formatNumber = formatNumber.replace('(','').replace(')','').replace(']','').replace('[','').strip()
        if (formatNumber.isdigit()):
            if formatNumber in arrayOfNumbers:
                checkForTenExistance(int(formatNumber),textBeforeStrip)
            else:
                CurrIndexType = 0
        elif (formatNumber in arrayOfSmallLetters):
            CurrIndexType = 1
        elif (formatNumber in arrayOfCAPLetters):
            CurrIndexType = 2
        elif (formatNumber in arrayOfDoubleSmallLetters):
            CurrIndexType = 3
        elif (formatNumber in arrayOfDoubleCAPLetters):
            CurrIndexType = 4
        elif (formatNumber in arraySmallofLatinNumbering):
            CurrIndexType = 5
        elif (formatNumber in arrayCapofLatinNumbering):
            CurrIndexType = 6
        elif ('.' in formatNumber):
            numbers = formatNumber.split('.')
            CurrIndexType = 8
            for n in numbers:
                if (not n.isdigit()):
                    CurrIndexType = -1
                    break
        elif (formatNumber in arrayOfNumbers):
            CurrIndexType = 10
    if (text.startswith('--')):
        CurrIndexType = 7
    elif (text.startswith('-')):
        CurrIndexType = 9
def ResetIndex ():
    index = 0
    global PreIndexType
    global CurrIndexType
    global lstOfPreIndexTypes
    global lstOfLevel
    global lstOfNumbersBrackets
    global nCurrSmallLetters 
    global nCurrCAPLetters 
    global nCurrSmallDoubleLetters 
    global nCurrCAPDoubleLetters
    global nCurrsmallLatinLetters
    global nCurrCAPLatinLetters
    global nCurrNumber
    global nCurrDoubleDash
    global nCurrSubNumber
    global nCurrSubNumberDash
    global nCurrArrNumbers
    nCurrNumber = 0
    nCurrSmallLetters = -1
    nCurrCAPLetters = -1
    nCurrSmallDoubleLetters = -1
    nCurrCAPDoubleLetters = -1
    nCurrsmallLatinLetters = -1
    nCurrCAPLatinLetters = -1
    nCurrArrNumbers = -1
    nCurrDoubleDash = 0
    nCurrSingleDash = 0
    for int in lstOfPreIndexTypes:
        if int == 0 and nCurrNumber == 0:
            nCurrNumber = lstOfLevel[index] + 1
        elif int == 1:
            nCurrSmallLetters = lstOfLevel[index]
        elif int == 2:
            nCurrCAPLetters = lstOfLevel[index]
        elif int == 3:
            nCurrSmallDoubleLetters = lstOfLevel[index]
        elif int == 4:
            nCurrCAPDoubleLetters = lstOfLevel[index]
        elif int == 5:
            nCurrsmallLatinLetters = lstOfLevel[index]
        elif int == 6:
            nCurrCAPLatinLetters = lstOfLevel[index]
        elif int == 7:
            nCurrDoubleDash = lstOfLevel[index] + 1
        elif int == 8:
            nCurrSubNumber = lstOfLevel[index] + 1
        elif int == 9:
            nCurrSingleDash = lstOfLevel[index] + 1
        elif int == 10:
            nCurrArrNumbers = lstOfLevel[index]
        index = index + 1
    if (nCurrSmallLetters == 26):
        nCurrSmallLetters = 0
    if (nCurrCAPLetters== 26):
        nCurrSmallLetters = 0
    if (nCurrsmallLatinLetters == 20):
        nCurrSmallLetters = 0
    if (nCurrCAPLatinLetters == 20):
        nCurrSmallLetters = 0
    if (nCurrCAPDoubleLetters == 26):
        nCurrSmallLetters = 0
    if (nCurrSmallDoubleLetters == 26):
        nCurrSmallLetters = 0
    if (nCurrArrNumbers == 9):
        nCurrSmallLetters = 0
def checkForTenExistance (number, text):
    global CurrIndexType
    arrayOfText = []
    lstofNumbers = []
    if ('('+str(number)+')' in text.strip()):
        arrayOfText = text.split('('+str(number)+')')
        lstofNumbers = lstOfNumbersBrackets
    elif ('['+str(number)+']' in text.strip()):
        arrayOfText = text.split('['+str(number)+']')
        lstofNumbers = lstOfNumbersSquare
    lengthOfi = len(arrayOfText[0])
    if (lengthOfi != lstofNumbers[number//11 - 1]):
        CurrIndexType = 10
    else:
        CurrIndexType = 0
        lstofNumbers[number//11 - 1] = 0
webDriver = webdriver.Chrome()
webDriver.maximize_window()
webDriver.get('http://library.amlegal.com/nxt/gateway.dll/Texas/dallas/cityofdallastexascodeofordinances?f=templates$fn=default.htm$3.0$vid=amlegal:dallas_tx')

# wait for visible price to have "Kr." text
print ('############## Task Started ###############')
webDriver.switch_to.frame('contents')
Chapter51ADallas = []
CodeCompativeTable = []
print ('############## Extracting Articles ###########')
try:
    webDriver.find_element_by_xpath('//div[@id = "Texas/dallas/cityofdallastexascodeofordinances/volumeiii"]//img[@class = "plusminus"]').click()
    while True:
        try:
            webDriver.find_element_by_xpath('//div[@id = "Texas/dallas/cityofdallastexascodeofordinances/volumeiii/chapter51adallasdevelopmentcodeordinance"]//img[@class = "plusminus"]').click()
            webDriver.find_element_by_xpath('//div[@id = "Texas/dallas/cityofdallastexascodeofordinances/volumeiii/chapter51adallasdevelopmentcodeordinance"]//div[@class="treenode"]')
            Chapter51ADallas = webDriver.find_elements_by_xpath('//div[@id = "Texas/dallas/cityofdallastexascodeofordinances/volumeiii/chapter51adallasdevelopmentcodeordinance"]//div[@class="treenode"]')
            break
        except:
            try:
                webDriver.find_element_by_xpath('//div[@id = "Texas/dallas/cityofdallastexascodeofordinances/volumeiii/chapter51adallasdevelopmentcodeordinance"]//img[@class = "plusminus"]').click()
                webDriver.find_element_by_xpath('//div[@id = "Texas/dallas/cityofdallastexascodeofordinances/volumeiii/chapter51adallasdevelopmentcodeordinance"]//div[@class="treenode"]')
                Chapter51ADallas = webDriver.find_elements_by_xpath('//div[@id = "Texas/dallas/cityofdallastexascodeofordinances/volumeiii/chapter51adallasdevelopmentcodeordinance"]//div[@class="treenode"]')
                break
            except:
                pass
    while True:
        try:
            webDriver.find_element_by_xpath('//div[@id = "Texas/dallas/cityofdallastexascodeofordinances/volumeiii/codecomparativetable0"]//img[@class = "plusminus"]').click()
            webDriver.find_element_by_xpath('//div[@id = "Texas/dallas/cityofdallastexascodeofordinances/volumeiii/codecomparativetable0"]//div[@class = "treenode"]')
            CodeCompativeTable = webDriver.find_elements_by_xpath('//div[@id = "Texas/dallas/cityofdallastexascodeofordinances/volumeiii/codecomparativetable0"]//div[@class="treenode"]')
            break
        except:
            try:
                webDriver.find_element_by_xpath('//div[@id = "Texas/dallas/cityofdallastexascodeofordinances/volumeiii/codecomparativetable0"]//img[@class = "plusminus"]').click()
                webDriver.find_element_by_xpath('//div[@id = "Texas/dallas/cityofdallastexascodeofordinances/volumeiii/codecomparativetable0"]//div[@class = "treenode"]')
                CodeCompativeTable = webDriver.find_elements_by_xpath('//div[@id = "Texas/dallas/cityofdallastexascodeofordinances/volumeiii/codecomparativetable0"]//div[@class="treenode"]')
                break
            except:
                pass
    ChaptersList = []
    for element in Chapter51ADallas:
        ChaptersList.append(element)
    for element in CodeCompativeTable:
        ChaptersList.append(element)
    for article in ChaptersList:
        index = 0
        articleText = article.text
        article.click()
        print ('>>>> Checking of Existence Item :' + articleText)  
        webDriver.switch_to.window(webDriver.window_handles[0]);
        webDriver.switch_to.frame('main')
        webDriver.switch_to.frame('docbody')
        OutputPath = 'OutputFile_'+ articleText.replace(',','').replace(':','')+'.csv'
        if os.path.exists(os.path.dirname(os.path.realpath(__file__)) +'\\' +OutputPath) is True:
                    if os.stat(os.path.dirname(os.path.realpath(__file__)) +'\\' +OutputPath).st_size > 0 :
                        webDriver.switch_to.window(webDriver.window_handles[0]);
                        webDriver.switch_to.frame('contents')
                        time.sleep(10)
                        continue
        print ('>>>>>> Creating Output File')
        csvFile = open(OutputPath, 'w+', encoding="utf-8")
        columnTitleRow = "Structure, Text\n"
        csvFile.write(columnTitleRow)
        print ('>>>>>> Processing the data extracted ..')
        try:
          txtSectionNamePart1 = ''
          txtSectionNamePart2 = ''
          if ('CHAPTER 51' in articleText):
              txtSectionNamePart1 = 'CHAPTER 51'
              txtSectionNamePart2 = 'DALLAS DEVELOPMENT CODE'
          DivsSectionandNormalLevels = webDriver.find_elements_by_xpath('//div')
          for div in DivsSectionandNormalLevels:
              if div.get_attribute("class") == 'Section': #New Section is detected
                if index > 0:
                     print ('>>>>>> Details of Section has been added .. ')
                     index += 1
                nCurrZeroSpacingbrackets = 0
                nCurrZeroSpacingSquare = 0
                nCurrwSpacing = 0
                nCurrWSpacing = 0
                nCurrWWSpacing = 0
                nCurrwwSpacing = 0
                nCurruSpacing  = 0
                nCurrUSpacing = 0
                nCurruuSpacing  = 0
                nCurrUUSpacing = 0
                nCurrHSpacing = 0
                nCurrHHSpacing = 0
                nCurrhSpacing = 0
                nCurrhhSpacing = 0
                nISpace = 0
                lstOfPreIndexTypes = []
                lstOfLevel = []
                lstOfNumbersBrackets = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                PreIndexType = -2
                CurrIndexType = -2
                nCurrSmallLetters = 0
                nCurrCAPLetters = 0
                nCurrArrNumbers = 0
                nCurrSmallDoubleLetters = 0
                nCurrCAPDoubleLetters = 0
                nCurrsmallLatinLetters = 0
                nCurrCAPLatinLetters = 0
                nCurrNumber = 1
                nCurrDoubleDash = 1
                nCurrSubNumber = 1
                nCurrSubNumberDash = 1
                doneAdded = 0
                Sectionelement = div.find_elements_by_xpath('.//div//a')
                txtSectionNamePart1 = 'SEC. '
                txtSectionNamePart2 = ''
                for element in Sectionelement:
                    try:
                        if element.get_attribute("title"):
                            txtSectionNamePart1 += element.get_attribute("title")
                            break
                    except:
                        pass
                txtSectionNamePart2 = div.text.replace(txtSectionNamePart1 + '.', '').strip()
                doneAdded = 0
                stringToWrite = "\"" +  txtSectionNamePart1.replace("\"", "\"\"").strip() +"\""  + ',' + "\"" +  txtSectionNamePart2.replace("\"", "\"\"").strip() +"\""
                csvFile.write(stringToWrite + '\n')
                print ('>>>>>> Section: '+ txtSectionNamePart1 + ' ' + txtSectionNamePart2 +' has been added .. ')
              elif div.get_attribute("class") == 'Normal-Level':
                #here is the add of normal level
                try:
                    txtHeader = ''
                    div.find_element_by_xpath('./div//table')
                    try:
                        HeadersElemenets = div.find_elements_by_xpath('./div[@style = "margin-bottom=10pt"]//table//tbody//tr')
                        rowCount = 0
                        for el in HeadersElemenets:
                            try:
                                if el.find_element_by_xpath('./td//div').get_attribute("class") == 'Table-Header':
                                    for elHeader in el.find_elements_by_xpath('./td//div[@class = "Table-Header"]'):
                                        try:    
                                            txtHeader += "\"" + elHeader.text+"\"" + ','
                                        except:
                                            pass
                                else:
                                    if rowCount == 0 and txtHeader != '':
                                        PartOfStructure =  txtSectionNamePart1.replace("\"", "\"\"").strip()
                                        for i in range(len(lstOfLevel)):
                                            PartOfStructure += '_' + str(lstOfLevel[i])
                                        PartOfStructure += '_1'
                                        csvFile.write("\"" + PartOfStructure + "\"" +',' + txtHeader + '\n')
                                        print('>>>>>>>>>> ' + PartOfStructure)
                                    BodyElemenetsCol = el.find_elements_by_xpath('./td//div//span')
                                    txtBody = ''
                                    for elCol in BodyElemenetsCol:
                                        try:
                                            txtBody += "\"" + elCol.text + "\"" + ','
                                        except:
                                            pass
                                    if txtHeader.startswith('""') or txtHeader == '':
                                        txtHeader = txtBody
                                    else:
                                        rowCount += 1
                                        csvFile.write("\"" + PartOfStructure + '_' + str(rowCount) +"\"" +','+ txtBody + '\n')
                                        print('>>>>>>>>>> ' + PartOfStructure+ '_' + str(rowCount))
                            except:
                                pass
                        
                    except Exception as e:
                        print(str(e))
                except:
                    NormalLevelText = div.text
                    arrayOfText = []
                    if NormalLevelText.strip().startswith ('(h)'):
                        arrayOfText = NormalLevelText.split('(h)')
                        nCurrhSpacing = len(arrayOfText[0])
                    elif NormalLevelText.strip().startswith ('(hh)'):
                        arrayOfText = NormalLevelText.split('(hh)')
                        nCurrhhSpacing = len(arrayOfText[0])
                    elif NormalLevelText.strip().startswith ('(H)'):
                        arrayOfText = NormalLevelText.split('(H)')
                        nCurrHSpacing = len(arrayOfText[0])
                    elif NormalLevelText.strip().startswith ('(HH)'):
                        arrayOfText = NormalLevelText.split('(HH)')
                        nCurrHHSpacing = len(arrayOfText[0])
                    elif NormalLevelText.strip().startswith ('(u)'):
                        arrayOfText = NormalLevelText.split('(u)')
                        nCurruSpacing = len(arrayOfText[0])
                    elif NormalLevelText.strip().startswith ('(uu)'):
                        arrayOfText = NormalLevelText.split('(uu)')
                        nCurruuSpacing = len(arrayOfText[0])
                    elif NormalLevelText.strip().startswith ('(U)'):
                        arrayOfText = NormalLevelText.split('(U)')
                        nCurrUSpacing = len(arrayOfText[0])
                    elif NormalLevelText.strip().startswith ('(UU)'):
                        arrayOfText = NormalLevelText.split('(UU)')
                        nCurrUUSpacing = len(arrayOfText[0])
                    elif NormalLevelText.strip().startswith ('(w)'):
                        arrayOfText = NormalLevelText.split('(w)')
                        nCurrwSpacing = len(arrayOfText[0])
                    elif NormalLevelText.strip().startswith ('(W)'):
                        arrayOfText = NormalLevelText.split('(W)')
                        nCurrWSpacing = len(arrayOfText[0])
                    elif NormalLevelText.strip().startswith ('(ww)'):
                        arrayOfText = NormalLevelText.split('(ww)')
                        nCurrwwSpacing = len(arrayOfText[0])
                    elif NormalLevelText.strip().startswith ('(WW)'):
                        arrayOfText = NormalLevelText.split('(WW)')
                        nCurrWWSpacing = len(arrayOfText[0])
                    elif NormalLevelText.strip().startswith ('(0)'):
                        arrayOfText = NormalLevelText.split('(0)')
                        nCurrZeroSpacingbrackets = len(arrayOfText[0])
                    elif NormalLevelText.strip().startswith ('[0]'):
                        arrayOfText = NormalLevelText.split('[0]')
                        nCurrZeroSpacingSquare = len(arrayOfText[0])
                    else:
                        for txtNum in arrayOfNumbers:
                            intNum = int(txtNum)
                            num = intNum - (intNum // 11)
                            if NormalLevelText.strip().startswith ('('+str(num )+')'):
                                arrayOfText = NormalLevelText.split('('+str(num)+')')
                                nNum = (int(num)//10 - 1)
                                nCurrSpacing = len(arrayOfText[0])
                                lstOfNumbersBrackets[nNum] = nCurrSpacing
                                break
                            elif NormalLevelText.strip().startswith ('['+str(num)+']'):
                                arrayOfText = NormalLevelText.split('['+str(num)+']')
                                nNum = (int(num)//10 - 1)
                                nCurrSpacing = len(arrayOfText[0])
                                lstOfNumbersSquare[nNum] = nCurrSpacing
                                break
                    if (txtSectionNamePart1 == 'SEC. 51A-4.402') and doneAdded == 0:
                        WorkOnSectionPartFn(csvFile, '(a) General provisions.', txtSectionNamePart1)
                        doneAdded = 1
                    WorkOnSectionPartFn( csvFile, NormalLevelText, txtSectionNamePart1)
          webDriver.switch_to.window(webDriver.window_handles[0]);
          webDriver.switch_to.frame('contents')
        except Exception as e:
            print(str(e))
        csvFile.close()
except Exception as e:
        print(str(e))