include ../Makefile.in

$(LANGUAGES): % : | po/%.mo data/templates/translations.html
	$(PYTHON) build/hosted.py -o out -i data/content -l $@ -p po -s static -b $(BASEPATH) -d data/projects.csv -t /srv/web/trac/projects -c svn -c git -c mtn -c hg -c bzr

