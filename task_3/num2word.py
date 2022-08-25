ones = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')

twos = ('Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')

tens = ('Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred')

suffixes = ('', 'Thousand', 'Million', 'Billion')

def process(number, index):
    
    if number=='0':
        return 'Zero'
    
    length = len(number)
    
    if(length > 3):
        return False
    
    number = number.zfill(3)
    words = ''
 
    hdigit = int(number[0])
    tdigit = int(number[1])
    odigit = int(number[2])
    
    words += '' if number[0] == '0' else ones[hdigit]
    words += ' Hundred ' if not words == '' else ''
    
    if(tdigit > 1):
        words += tens[tdigit - 2]
        words += ' '
        words += ones[odigit]
    
    elif(tdigit == 1):
        words += twos[(int(tdigit + odigit) % 10) - 1]
        
    elif(tdigit == 0):
        words += ones[odigit]

    if(words.endswith('Zero')):
        words = words[:-len('Zero')]
    else:
        words += ' '
     
    if(not len(words) == 0):    
        words += suffixes[index]
        
    return words;
    
def getWords(number):
    length = len(str(number))
    
    if length>12:
        return 'This program supports upto 12 digit numbers.'
    
    count = length // 3 if length % 3 == 0 else length // 3 + 1
    copy = count
    words = []
 
    for i in range(length - 1, -1, -3):
        words.append(process(str(number)[0 if i - 2 < 0 else i - 2 : i + 1], copy - count))
        count -= 1;

    final_words = ''
    for s in reversed(words):
        temp = s + ' '
        final_words += temp
    
    return final_words
# End Main Logic

# Reading number from user
number = int(input('Enter any number: '))
print('%d in words is: %s' %(number, getWords(number)))
def number_converter(number):
    numbers = {
            0:"ዜሮ",1:"አንድ",2:"ሁለት",3:"ሶስት",4:'አራት',5:'አምስት',6:'ስድስት',7:'ሰባት',8:'ስምንት',9:'ዘጠኝ',10:'አስር',11:'አስራ አንድ',\
            12:'አስራ ሁለት',13:'አስራ ሶስት',14:'አስራ አራት',15:'አስራ አምስት',16:'አስራ ስድስት',17:'አስራ ሰባት',18:'አስራ ስምንት',19:'አስራ ዘጠኝ',\
            20:'ሃያ',30:'ሰላሳ',40:'አርባ',50:'ሃምሳ',60:'ስልሳ',70:'ሰባ',80:'ሰማንያ',90:'ዘጠና'}
    if number < 20:
        return numbers[number]
    elif number < 100:
        if number % 10 == 0:
            return numbers[number]
        else:
            return numbers[number - (number % 10)] + f" {numbers[number % 10]}"
    elif number < 1000:
        if number % 100 == 0:
            return numbers[number // 100] + " መቶ"
        else:
            return numbers[number // 100] + " መቶ " + number_converter(number % 100)
    elif number < 1000000:
        if number % 1000 == 0:
            return number_converter(number // 1000) + " ሺህ"
        else:
            return number_converter(number // 1000) + " ሺህ" + f" {number_converter(number % 1000)}"
    elif number < 1000000000:
        if number % 1000000 == 0:
            return number_converter(number // 1000000) + " ሚሊዮን"
        else:
            return number_converter(number // 1000000) + " ሚሊዮን" + f" {number_converter(number % 1000000)}"
    elif number < 1000000000000:
        if number % 1000000000 == 0:
            return number_converter(number // 1000000000) + " ቢሊዮን"
        else:
            return number_converter(number // 1000000000) + " ቢሊዮን" + f" {number_converter(number % 1000000000)}"
input = input("ቁጥር አስገባ:")

try:
    num = int(input)
    print(number_converter(num))
except:
    print("እባክዎ ትክክለኛ ቁጥር ያስገቡ እና እንደገና ይሞክሩ")
