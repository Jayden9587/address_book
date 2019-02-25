val = input()

ch = ''
result =''
for i in val :
    if int(i)%2 == 0 :
        if ch == 'even':
            result += '*'
        ch = 'even'
    else :
        if ch == 'odd' :
            result += '-'
        ch = 'odd'
    result += i
print(result)
