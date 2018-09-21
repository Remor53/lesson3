if __name__ == '__main__':
    with open('C:\\projects\\lesson3\\referat.txt',
              'r', encoding='utf-8') as f1:
        text1 = f1.read()
        amount_word = len(text1.split())
        text2 = text1.replace('.', '!')
    with open('C:\\projects\\lesson3\\referat2.txt',
              'w', encoding='utf-8') as f2:
        f2.write(text2.replace('\n', ''))
