##CS 101
##Program 3 - Roman Numeral Calculator
##JJC7WB@mail.umkc.edu
##John Clement
##
##PROBLEM: I will be converting two roman numerals into a decimal and roman numeral sum and display it to the user.
##
##
##ALGORITHM...
##1. First, get an input string from the user as the first Roman Numeral to add and convert it to uppercase letters.
##2. Loop through the input string for meta-details, such as string length, valid characters, and patterns >> starting from lower numbers to higher number combinations
##3. I will be counting the number of C's in the output and thereby limiting the number automatically that it can get to
##4. I'll extract the number in the hundreds place and add that to the ending number so I just have to worry about conditions from 0-99.
##5. I'll loop through the input string one time from left of the string to right, checking all possible conditions
##6. based on the base_hundred amount whether 1,2,3 hundred... I'll start the counter when looping through nested loops.  this will be my dynamic counter 
##7. I'll give the user the option to re-enter the roman numeral with each one they enter.
##8. I will have three main functions and then an execution fragment of code which will run everything.  this will ensure organization.
##9. The first function will count the amount of C's (hundreds) in the roman numeral input.  The second will ensure not more than 3 c's can be inputted in the string.  The third function will calculate the roman numeral.
##    I will have a fourth function also for changing the decimal total back into a roman numeral.
##10. I will put everything in a while loop which will be the execution code fragment.  I will then provide the user with the total amount in decimal, and roman numeral.
##11. Then, the output will be displayed
##
##
##ERROR HANDLING:
##1. If there are any index errors in this for loop, then i'll just restart the for loop after sending it to the an exception handler to handle this
##    specific error type.
##2. I will be validating incorrect sequences of characters like XXXX, etc...
##3. For exception handling >> while validating the string... send it to an exception handler that breaks out of the calculation
##4. For exception handling concerned the calculation code, if at any point a index is referenced in the input string that doesnt exist >> break out of the calculation and output the total as it is.


    

##validate the amount of hundreds aloud for each roman numeral to be calculated
## and receive the two roman numerals as input
def get_first(number):
    if number == 1:
        inputaa = input("enter first rn").upper()
    elif number == 2:
        inputaa = input("enter second rn").upper()
    
    if inputaa.count('C') > 3:
        print("Invalid roman numeral entry")
        get_first()
    return inputaa



##Count how many C's are at the beginning of the Roman Numeral Input, so we know how many hundreds is going to be our base number + the calculated Roman numeral below 100....
def start1(inp):
    c_count = 0
    done_w = 0
    invalid_attempt = 0
    while done_w == 0:
        for ind, i in enumerate(inp):
            try:
                if i =='C':
                    c_count+=1
                    if inp[ind+1] == 'C':
                        c_count+=1
                        if inp[ind+2] == 'C':
                            c_count+=1
                        elif inp[ind+2] == 'X':
                            break
                    elif inp[ind+1] == 'X':
                        break
            except IndexError:
                pass
            break
        done_w = 1                
        
    return c_count





##change decimal number to roman numeral sum
def calculate_0_99_RN(resulta,resultb):
    total = resulta+resultb
    ##string version of the total, so we can use it to iterate over as a collection of characters
    stotal = str(resulta+resultb)
    ##appending roman numerals onto a list if the number calculated from the previous roman numerals met that condition
    output = []
    ##final string to output to user with the decimal number converted to a roman numeral sum
    results = ''
    counter1 = 0
    ##roman numeral numbers from 1-99
    roman_numerals = [
                      'I','II','III','IV','V','VI','VII','VIII','IX','X', 'XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX',
                      'XXI','XXII','XXIII','XXIV','XXV','XXVI','XXVII','XXVIII','XXIX','XXX',
                      'XXXI','XXXII','XXXIII','XXXIV','XXXV','XXXVI','XXXVII','XXXVIII','XXXIX','XL',
                      'XLI','XLII','XLIII','XLIV','XLV','XLVI','XLVII','XLVIII','XLIX','L',
                      'LI','LII','LIII','LIV','LV','LVI','LVII','LVIII','LIX','LX',
                      'LXI','LXII','LXIII','LXIV','LXV','LXVI','LXVII','LXVIII','LXIX','LXX',
                      'LXXI','LXXII','LXXIII','LXXIV','LXXV','LXXVI','LXXVII','LXXVIII','LXXIX','LXXX',
                      'LXXXI','LXXXII','LXXXIII','LXXXIV','LXXXV','LXXXVI','LXXXVII','LXXXVIII','LXXXIX', 'XC',
                      'XCI','XCII','XCIII','XCIV','XCV','XCVI','XCVII','XCVII','XCVIII','XCIX']


