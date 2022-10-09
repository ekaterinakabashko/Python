# Задание 1
#Функция splitLines должна возвращать список lines из отдельных строк в коде пользователя
def splitLines(code):
    res = []
    code = code.split('\n')
    for line in code:
        res.append(line)
    return res

# Задание 2
#Функция countFuncs должна возвращать переменную funcsAmount, равную кол-ву строк, в которых объявляются неанонимные функции (т.е. функции, которые начинаются с ключевого слова def)
import re
def countFuncs(code):
    shet = 0
    code = code.split('\n')
    for i in code:
        print (i)
        if re.findall('^def\s.*', i):
            shet +=1
    return shet

# Задание 3
#Функция clearLines должна возвращать список lines, в которых код пользователя разбит по строкам (как в пункте 1), но из начала и конца каждой строки должны быть убраны лишние пробелы.
import re
def clearLines(code):
    res = []
    code = code.split('\n')
    for line in code:
        res.append(line.strip())
    return res

# Задание 4
#Функция deleteLibs должна удалять из кода пользователя все строки, в которых присутствует команда import, а после нее название библиотеки. Функция должна возвращать исправленный код.
def deleteLibs(code):
    code = code.split('\n')
    res = []
    allowedLibs = ['pandas', 'numpy']
    for line in code:
        if line != '':
            for i in allowedLibs:
                if line not in res:
                    if i in line:
                        res.append(line)
                    if not i in line and not'import' in line:
                        res.append(line)
    return res


# Задание 5
#Функция deleteCommands должна удалять из кода пользователя все строки, в которых присутствуют команды exec или eval. Функция должна возвращать исправленный код.
import re
def deleteCommands(code):
    code = code.split('\n')
    res = []
    for line in code:
        res.append(re.sub(r'exec$|eval$', '', line))
    return (res)


# Задание 6
#Функция countWords должна считать количество раз, которое каждое слово встречается в коде пользователя. Функция должна возвращать словарь вида {word: amount}.
import re
def countWords(code):
    code = re.sub(r'[^\w\s]', '', code) # ^\w\s allows us to select anything that isn’t a word or a whitespace, which in our case, it selects punctuation.
    counts = dict()
    words = code.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

# Задание 7
#Функция uniqueLines должна принимать на вход код пользователя и возвращать список из уникальных слов (т.е. если одно слово встречается несколько раз, то необходимо включить его в список только один раз).
import re
def uniqueLines(code):
    code = re.sub(r'[^\w\s]', '', code)
    code = sorted(set(code.split()))
    return code

# Задание 8
#Функция reverseWords должна принимать на вход код пользователя и формировать словарь вида {word: reversed_word}. Здесь reversed_word - слово, перевернутое задом наперед. Помимо этого, функция должна быть задокументирована, т.е. при вызове reversed_word.__doc__ должна возвращаться документация к функции.
import re
def reverseWords(code):
    """Функция reverseWords принимает код пользователя. Возвращаемое значение: словарь."""
    code = re.sub(r'[^\w\s]', ' ', code)
    words = code.split()
    newWords = [word[::-1] for word in words]
    return dict(zip(words,newWords))

# Задание 9
#Функция checkCode должна принимать на вход произвольное количество позиционных и именованных аргументов. В случае, если среди именнованных аргументов нет аргумента code , необходимо возбудить исключение TypeError: checkCode() needs 'code' keyword argument . В случае, если такой именованный аргумент присутствует, необходимо проверить, является ли code строкой. Если не является, необходимо возбудить исключение TypeError . Если является, вернуть True .
def checkCode(*args, **kwargs):
        if 'code' not in kwargs:
            raise TypeError('checkCode() needs "code" keyword argument.')
        else:
            if isinstance('code', str):
                print(isinstance('code', str))
            else:
                raise TypeError('TypeError')

# Задание 10
#Генератор lineGenerator, который будет принимать на вход код пользователя и отдавать по одной строке.
def lineGenerator(code):
    code = code.split('\n')
    for i in code:
        yield i
