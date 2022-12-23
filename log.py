from model import get_info as info

def read_contact():
    with open('Phonebook.csv', 'r', encoding='utf=8') as f:  # открываем файл на чтение
        return f.read()

def writing_scv (info):
    file = 'phonebook.csv'
    with open (file, 'a', encoding='utf=8') as data: # открываем файл на запись, преобразовываем в unicode-строку 
        data.write(f'Last name: {info[0]}; First name {info[1]}; Phone number {info[2]}; Discriotion {info[3]}\n')
        # и записываем в файл 

def writing_txt (info):
    file = 'phonebook.txt'
    with open (file, 'a', encoding='utf=8') as data: # открываем файл на запись, преобразовываем в unicode-строку 
        data.write(f'Last name: {info[0]}\n First name {info[1]}\n Phone number {info[2]}\n Discriotion {info[3]}\n\n') 
        # и записываем в файл   



