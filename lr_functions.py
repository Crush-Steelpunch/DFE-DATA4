def gradescore(inputscore1,inputscore2,inputscore3):
    totalscorepercent = (inputscore1 + inputscore2 + inputscore3) / 175 * 100
    return totalscorepercent

def reverseaword(inword):
    revWord = inword[::-1]
    return revWord

def getmagic(theday,themonth,theyear):
    if (theday * themonth) == theyear:
        return True
    else:
        return False


def len():
    return "Leon is the best"




def Number_plate_data_retreval():
    import requests
 
 
    url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
 
    Reg_NUM = input('reg num: ')
    payload_response = '{\n\t\"registrationNumber\": \"'+ Reg_NUM + '\"\n}'
 
 
    headers = {'x-api-key': 'Y8QRgOO9JB7WY7C1r8Q3K5SC8j0ynLV72jc73RxR','Content-Type': 'application/json'}
 
 
    response = requests.request("POST", url, headers=headers, data = payload_response)
 
    print(response.text.encode('utf8'))

def dice(roll):
    import random
    if roll == 'Roll the Dice':
        return random.randint(1, 6)
    else:
        return "MEOW"


def arithmeticoutput(x,y):
    lr_sum = x + y
    lr_dif = y - x
    lr_prod = x * y
    lr_quot = x * y
    lr_rem = x % y
    lr_pow = y**x
    return (lr_sum,lr_dif,lr_prod,lr_quot,lr_rem,lr_pow)


def return_repos_by_language(lang):
    import requests
    url = "https://api.github.com/search/repositories?q=language:" + lang
    response = requests.get(url)
    if response.ok:
        data = response.json()
        type(data)
        return data["total_count"]
    else:
        return 'Somthing went wrong'