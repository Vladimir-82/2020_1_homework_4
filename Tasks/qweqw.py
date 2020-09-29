def find_even_numbers(limit):
    even_list=[i for i in range(limit+1) if i%2==0]
    print(even_list[1:])

num=int(input('Enter a number:'))
find_even_numbers(num)


