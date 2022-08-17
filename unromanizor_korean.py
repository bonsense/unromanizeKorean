from hangul_utils import join_jamos
import json

vowel = {
    'yae': 'ㅒ',
    'wae': 'ㅙ',
    'ae': 'ㅐ',
    'oe': 'ㅚ',
    'wi': 'ㅟ',
    'ya': 'ㅑ',
    'yŏ': 'ㅕ',
    'yo': 'ㅛ',
    'yu': 'ㅠ',
    'yŭ': 'ㅠ',
    'ye': 'ㅖ',
    'wa': 'ㅘ',
    'wŏ': 'ㅝ',
    'wǒ': 'ㅝ',
    'we': 'ㅞ',
    'ŭi': 'ㅢ',
    'a': 'ㅏ',
    'e': 'ㅔ',
    'ŏ': 'ㅓ',
    'o': 'ㅗ',
    'u': 'ㅜ',
    'ŭ': 'ㅡ',
    'i': 'ㅣ',
}
vowel2 = {
    'ㅏ': '',
    'ㅑ': '야',
    'ㅓ': '어',
    'ㅕ': '여',
    'ㅗ': '오',
    'ㅛ': '요',
    'ㅜ': '우',
    'ㅠ': '유',
    'ㅡ': '으',
    'ㅢ': '의',
    'ㅣ': '이',
    'ㅐ': '애',
    'ㅒ': '얘',
    'ㅔ': '에',
    'ㅖ': '예',
    'ㅙ': '왜',
    'ㅞ': '웨',
    'ㅚ': '외',
    'ㅟ': '위',
    'ㅘ': '와',
    'ㅝ': '워'
}
onset = {
    'n\'g': "ㄴㄱ",
    'nʻg': "ㄴㄱ",
    'ng': 'ㅇ',
    'kʻ': 'ㅋ',
    'kʼ': 'ㅋ',
    'k\'': 'ㅋ',
    'tʻ': 'ㅌ',
    'tʼ': 'ㅌ',
    't\'': 'ㅌ',
    'pʻ': 'ㅍ',
    'pʼ': 'ㅍ',
    'p\'': 'ㅍ',
    'chʻ': 'ㅊ',
    'ch\'': 'ㅊ',
    'chʼ': 'ㅊ',
    'kk': 'ㄲ',
    'tt': 'ㄸ',
    'pp': 'ㅃ',
    'ss': 'ㅆ',
    'tch': 'ㅉ',
    'ch': 'ㅈ',
    'j': 'ㅈ',
    'k': 'ㄱ',
    'g': 'ㄱ',
    't': 'ㄷ',
    'd': 'ㄷ',
    'p': 'ㅂ',
    'b': 'ㅂ',
    's': 'ㅅ',
    'h': 'ㅎ',
    'n': 'ㄴ',
    'm': 'ㅁ',
    'r': 'ㄹ',
    'l': 'ㄹ'   #need another rule for deromanization
}
key_of_vowel = list(vowel.keys())
value_of_vowel = list(set(vowel.values()))
key_onset = list(onset.keys())

def translator (trob):
#.....<trob> means translation object
#trimming...
    trob = trob.lower().replace('ǒ', 'ŏ').replace('ǔ', 'ŭ').replace('ō', 'ŏ').replace("author", '').replace('ʻ', '\'').replace('ʼ', '\'')
#translating...
    if trob.find("shwi") != -1:
        trob = trob.replace("shwi", 'ㅅㅟ')
    for i in key_of_vowel:
        result = trob.find(i)
        if result != -1:
            trob = trob.replace(i, vowel[i])
    for i in key_onset:
        result = trob.find(i)
        if result != -1:
            trob = trob.replace(i, onset[i])
    locationOfEung = trob.find('ㅇ')
    if locationOfEung != -1:
        try:
            if value_of_vowel.count(trob[locationOfEung+1]) == 1:
             trob = trob[:locationOfEung] + "ㅇ" + trob[locationOfEung:]
        except:
            pass
    trob = join_jamos(trob)
    for i in value_of_vowel:
        if trob.find(i) != -1:
            trob = trob.replace(i, "ㅇ" + i)
    trob = join_jamos(trob)
    trob = trob.replace("y이", "이").replace("우이", '의')
    return trob

with open("/Users/minkijung/Desktop/tplkoreanbook/server/tpl_python/data_webcrawling/new_data/tpl_data.json", "r") as j:
    books = json.loads(j.read())
    books = books["books"]

for book in books:
    book_id = book['id']
    book_title = book['tpl_title']
    book_author = book['tpl_author']

    translated_title = translator(book_title)
    books[book_id]['translated_title'] = translated_title

    translated_author = translator(book_author)
    books[book_id]['translated_author'] = translated_author

data = {"books": books}
with open("/Users/minkijung/Desktop/tplkoreanbook/server/tpl_python/data_webcrawling/new_data/translated_data.json", "w") as j:
    json.dump(data, j, indent=3, ensure_ascii=False)