import requests, os, bs4, time
print('===10===|===3===|===10-1===|===3-1===|===10+-===|===3+-===|===1234===|===10226770===')
cash1 = 0
cash2 = 0
cash3 = 0
cash4 = 0
cash5 = 0
cash6 = 0
cash7 = 0
cash8 = 0
check = 0
numset1 = [1,2,3,4]
numset2 = [10,22,67,70]

while True:

    url = "https://www.lotto.pl/keno/wyniki-i-wygrane/ostatnie-wyniki"
    res = requests.get(url)
    res.raise_for_status()
    soup= bs4.BeautifulSoup(res.text, features= 'html.parser')

    tab = []
    tabnum = []

    for hit in soup.find_all(attrs={"class": "number text-center"}):
        tab.append(hit.text.strip())
    for hit in soup.find_all(attrs={"class": "wynik not_last"}):
        tabnum.append(hit.text.strip())

    first = tab[:20]
    tab2 = tab[:60]
    #print(first)
    try:
        if checker == tabnum[0][:6]:
            raise Exception
        score = 0
        for numb in numbers1:
            if numb in first:
                score += 1
        if score == 0: cash1 -= 2
        if score == 1: cash1 -= 2
        if score == 3: cash1 += 2
        if score == 4: cash1 += 58
        score = 0
        for numb in numbers2:
            if numb in first:
                score += 1
        if score == 0: cash2 -= 2
        if score == 1: cash2 -= 2
        if score == 3: cash2 += 2
        if score == 4: cash2 += 58
        score = 0
        for numb in numbers1:
            if str(int(numb)-1) in first:
                score += 1
        if score == 0: cash3 -= 2
        if score == 1: cash3 -= 2
        if score == 3: cash3 += 2
        if score == 4: cash3 += 58
        score = 0
        for numb in numbers2:
            if str(int(numb)-1) in first:
                score += 1
        if score == 0: cash4 -= 2
        if score == 1: cash4 -= 2
        if score == 3: cash4 += 2
        if score == 4: cash4 += 58
        score = 0
        for numb in numbers1:
            if str(int(numb)-1+check) in first:
                score += 1
        if score == 0: cash5 -= 2
        if score == 1: cash5 -= 2
        if score == 3: cash5 += 2
        if score == 4: cash5 += 58
        score = 0
        for numb in numbers2:
            if str(int(numb)-1+check) in first:
                score += 1
        if score == 0: cash6 -= 2
        if score == 1: cash6 -= 2
        if score == 3: cash6 += 2
        if score == 4: cash6 += 58
        score = 0
        for numb in numset1:
            if str(numb) in first:
                score += 1
        if score == 0: cash7 -= 2
        if score == 1: cash7 -= 2
        if score == 3: cash7 += 2
        if score == 4: cash7 += 58
        score = 0
        for numb in numset2:
            if str(numb) in first:
                score += 1
        if score == 0: cash8 -= 2
        if score == 1: cash8 -= 2
        if score == 3: cash8 += 2
        if score == 4: cash8 += 58

        print(str(cash1) + ' ' * (8 - len(str(cash1))) + '|' + str(cash2) + ' ' * (7 - len(str(cash2))) + '|' +
              str(cash3) + ' ' * (10 - len(str(cash3))) + '|' + str(cash4) + ' ' * (9 - len(str(cash4))) + '|' +
              str(cash5) + ' ' * (10 - len(str(cash5))) + '|' + str(cash6) + ' ' * (9 - len(str(cash6))) + '|' +
              str(cash7) + ' ' * (10 - len(str(cash7))) + '|' + str(cash8) + ' ' * (13 - len(str(cash8))))
    except Exception as e:
        #print(e)
        pass

    numbers1 = []
    numbers2 = []

    for a in range(4):
        max = 0
        for i in tab:
            if max < tab.count(i) and i not in numbers1:
                max = tab.count(i)
                x = i
        numbers1.append(x)
        max1 = 0
        for i in tab2:
            if max1 < tab2.count(i) and i not in numbers2:
                max1 = tab2.count(i)
                x = i
        numbers2.append(x)

    if check == 0:
        check = 2
    else:
        check = 0


    #print(tabnum[0][:6])
    #print(numbers1)
    #print(numbers2)
    checker = tabnum[0][:6]
    #print(numbers1)
    #print(numbers2)
    time.sleep(100)
