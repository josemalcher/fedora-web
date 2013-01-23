include ../Makefile.in

$(LANGUAGES): % : | static rss-cache po/%.mo data/templates/translations.html
	$(PYTHON) build/build.py -o out -i data/content -l $@ -p po -b $(BASEPATH)

