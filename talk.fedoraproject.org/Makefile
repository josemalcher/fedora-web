LANGUAGES = $(shell grep -v "^\#" po/LINGUAS)
PO_FILES = $(patsubst %, po/%.po, $(LANGUAGES))
MO_FILES = $(patsubst %, po/%.mo, $(LANGUAGES))
HTML_FILES = $(shell find . -name "*.html")

PYTHON = python
PYBABEL = pybabel
BASEPATH = /

all: po/talk.fedoraproject.pot $(MO_FILES) $(LANGUAGES)

$(LANGUAGES): data/templates/translations.html
	$(PYTHON) build/build.py -o out -i data/content -l $@ -p po -s static -b $(BASEPATH) -d data/projects.csv -t /srv/web/talk

po/en.po: po/talk.fedoraproject.pot
	cp po/talk.fedoraproject.pot po/en.po

%.po: po/talk.fedoraproject.pot
	msgmerge --no-wrap --update $@ $^

%.mo: %.po
	msgfmt -o $@ $<

po/talk.fedoraproject.pot: $(HTML_FILES)
	${PYBABEL} extract -F build/pybabel.cfg data -o $@

data/templates/translations.html: po/LINGUAS
	$(PYTHON) build/translations.py $^ > $@

clean:
	rm -rf out
	rm -f po/en.po
	rm -f po/*.mo
	rm -f data/templates/translations.html

.PHONY: all clean
