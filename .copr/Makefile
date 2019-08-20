srpm:
	dnf -y install rpmdevtools rpm-build
	spectool -g -R $(spec)
	rpmbuild -bs $(spec)