##whatever the first index of the stotal string collection is, append that as the hundreds value if the amount of characters in stotal is above 3.
## Otherwise, for 1 and 2 digit numbers, just read the correlating index in the roman_numerals array of values from 1-99
    if counter1 == 0:
        counter1 +=1
        if len(stotal) == 1:
            output.append(roman_numerals[total-1])
        elif len(stotal) == 2:
            output.append(roman_numerals[total-1])
        elif len(stotal) == 3:
            if stotal[0] == '1':
                output.append('C')
            elif stotal[0] == '2':
                output.append('CC')
            elif stotal[0] == '3':
                output.append('CCC')
            elif stotal[0] == '4':
                output.append('CD')
            elif stotal[0] == '5':
                output.append('D')
            elif stotal[0] == '6':
                output.append('DC')
            elif stotal[0] == '7':
                output.append('DCC')

            ##append the roman numeral at the index in the roman_numeral array that correlates to the decimal number in the tens and ones place of the number.
            output.append(roman_numerals[int(stotal[1]+stotal[2])-1])
            ##convert the list into one string with no spaces.
            results = "".join(output)
            ##output the results
            print("The roman numeral total is {}".format(results))
                      

    return results













def calculate_0_99(Number_Hundred, inputa):
    c = 'c'
    total = 0
    while total <= 380 and c == 'c':
        c = 'cc'
        base_Hundred = 0
        counter = 0 
        Number_Hundred_Int = str(Number_Hundred)
        base_Hundred = 0    

