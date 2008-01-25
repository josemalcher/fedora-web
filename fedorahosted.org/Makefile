LANGUAGES = $(shell grep -v "^\#" po/LINGUAS)
PO_FILES = $(patsubst %, po/%.po, $(LANGUAGES))
MO_FILES = $(patsubst %, po/%.mo, $(LANGUAGES))
HTML_FILES = $(shell find . -name "*.html")

PYTHON = python
PYBABEL = pybabel
BASEPATH = /

all: po/fedorahosted.pot $(MO_FILES) $(LANGUAGES)

$(LANGUAGES): data/templates/translations.html
	$(PYTHON) build/build.py -o out -i data/content -l $@ -p po -s static -b $(BASEPATH) -d data/projects.csv -t /srv/web/trac/projects

po/en.po: po/fedorahosted.pot
	cp po/fedorahosted.pot po/en.po

%.po: po/fedorahosted.pot
	msgmerge --no-wrap --update $@ $^

%.mo: %.po
	msgfmt -o $@ $<

po/fedorahosted.pot: $(HTML_FILES)
	${PYBABEL} extract -F build/pybabel.cfg data -o $@

data/templates/translations.html: po/LINGUAS
	$(PYTHON) build/translations.py $^ > $@

clean:
	rm -rf out
	rm -f po/en.po
	rm -f po/*.mo
	rm -f data/templates/translations.html

.PHONY: all clean
