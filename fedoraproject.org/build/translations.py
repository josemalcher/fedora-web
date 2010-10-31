#!/usr/bin/python
#coding=UTF-8
import sys

# See https://translate.fedoraproject.org/languages/
# for a list of languages
language_name_map = {
'af': 'Afrikaans (af)',
'ar': 'عربي',
'as': 'Assamese (as)',
'ast': 'Asturianu',
'bal': 'Balochi (bal)',
'bg': 'Bulgarian (bg)',
'bn_IN': 'বাংলা (ভারত)',
'ca': 'Catalan (ca)',
'cs': 'Česky',
'da': 'dansk',
'de': 'Deutsch',
'de_CH': 'Swiss German (de_CH)',
'el': 'Ελληνικά',
'en': 'English',
'es': 'Español',
'fa': 'پارسی',
'fi': 'suomi',
'fr': 'Français',
'gu': 'ગુજરાતી',
'he': 'עברית',
'hi': 'हिन्दी',
'hu': 'magyar',
'id': 'Indonesia',
'is': 'Íslenska',
'it': 'Italiano',
'ja': '日本語',
'kn': 'ಕನ್ನಡ',
'ko': '한국어',
'ml': 'മലയാളം',
'mr': 'Marathi (mr)',
'nl': 'Nederlands',
'or': 'ଓଡ଼ିଆ',
'pa': 'Panjabi (pa)',
'pl': 'polski',
'pt': 'Português',
'pt_BR': 'Brazilian (pt_BR)',
'ro': 'Romanian (ro)',
'ru': 'Русский',
'sk': 'Slovak (sk)',
'sq': 'Shqip',
'sr': 'српски',
'sv': 'Swedish (sv)',
'ta': 'Tamil (ta)',
'te': 'Telugu (te)',
'tg': 'Tajik (tg)',
'th': 'Thai (th)',
'uk': 'українська',
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