##check to see if the base hundred to append to the output results is 100,200, or 300        
        if Number_Hundred_Int == '0':
            base_Hundred = 0
        elif Number_Hundred_Int == '1':
            base_Hundred = 1
        elif Number_Hundred_Int == '2':
            base_Hundred = 2
        elif Number_Hundred_Int == '3':
            base_Hundred = 3

            
        if base_Hundred == 3:
            total += base_Hundred+297
        elif base_Hundred == 2:
            total += base_Hundred+198
        elif base_Hundred == 1:
            total += base_Hundred+99
        elif base_Hundred == 0:
            total += 0



            


        ##technicially loop through the entire string so that its scope is entirely available to read
        for index, i in enumerate(inputa):
            ##also, just loop through the number index where the base hundred starts to 
            if counter == 0:
                ##validate before calculating
                try:
                    ##validate that all the entered roman numeral characters are valid, and if not, break the program
                    for a in range(0, len(inputa)):
                        if inputa[a] == 'X':
                            pass                    
                        elif inputa[a] == 'L':
                            pass
                        elif inputa[a] == 'I':
                            pass
                        elif inputa[a] == 'V':
                            pass
                        elif inputa[a] == 'C':
                            pass
                        else:
                            raise Exception
                            
                ##break the program            
                except Exception:
                    print("exception raised")
                    if total == 0:
                        break

                ##For each nested condition of roman numerals from 1-99, check the conditions and add a number amount to the total, that matches the value of the roman numeral
                ##calculate, only run this once
                try:
                    #I to IX
                    counter = 1
                    if inputa[base_Hundred] == 'I':
                        total+=1
                        if inputa[base_Hundred+1] == 'I':
                            total+=1         
                            if inputa[base_Hundred+2] == 'I':
                                total+=1
                        elif inputa[base_Hundred+1] == 'V':
                            total+= 3
                        elif inputa[aa+1] == 'X':
                            total+=8
                    elif inputa[base_Hundred] == 'V':
                        total+=5
                        if inputa[base_Hundred+1] == 'I':
                            total+=1
                            if inputa[base_Hundred+2] == 'I':
                                total+=1
                                if inputa[base_Hundred+3] == 'I':
                                    total+=1        
                    ##X
                    elif inputa[base_Hundred] =='X':
                        total+=10
                        if inputa[base_Hundred+1] == 'I':
                            total+=1
                            if inputa[base_Hundred+2] == 'I':
                                total+=1
                                if inputa[base_Hundred+3] == 'I':
                                    total+=1
                            elif inputa[base_Hundred+2] == 'V':
                                total+=3
                            elif inputa[base_Hundred+2] == 'X':
                                total+=8
                        elif inputa[base_Hundred+1] == 'V':
                            total+=5
                            if inputa[base_Hundred+2] == 'I':
                                total+=1
                                if inputa[base_Hundred+3] == 'I':
                                    total+=1
                                    if inputa[base_Hundred+4] == 'I':
                                        total+=1
                        ##XX
                        elif inputa[base_Hundred+1] == 'X':
                            total+=10
                            if inputa[base_Hundred+2] == 'I':
                                total+=1
                                if inputa[base_Hundred+3] == 'I':
                                    total+=1
                                    if inputa[base_Hundred+4] == 'I':
                                        total+=1
                                elif inputa[base_Hundred+3] == 'V':
                                    total+=3
                                elif inputa[base_Hundred+3] == 'X':
                                    total+=8 
                            elif inputa[base_Hundred+2] == 'V':
                                total+=5
                                if inputa[base_Hundred+3] == 'I':
                                    total+=1
                                    if inputa[base_Hundred+4] == 'I':
                                        total+=1
                                        if inputa[base_Hundred+5] == 'I':
                                            total+=1
                            ##XXX
                            elif inputa[base_Hundred+2] == 'X':
                                total+=10
                                if inputa[base_Hundred+3] == 'I':
                                    total+=1
                                    if inputa[base_Hundred+4] == 'I':
                                        total+=1
                                        if inputa[base_Hundred+5] == 'I':
                                            total+=1
                                    elif inputa[base_Hundred+4] == 'V':
                                        total+=3
                                    elif inputa[base_Hundred+4] == 'X':
                                        total+=8 
                                elif inputa[base_Hundred+3] == 'V':
                                    total+=5
                                    if inputa[base_Hundred+4] == 'I':
                                        total+=1
                                        if inputa[base_Hundred+5] == 'I':
                                            total+=1
                                            if inputa[base_Hundred+6] == 'I':
                                                total+=1  


                      
                        ##XL
                        elif inputa[base_Hundred+1] == 'L':
                            total+=30
                            if inputa[base_Hundred+2] == 'I':
                                total+=1
                                if inputa[base_Hundred+3] == 'I':
                                    total+=1
                                    if inputa[base_Hundred+4] == 'I':
                                        total+=1
                                elif inputa[base_Hundred+3] == 'V':
                                    total+=3
                                elif inputa[base_Hundred+3] == 'X':
                                    total+=8 
                            elif inputa[base_Hundred+2] == 'V':
                                total+=5
                                if inputa[base_Hundred+3] == 'I':
                                    total+=1
                                    if inputa[base_Hundred+4] == 'I':
                                        total+=1
                                        if inputa[base_Hundred+5] == 'I':
                                            total+=1
                            elif inputa[base_Hundred+2] == 'X':
                                total+=10
                                if inputa[base_Hundred+3] == 'V':
                                    total+=5
                                    if inputa[base_Hundred+4] == 'I':
                                        total+=1
                                        if inputa[base_Hundred+5] == 'I':
                                            total+=1
                                            if inputa[base_Hundred+6] == 'I':
                                                total+=1
                                elif inputa[base_Hundred+3] == 'I':
                                    total+=1
                                    if inputa[base_Hundred+4] == 'I':
                                        total+=1
                                        if inputa[base_Hundred+5] == 'I':
                                            total+=1
                                elif inputa[base_Hundred+3] == 'X':
                                    total+=10
                                    if inputa[base_Hundred+4] == 'I':
                                        total+=1
                                        if inputa[base_Hundred+5] == 'I':
                                            total+=1
                                    elif inputa[base_Hundred+4] == 'X':
                                        total+=10
                                        if inputa[base_Hundred+5] == 'I':
                                            total+=1
                                            if inputa[base_Hundred+6] == 'I':
                                                total+=1
                                        elif inputa[base_Hundred+5] == 'V':
                                            total+=5
                                            if inputa[base_Hundred+6] == 'I':
                                                total+=1
                                                if inputa[base_Hundred+7] == 'I':
                                                    total+=1
                                    elif inputa[base_Hundred+4] == 'V':
                                        total+=5
                                        if inputa[base_Hundred+5] == 'I':
                                            total+=1
                                            if inputa[base_Hundred+6] == 'I':
                                                total+=1
                                            
                        
                        ##XC
                        elif inputa[base_Hundred+1] == 'C':
                            total+=80
                            if inputa[base_Hundred+2] == 'I':
                                total+=1
                                if inputa[base_Hundred+3] == 'I':
                                    total+=1
                                    if inputa[base_Hundred+4] == 'I':
                                        total+=1
                                elif inputa[base_Hundred+3] == 'V':
                                    total+=3
                                elif inputa[base_Hundred+3] == 'X':
                                    total+=8
                            elif inputa[base_Hundred+2] == 'V':
                                total+=5
                                if inputa[base_Hundred+3] == 'I':
                                    total+=1
                                    if inputa[base_Hundred+4] == 'I':
                                        total+=1
                                        if inputa[base_Hundred+5] == 'I':
                                            total+=1
                                
                                        
                            
                    ##L
                    elif inputa[base_Hundred] == 'L':
                        total+=50
                        if inputa[base_Hundred+1] == 'I':
                            total+=1
                            if inputa[base_Hundred+2] == 'I':
                                total+=1
                                if inputa[base_Hundred+3] == 'I':
                                    total+=1
                            elif inputa[base_Hundred+2] == 'V':
                                total+=3
                            elif inputa[base_Hundred+2] == 'X':
                                total+=8
                        ##LX
                        elif inputa[base_Hundred+1] == 'X':
                            total+=10
                            ##LXX
                            if inputa[base_Hundred+2] == 'X':
                                total+=10
                                ##LXXX
                                if inputa[base_Hundred+3] == 'X':
                                    total+=10
                                    ##LXXXI
                                    if inputa[base_Hundred+4] == 'I':
                                        total+=1
                                        if inputa[base_Hundred+5] == 'I':
                                            total+=1
                                            if inputa[base_Hundred+6] == 'I':
                                                total+=1
                                        elif inputa[base_Hundred+5] == 'X':
                                            total+=8
                                        elif inputa[base_Hundred+5] == 'V':
                                            total+=3
                                    ##LXXXV
                                    elif inputa[base_Hundred+4] == 'V':
                                        total+=3
                                        if inputa[base_Hundred+5] == 'I':
                                            total+=1
                                            if inputa[base_Hundred+6] == 'I':
                                                total+=1
                                                if inputa[base_Hundred+7] == 'I':
                                                    total+=1
                                ##LXXI
                                elif inputa[base_Hundred+3] == 'I':
                                    total+=1
                                    if inputa[base_Hundred+4] == 'I':
                                        total+=1
                                        if inputa[base_Hundred+5] == 'I':
                                            total+=1
                                    elif inputa[base_Hundred+4] == 'X':
                                        total+=8
                                ##LXXV
                                elif inputa[base_Hundred+3] == 'V':
                                    total+=5
                                    if inputa[base_Hundred+4] == 'I':
                                        total+=1
                                        if inputa[base_Hundred+5] == 'I':
                                            total+=1
                                            if inputa[base_Hundred+6] == 'I':
                                                total+=1
                            ##LXI
                            elif inputa[base_Hundred+2] == 'I':
                                total+=1
                                if inputa[base_Hundred+3] == 'I':
                                    total+=1
                                    if inputa[base_Hundred+4] == 'I':
                                        total+=1
                                elif inputa[base_Hundred+3] == 'X':
                                    total+=8
                                elif inputa[base_Hundred+3] == 'V':
                                    total+=3
                                    
                        elif inputa[base_Hundred+1] == 'V':
                            total+=5
                            if inputa[base_Hundred+2] == 'I':
                                total+=1
                                if inputa[base_Hundred+3] == 'I':
                                    total+=1
                                    if inputa[base_Hundred+4] == 'I':
                                        total+=1
                                        
    
                                     
                ##continue searching the conditions, re-starting the loop if a condition is checked outside of the bounds of the index in the total    
                except IndexError:
                    pass
                ##validate that each number is less than 380 for each Roman Numeral
                if total > 380:
                    print("invalid entry\n\n")
                    

    return total
                        

    



    
##used to check if the first roman numeral has been collected yet                    
resulta_collected = False
play_again = 'Y'


while play_again == 'Y':
    ##Get the first roman numeral to add
    inputa = get_first(1)
    ##count the amount of c's in the input
    num_h = start1(inputa)
    ##calculate the first roman numeral
    resulta = calculate_0_99(num_h, inputa)
    ##validate that the individual number inputted for the roman numeral is less than or equal to 380, as that is the limit for this program when it comes to each roman numeral.
    if resulta <= 380:
        play_again = input("Do you want to change your first number before we continue to getting the second roman numeral from you?").upper()
        if play_again != 'Y':
            ##once the first result is collected run the next bit of code
            resulta_collected = True
            if resulta_collected == True:
                play_again = ''
                print("entering result b calculation")
                ##Get the second roman numeral to add
                inputb = get_first(2)
                num_h = start1(inputb)
                ##calculate the roman numeral decimal amount of the first entered Roman numeral
                resultb = calculate_0_99(num_h, inputb)
                ##output the decimal total
                print("Decimal total is: {0}".format(resulta+resultb))
                calculate_0_99_RN(resulta,resultb)
                
        
        
        


    

    


    






    
