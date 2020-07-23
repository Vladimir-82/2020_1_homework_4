'''
Мне нравится 👍
Создайте функцию, которая, принимая массив имён, возвращает строку описывающая количество лайков (как в Facebook).

def likes(*arr: str) -> str:
    pass
Примеры:

likes() -> "no one likes this"
likes("Peter") -> "Peter likes this"
likes("Jacob", "Alex") -> "Jacob and Alex like this"
likes("Max", "John", "Mark") -> "Max, John and Mark like this"
likes("Alex", "Jacob", "Mark", "Max") -> "Alex, Jacob and 2 others like this"
Бонусные очки
Функция работает на нескольких языках и кодировках - язык ответа определяется по языку входного массива.
'''
EN_ALFABET='a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
BY_ALFABET='а','б','в','г','д','дж','дз','е','ё','ж','з','і','й','к','л','м','н','о','п','р','с','т','у','ў','ф','х','ц','ч','ш','ъ','ы','э','ю','я'
RU_ALFABET='а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я'


def alfabet(var):
    text=var.lower()
    for i in text:
        if i in EN_ALFABET:
            return 'EN'
        elif i in BY_ALFABET:
            return 'BY'
        elif i in RU_ALFABET:
            return 'RU'
        else:
            return 'EN'


def likes(var:str, alfabet):
    if len(var)==0:
        if alfabet(var)=='EN':
            result = "no one likes this"
        elif alfabet(var) == 'BY':
            result = "Гэта нікому не падабаецца"
        elif alfabet(var) == 'RU':
            result = "Это не нравится никому"

    #elif len(var)==1:
        #if alfabet(var)=='EN':
            result = (f'{var} likes this')
        #elif alfabet(var) == 'BY':
            #result = (f'{var} падабаецца гэта')
        #elif alfabet(var) == 'RU':
            #result = (f'{var} нравится это')


    elif len(var) == 2:
        if alfabet(var) == 'EN':
            result = (f'{var[0]} and {var[1]} like this')
        elif alfabet(var) == 'BY':
            result = (f'{var[0]} and {var[1]} падабаецца гэта')
        elif alfabet(var) == 'RU':
            result = (f'{var[0]} and {var[1]} нравится это')


    elif len(var) == 3:
        if alfabet(var) == 'EN':
            result = (f'{var[0]}, {var[1]} and {var[2]} like this')
        elif alfabet(var) == 'BY':
            result = (f'{var[0]}, {var[1]} and {var[2]} падабаецца гэта')
        elif alfabet(var) == 'RU':
            result = (f'{var[0]}, {var[1]} and {var[2]} нравится это')


    else:
        if alfabet(var) == 'EN':
            result = (f'{var[0]}, {var[1]} and {len(var[2::])} others like this')
        elif alfabet(var) == 'BY':
            result = (f'{var[0]}, {var[1]} and {len(var[2::])} падабаецца гэта')
        elif alfabet(var) == 'RU':
            result = (f'{var[0]}, {var[1]} and {len(var[2::])} нравится это')


    return result

var =("Alex", "Jacob")

result =likes(var, alfabet)

print(result)