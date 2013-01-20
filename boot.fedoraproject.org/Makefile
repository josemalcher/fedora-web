ifndef LANGUAGES
LANGUAGES := $(shell grep -v "^\#" po/LINGUAS)
endif
HTML_FILES = $(shell find data -name "*.html")
# Check if the Fedora release is at least Fedora 18 (httpd-2.4.3 or later)
NEW_HTTPD = $(shell expr `cat /etc/redhat-release  |awk '{print $$3}'` \>= 18)

PYTHON = python
PYBABEL = $(PYTHON) /usr/bin/pybabel
BASEPATH = /
PWD = $(shell pwd)

all: $(LANGUAGES)
	cp static/robots.txt out/
rss-cache:
	@echo Caching RSS...
	$(PYTHON) build/build.py -o out -i data/content -r -b $(BASEPATH)

static:
	@echo Copying static...
	$(PYTHON) build/build.py -o out -s static -b $(BASEPATH)

$(LANGUAGES): % : | static rss-cache po/%.mo data/templates/translations.html
	$(PYTHON) build/build.py -o out -i data/content -l $@ -p po -b $(BASEPATH)

po/%.mo: po/%.po
	msgfmt -o $@ $<

po/fedora-web.pot: $(HTML_FILES)
	${PYBABEL} extract -F build/pybabel.cfg data -o $@

data/templates/translations.html: po/LINGUAS
	$(PYTHON) build/translations.py $^ > $@

clean:
	rm -rf out
	rm -f po/*.mo
	rm -f data/templates/translations.html
	rm -f build/rss.cache build/rss.pyc
	rm -f httpd/conf/*.conf httpd/conf/languages.conf.in

msgmerge: $(wildcard po/*.po)

pot: $(HTML_FILES)
	${PYBABEL} extract -F build/pybabel.cfg data -o po/fedora-web.pot

pushpot:
	tx push -s

pullpos:
#	tx pull -af
#	tx pull --lang=en

push:
	git push

httpd/conf/httpd.conf: httpd/conf/httpd.conf.in
ifeq ($(NEW_HTTPD),1)
	cp httpd/conf/httpd.conf.in httpd/conf/httpd.conf
else
	@echo "Using the old httpd config file"
	cp httpd/conf/httpd.conf.old.in httpd/conf/httpd.conf
endif
	sed -i \
		-e 's#@SERVERROOT@#$(PWD)/httpd#g' \
		-e 's#@DOCUMENTROOT@#$(PWD)/out#g' \
		httpd/conf/httpd.conf


httpd/conf/languages.conf.in: po/LINGUAS
	$(PYTHON) build/buildconf.py $^ > $@

httpd/conf/languages.conf: httpd/conf/languages.conf.in
	cp httpd/conf/languages.conf.in httpd/conf/languages.conf
	sed -i \
		-e 's#@SERVERROOT@#$(PWD)/httpd#g' \
		-e 's#@DOCUMENTROOT@#$(PWD)/out#g' \
		httpd/conf/languages.conf

test: 	httpd/conf/httpd.conf httpd/conf/languages.conf
	/usr/sbin/httpd -d httpd -f conf/httpd.conf
	@echo "Test instance started at: http://localhost:5000/"

stoptest:
	pid=`cat httpd/run/httpd.pid` && \
	kill -TERM $$pid

.PHONY: all static rss-cache clean push test stoptest
