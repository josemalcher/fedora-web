LANGUAGES = en
PO_FILES = $(patsubst %, po/%.po, $(LANGUAGES))
MO_FILES = $(patsubst %, po/%.mo, $(LANGUAGES))

PYTHON = python
PYBABEL = pybabel
BASEPATH = /

all: po/fedora-web.pot $(MO_FILES) $(LANGUAGES)

$(LANGUAGES):
	$(PYTHON) build/build.py -o out -i data/content -l $@ -p po -s images,css -b $(BASEPATH)

po/en.po: po/fedora-web.pot
	cp po/fedora-web.pot po/en.po

# FIXME: This apparently doesn't run when the po files already exist.
%.po: po/fedora-web.pot
	msgmerge --no-wrap --update $@ $^

%.mo: %.po
	msgfmt -o $@ $<

po/fedora-web.pot:
	${PYBABEL} extract -F build/pybabel.cfg data -o po/fedora-web.pot

clean:
	rm -rf out
	rm po/en.po
	rm po/*.mo

.PHONY: all clean
