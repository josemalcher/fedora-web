include ../Makefile.in

$(LANGUAGES): % : | staticSnd rss-cache po/%.mo data/templates/translations.html
	$(PYTHON) $(BUILDDIR)/build.py -o out -i data/content -l $@ -p po -b $(BASEPATH)

