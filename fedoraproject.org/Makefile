ifndef LANGUAGES
LANGUAGES := $(shell grep -v "^\#" po/LINGUAS)
endif
PO_FILES = $(filter-out po/en.po,$(wildcard po/*.po))
MO_FILES = $(PO_FILES:.po=.mo)
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

$(PO_FILES): po/fedora-web.pot
	msgmerge --no-wrap --update $@ $^

$(MO_FILES) po/en.mo: $(PO_FILES) po/en.po
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
	rm -f build/rss.cache

push:
	git push

test:
	cp httpd/conf/httpd.conf.in httpd/conf/httpd.conf
	sed -i -e 's#@SERVERROOT@#$(PWD)/httpd#g' httpd/conf/httpd.conf
	sed -i -e 's#@DOCUMENTROOT@#$(PWD)/out#g' httpd/conf/httpd.conf
	/usr/sbin/httpd -d httpd -f conf/httpd.conf
	@echo "Test instance started at: http://localhost:5000/"

stoptest:
	pid=`cat httpd/run/httpd.pid` && \
	kill -TERM $$pid

.PHONY: all clean push test stoptest
