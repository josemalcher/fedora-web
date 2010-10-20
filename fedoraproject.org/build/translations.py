#!/usr/bin/python
import sys

# See https://translate.fedoraproject.org/languages/
# for a list of languages
language_name_map = {
'af': 'Afrikaans (af)',
'ar': 'Arabic (ar)',
'as': 'Assamese (as)',
'ast': 'Asturian (ast)',
'bal': 'Balochi (bal)',
'bg': 'Bulgarian (bg)',
'bn_IN': 'Bengali (bn_IN)',
'ca': 'Catalan (ca)',
'cs': 'Czech (cs)',
'da': 'Danish (da)',
'de': 'German (de)',
'de_CH': 'Swiss German (de_CH)',
'el': 'Greek (el)',
'en': 'English (en)',
'es': 'Spanish (es)',
'fa': 'Persian (fa)',
'fi': 'Finnish (fi)',
'fr': 'French (fr)',
'gu': 'Gujarati (gu)',
'he': 'Hebrew (he)',
'hi': 'Hindi (hi)',
'hu': 'Hungarian (hu)',
'id': 'Indonesian (id)',
'is': 'Icelandic (is)',
'it': 'Italian (it)',
'ja': 'Japanese (ja)',
'kn': 'Kannada (kn)',
'ko': 'Korean (ko)',
'ml': 'Malayalam (ml)',
'mr': 'Marathi (mr)',
'nl': 'Dutch (nl)',
'or': 'Oriya (or)',
'pa': 'Panjabi (pa)',
'pl': 'Polish (pl)',
'pt': 'Portuguese (pt)',
'pt_BR': 'Brazilian (pt_BR)',
'ro': 'Romanian (ro)',
'ru': 'Russian (ru)',
'sk': 'Slovak (sk)',
'sq': 'Albanian (sq)',
'sr': 'Serbian (sr)',
'sv': 'Swedish (sv)',
'ta': 'Tamil (ta)',
'te': 'Telugu (te)',
'tg': 'Tajik (tg)',
'th': 'Thai (th)',
'uk': 'Ukrainian (uk)',
'zh_CN': 'Chinese (China) (zh_CN)',
'zh_TW': 'Chinese (Taiwan) (zh_TW)',
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
