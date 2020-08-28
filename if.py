def words(a_string):
    some_list=a_string.split(' ')
    some_dict={i:len(i) for i in some_list}
    print(some_dict)

    max_value=max(some_dict.values())
    final_dict = {k: v for k, v in some_dict.items() if v == max_value}
    print(final_dict)





a_string='asdsad eee ttt'
words(a_string)