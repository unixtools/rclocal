VERSION=2.1.1

all:

install:
	mkdir -p $(DESTDIR)/etc/init.d
	cp files/rclocal $(DESTDIR)/etc/init.d/rclocal

dist:
	rm -rf /tmp/rclocal-$(VERSION)
	mkdir /tmp/rclocal-$(VERSION)
	cp -pr . /tmp/rclocal-$(VERSION)
	cd /tmp/rclocal-$(VERSION) && rm -rf *.gz .git .gitignore
	tar -C/tmp -czvf ../rclocal-$(VERSION).tar.gz rclocal-$(VERSION)
	rm -rf /tmp/rclocal-$(VERSION)

deb: dist
	cp ../rclocal-$(VERSION).tar.gz ../rclocal_$(VERSION).orig.tar.gz
	dpkg-buildpackage
	rm ../rclocal_$(VERSION).orig.tar.gz