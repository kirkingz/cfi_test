import pytest

@pytest.fixture()
def sum(a=3, b=2):
    """функция считает сумму двух значений a и b"""
    sum = a + b
    return sum

@pytest.fixture()
def welcom(name='Артем'):
    """функция выводит привествие с задаваемым параметром name"""
    return print('Привет', name)

@pytest.fixture()
def draw_box(height=4, width=7):
    """функция рисует прямоугольник с параметрами height - высота, с - ширина"""
    for i in range(height):
        print('*' * width)

@pytest.fixture()
def list():
    """функция добавляет новое значение в список и выводит max и min значение в списке"""
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l.append(11)
    print("Максмальное число в списке:", max(l))
    print("Минимальное число в списке:",min(l))
    return l

@pytest.fixture()
def login_password():
    """функция выводит значения по ключу"""
    dict = {"ba": 2022, "Виктор": 1234, "max100500": 21031993}
    print(dict.get("ba"))
    return dict.get("ba")

@pytest.fixture()
def tup():
    """функция определяет количество вхождений определенного элемента в кортеже."""
    p_tup = (5,"Лондон", 101,"Пекин", 42, 3,"Москва", 101, 224,"Париж",101)
    print(p_tup.count(101))
    return p_tup.count(101)

@pytest.fixture()
def months():
    """функция соединяет два множества"""
    months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
    months_b = set(["July", "Aug", "Sep", "Oct", "Nov", "Dec"])
    all_months = months_a.union(months_b)
    print(all_months)
    return all_months