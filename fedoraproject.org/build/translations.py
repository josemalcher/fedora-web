#!/usr/bin/python
#coding=UTF-8
import sys

# See http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
# for a list of languages
language_name_map = {
'af': 'Afrikaans',
'ar': 'عربي',
'as': 'অসমীয়া',
'ast': 'Asturianu',
'bal': 'بلوچی',
'bg': 'български език',
'bn': 'বাংলা',
'bn_IN': 'বাংলা (ভারত)',
'br': 'Brezhoneg',
'ca': 'Català',
'cs': 'česky',
'da': 'dansk',
'de': 'Deutsch',
'de_CH': 'Schwyzerdütsch',
'el': 'Ελληνικά',
'en': 'English',
'es': 'Español',
'et': 'eesti',
'eu': 'euskera',
'fa': 'پارسی',
'fi': 'suomi',
'fr': 'Français',
'gl': 'galego',
'gu': 'ગુજરાતી',
'he': 'עברית',
'hi': 'हिन्दी',
'hu': 'Magyar',
'id': 'Indonesia',
'is': 'Íslenska',
'it': 'Italiano',
'ja': '日本語',
'ka': 'ქართული',
'kk': 'қазақ тілі',
'kn': 'ಕನ್ನಡ',
'ko': '한국어',
'ks': 'कश्मीरी',
'lv': 'latviešu',
'ml': 'മലയാളം',
'mr': 'मराठी',
'nb': 'Norsk bokmål',
'nl': 'Nederlands',
'or': 'ଓଡ଼ିଆ',
'pa': 'ਪੰਜਾਬੀ',
'pl': 'polski',
'pt': 'Português',
'pt_BR': 'Português brasileiro',
'ro': 'română',
'ru': 'Pусский',
'si': 'සිංහල',
'sk': 'slovenčina',
'sq': 'Shqip',
'sr': 'српски',
'sv': 'svenska',
'ta': 'தமிழ்',
'te': 'తెలుగు',
'tg': 'тоҷикӣ',
'th': 'ไทย',
'tr': 'Tϋrkçe',
'uk': 'українська',
'ur': 'اردو',
'vi': 'Tiếng Việt',
'zh_CN': '简体中文',
'zh_TW': '正體中文',
}

linguasfile = sys.argv[1]
f = open(linguasfile)
print '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
  xmlns:py="http://genshi.edgewall.org/"
  xmlns:xi="http://www.w3.org/2001/XInclude"
  py:strip="">
  '''
try:
    for lang in f:
        lang = lang.strip()
        if lang and not lang.startswith('#'):
            print '    <option value="' + lang + '" py:attrs="{\'selected\': lang == \'' + lang + '\' and \'selected\' or None}">' + language_name_map.get(lang, lang) + '</option>'
finally:
    f.close()
print '''</html>
'''
