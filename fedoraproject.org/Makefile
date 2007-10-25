LANGUAGES = $(shell grep -v "^\#" po/LINGUAS)
PO_FILES = $(patsubst %, po/%.po, $(LANGUAGES))
MO_FILES = $(patsubst %, po/%.mo, $(LANGUAGES))

PYTHON = python
PYBABEL = pybabel
BASEPATH = /

all: data/templates/translations.html po/fedora-web.pot $(MO_FILES) $(LANGUAGES)

$(LANGUAGES): data/templates/translations.html
	$(PYTHON) build/build.py -o out -i data/content -l $@ -p po -s images,css,js -b $(BASEPATH)

po/en.po: po/fedora-web.pot
	cp po/fedora-web.pot po/en.po

# FIXME: This apparently doesn't run when the po files already exist.
%.po: po/fedora-web.pot
	msgmerge --no-wrap --update $@ $^

%.mo: %.po
	msgfmt -o $@ $<

# FIXME: This apparently doesn't run when the POT file already exists.
po/fedora-web.pot:
	${PYBABEL} extract -F build/pybabel.cfg data -o $@

data/templates/translations.html: po/LINGUAS
	$(PYTHON) build/translations.py $^ > $@

clean:
	rm -rf out
	rm -f po/en.po
	rm -f po/*.mo
	rm -f data/templates/translations.html

.PHONY: all clean
