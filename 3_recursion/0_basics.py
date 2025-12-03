def test_equal(val_1, val_2):
    print(val_1 == val_2)


# Конвертирование целого числа в строку по любому основанию от 2 до 16

def to_str(n, base):
    chars = "0123456789ABCDEF"
    if n < base:
        return str(n)
    else:
        return to_str(n // base, base) + chars[n % base]


test_equal(to_str(1453, 16), "5AD")
test_equal(to_str(10, 2), "1010")


# Напишите функцию, которая принимает строку в качестве параметра
# и возвращает её же, но задом наперёд.

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse(s[0:-1])


test_equal(reverse("hello"),"olleh")
test_equal(reverse("l"),"l")
test_equal(reverse("follow"),"wollof")
test_equal(reverse(""),"")


# Напишите функцию, которая принимает строку в качестве параметра
# и возвращает истину в случае палиндрома, ложь - в обратном.
# Напомним, что строка является ппалиндромом,
# если одинаково читается справа налево и слева направо.
# Например, radar - это палиндром.
# Словосочетания тоже могут быть палиндромами,
# но прежде из них нужно удалить все пробелы и знаки препинания.
# Например, madam i’m adam - это палиндром.
# Вот ещё несколько забавных палиндромов:
#
#     kayak
#     aibohphobia
#     Live not on evil
#     Reviled did I live, said I, as evil I did deliver
#     Go hang a salami; I’m a lasagna hog.
#     Able was I ere I saw Elba
#     Kanakanak – a town in Alaska
#     Wassamassaw – a town in South Dakota

def remove_white(s):
    spec_chars = ' .,?!@"\\\'`’:;-=+*/^%$#&()[]{}'
    if len(s) <= 1:
        return '' if s in spec_chars else s
    elif s[0] in spec_chars:
        return remove_white(s[1:])
    else:
        return s[0] + remove_white(s[1:])

def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0].lower() == s[-1].lower() and is_palindrome(s[1:-1])

test_equal(is_palindrome(remove_white("x")),True)
test_equal(is_palindrome(remove_white("radar")),True)
test_equal(is_palindrome(remove_white("hello")),False)
test_equal(is_palindrome(remove_white("")),True)
test_equal(is_palindrome(remove_white("hannah")),True)
test_equal(is_palindrome(remove_white("madam i'm adam")),True)
test_equal(is_palindrome(remove_white("kayak")),True)
test_equal(is_palindrome(remove_white("aibohphobia")),True)
test_equal(is_palindrome(remove_white("Live not on evil")),True)
test_equal(is_palindrome(remove_white("Reviled did I live, said I, as evil I did deliver")),True)
test_equal(is_palindrome(remove_white("Go hang a salami; I’m a lasagna hog.")),True)
test_equal(is_palindrome(remove_white("Able was I ere I saw Elba")),True)
test_equal(is_palindrome(remove_white("Kanakanak")),True)
test_equal(is_palindrome(remove_white("Wassamassaw")),True)
