ifndef LANGUAGES
LANGUAGES := $(shell grep -v "^\#" po/LINGUAS)
endif
GENERIC_HEADER = msgid ""\
                 msgstr ""\
                 "Project-Id-Version: PROJECT VERSION\n"\
                 "MIME-Version: 1.0\n"\
                 "Content-Type: text/plain; charset=utf-8\n"\
                 "Content-Transfer-Encoding: 8bit"
PO_FILES = $(wildcard po/*.po)
MO_FILES = $(PO_FILES:.po=.mo)
HTML_FILES = $(shell find data -name "*.html")

PYTHON = python
PYBABEL = pybabel
BASEPATH = /
PWD = $(shell pwd)

all: $(LANGUAGES)
	cp static/robots.txt out/

static: 
	mkdir -p out/static/js
	wget http://code.jquery.com/jquery-latest.js -O out/static/js/jquery.js -q

$(LANGUAGES): % : | static po/%.mo data/templates/translations.html
	$(PYTHON) build/build.py -o out -i data/content -l $@ -p po -s static -b $(BASEPATH) -d data/projects.csv -t /srv/web/trac/projects -c svn -c git -c mtn -c hg -c bzr

po/%.mo: po/%.po
	msgfmt -o $@ $<

po/fedorahosted.pot: $(HTML_FILES)
	${PYBABEL} extract -F build/pybabel.cfg data -o $@

pot: $(HTML_FILES)
	${PYBABEL} extract -F build/pybabel.cfg data -o po/fedorahosted.pot

pushpot:
	tx push -s

pullpos:
	tx pull -af
	tx pull --lang=en

data/templates/translations.html: po/LINGUAS
	$(PYTHON) build/translations.py $^ > $@

clean:
	rm -rf out
	rm -f po/*.mo
	rm -f data/templates/translations.html
	rm -f build/rss.cache

msgmerge: $(wildcard po/*.po)

push:
	git push

httpd/conf/httpd.conf: httpd/conf/httpd.conf.in
	cp httpd/conf/httpd.conf.in httpd/conf/httpd.conf
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

test: httpd/conf/httpd.conf httpd/conf/languages.conf
	/usr/sbin/httpd -d httpd -f conf/httpd.conf
	@echo "Test instance started at: http://localhost:5000/"

stoptest:
	pid=`cat httpd/run/httpd.pid` && \
	kill -TERM $$pid

.PHONY: all clean push test stoptest
