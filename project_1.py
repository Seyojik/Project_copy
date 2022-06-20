import shutil

# Исходный путь

src = input("Введите: ")
#'C:/Work/PyCharm/folders/src/'
dst = input("Введите: ")
#'C:/Work/PyCharm/folders/dst/'
# Путь назначения



shutil.copytree(src, dst, ignore=shutil.ignore_patterns('*.txt', 'in.html', '11'))

a = input('Введите: ')
if a == 'yes':
    shutil.rmtree(src)
elif a == 'no':
    print('Исходный файл не был удалён')