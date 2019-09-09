from yandex_translate import YandexTranslate # alinan translate.translate(g, 'en-tr')['text'][0]

translate = YandexTranslate('trnsl.1.1.20190620T080928Z.059272b876400ab5.db9848757da3b1698721fef656db05d4903c4d1b')


def tr_from_en_list(en_list):
    # return list tr
    
    alinan_texts = []
    
    for ji in range(len(en_list)):
        en_word = en_list[ji]
        alinan_dic = translate.translate(en_word, 'en-tr')
        alinan_text = alinan_dic['text'][0]
        alinan_texts.append(alinan_text)
        
        
    return     alinan_texts