LANGUAGES = en
MO_FILES = $(patsubst %, %.mo, $(filter-out en ,$(LANGUAGES)))

PYTHON = python
PYBABEL = pybabel
BASEPATH = /

all: po $(MO_FILES) $(LANGUAGES)

$(LANGUAGES):
	$(PYTHON) build/build.py -o out -i data/content -l $@ -p po -s images,css -b $(BASEPATH) -e

%.po: po/fedora-web.pot
	msgmerge --no-wrap --update $@ $^

%.mo: %.po
	msgfmt -o $@ $<

po/fedora-web.pot:
	${PYBABEL} extract -F build/pybabel.cfg data -o po/fedora-web.pot

clean:
	rm -rf out

.PHONY: site all po clean
