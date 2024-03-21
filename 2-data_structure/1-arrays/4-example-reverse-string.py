# revsere a string 

def reverse(string: str):
    if not string or len(string) < 2:
        return string
    res = ""
    for i in range(len(string) -1 , -1, -1):
        res += string[i]
    return res 



def reverse2(string: str):
    if not string or len(string) < 2:
        return string
    res = list(string)
    i = 0 
    j = len(res) -1 
    while i < j:
        res[i], res[j] = res[j], res[i]
        i +=1
        j -=1
    return "".join(res)


def reverse3(string: str):
    return string[::-1]


def reverse4(string: str):
    list_val = [*string]
    list_val.reverse()
    return "".join(list_val)

print(reverse('mousa') == reverse2('mousa') == reverse3('mousa')== reverse4('mousa')) 


