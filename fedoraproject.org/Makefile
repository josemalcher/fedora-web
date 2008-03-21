LANGUAGES = $(shell grep -v "^\#" po/LINGUAS)
PO_FILES = $(patsubst %, po/%.po, $(LANGUAGES))
MO_FILES = $(patsubst %, po/%.mo, $(LANGUAGES))
HTML_FILES = $(shell find . -name "*.html")

PYTHON = python
PYBABEL = pybabel
BASEPATH = /
PWD = $(shell pwd)

all: po/fedora-web.pot $(MO_FILES) $(LANGUAGES)
	cp static/robots.txt	out/

$(LANGUAGES): data/templates/translations.html
	$(PYTHON) build/build.py -o out -i data/content -l $@ -p po -s static -b $(BASEPATH)

po/en.po: po/fedora-web.pot
	cp po/fedora-web.pot po/en.po

%.po: po/fedora-web.pot
	msgmerge --no-wrap --update $@ $^

%.mo: %.po
	msgfmt -o $@ $<

po/fedora-web.pot: $(HTML_FILES)
	${PYBABEL} extract -F build/pybabel.cfg data -o $@

data/templates/translations.html: po/LINGUAS
	$(PYTHON) build/translations.py $^ > $@

clean:
	rm -rf out
	rm -f po/en.po
	rm -f po/*.mo
	rm -f data/templates/translations.html

push:
	git rebase master live
	git checkout master
	git push

test:
	cp httpd/conf/httpd.conf.in httpd/conf/httpd.conf
	sed -i -e 's#@SERVERROOT@#$(PWD)/httpd#g' httpd/conf/httpd.conf
	sed -i -e 's#@DOCUMENTROOT@#$(PWD)/out#g' httpd/conf/httpd.conf
	/usr/sbin/httpd -d httpd -f conf/httpd.conf

stoptest:
	pid=`cat httpd/run/httpd.pid` && \
	kill -TERM $$pid

.PHONY: all clean push test stoptest
