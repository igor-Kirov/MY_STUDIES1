

class WordsFinder():
    ar_name =[]
    def __init__(self, *fname):
        if len(*fname)>0:
            for i in fname:
                self.ar_name.append(i)

    def get_all_words(self):
        dic_fale ={}
        list2 = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']
        for af in self.ar_name:
            with open(af, encoding='utf-8') as file:
                text = file.read()
                text = text.lower()
                for y in list2:
                    text = text.replace(y, '')
                dic_fale[(af)] = text.split(' ')
        return dic_fale

    def find(self,word):
        dic_fin = {}
        dic_fale = self.get_all_words()
        for key, val in dic_fale.items():
            pos = val.index(word.lower())+1
            dic_fin[(key)] = pos
            return dic_fin

    def count(self, word):
        dic_fin = {}
        dic_fale = self.get_all_words()
        for key, val in dic_fale.items():
            pos = val.count(word.lower())
            dic_fin[(key)] = pos
            return dic_fin

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего