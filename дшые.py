def messange(mes):
    some_list=[]
    for i in mes:
        if i!=',':
            some_list.append(i)

    some_turple=tuple(some_list)
    print(some_list)
    print(some_turple)

text=input("Enter a messange:")
messange(text)