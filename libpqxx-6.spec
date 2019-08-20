
Name:           libpqxx
Summary:        C++ client API for PostgreSQL
Epoch:          1
Version:        6.4.5
Release:        1%{?dist}


License:        BSD
URL:            http://pqxx.org/
Source0:        https://github.com/jtv/libpqxx/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  libpq-devel
BuildRequires:  postgresql-server-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  xmlto
BuildRequires:  postgresql-test-rpm-macros

%define cmake_builddir cmake_build

%description
C++ client API for PostgreSQL. The standard front-end (in the sense of
"language binding") for writing C++ programs that use PostgreSQL.
Supersedes older libpq++ interface.

%package devel
Summary:        Development tools for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libpq-devel
%description devel
%{summary}.

%package doc
Summary: Developer documentation for %{name}
BuildArch: noarch
%description doc
%{summary}.


%prep
%autosetup

# fix spurious permissions
chmod -x COPYING


%build
mkdir %cmake_builddir
pushd %cmake_builddir
%cmake ..
%make_build
popd

%configure
pushd doc
%make_build
popd


%install
pushd %cmake_builddir
%make_install
popd

mkdir -p %{buildroot}%{_libdir}/pkgconfig
cp -f libpqxx.pc %{buildroot}%{_libdir}/pkgconfig/libpqxx.pc


%check
%postgresql_tests_run
pushd test
ctest -V %{?_smp_mflags}
popd

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README.md VERSION
%license COPYING
%{_libdir}/libpqxx.so
%{_docdir}/%{name}/accessing-results.md
%{_docdir}/%{name}/escaping.md
%{_docdir}/%{name}/getting-started.md
%{_docdir}/%{name}/mainpage.md
%{_docdir}/%{name}/performance.md
%{_docdir}/%{name}/prepared-statement.md
%{_docdir}/%{name}/streams.md
%{_docdir}/%{name}/thread-safety.md

%files devel
%doc README-UPGRADE
%{_includedir}/pqxx/
%{_libdir}/libpqxx.a
%{_libdir}/pkgconfig/libpqxx.pc
%{_libdir}/cmake/libpqxx/libpqxx-config.cmake
%{_libdir}/cmake/libpqxx/libpqxx-config-version.cmake
%{_libdir}/cmake/libpqxx/libpqxx-targets.cmake
%{_libdir}/cmake/libpqxx/libpqxx-targets-noconfig.cmake

%files doc
%doc doc/html/*


%changelog
* Tue Aug 20 2019 Aleksei Aleshin <alalexey@gmail.com> - 1:6.4.5-1
- Bumb version to 6.4.5 and switch to cmake build

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 27 2018 Pavel Raiskup <praiskup@redhat.com> - 4.0.1-16
- don't ignore testsuite failures, run it against live PostgreSQL server

* Fri Jul 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:4.0.1-15
- fix calls to /usr/bin/python (#1604643)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1:4.0.1-13
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Mar 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:4.0.1-12
- BR: gcc-c++, use %%license %%make_build %%make_install

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 24 2017 Dave Johansen <davejohansen@gmail.com> - 1:4.0.1-8
- Fix linker issue during configure

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 19 2015 Rex Dieter <rdieter@fedoraproject.org> 4.0.1-4
- rebuild (gcc5)

* Thu Feb 26 2015 Rex Dieter <rdieter@fedoraproject.org> 1:4.0.1-3
- rebuild (gcc5)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 24 2014 Rex Dieter <rdieter@fedoraproject.org> 1:4.0.1-1
- 4.0.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Sep 20 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:3.2-0.6
- .spec cleanup
- -doc subpkg
- (re)enable %%check

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 01 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1:3.2-0.1
- version upgrade
- upstream fixes for gcc4.6
- fix ftbfs (rhbz#716147)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 29 2009 Rex Dieter <rdieter@fedoraproject.org> - 1:3.0.2-4
- Epoch: 1
- libpqxx-3.0.2

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 09 2009 Rex Dieter <rdieter@fedoraproject.org> 3.0.0-1
- libpqxx-3.0

* Tue Mar 03 2009 Robert Scheck <robert@fedoraproject.org> - 2.6.8-12
- Rebuilt against libtool 2.2

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Rex Dieter <rdieter@fedoraproject.org> 2.6.8-10
- gcc43 patch
- fix multilib conflicts (#342331)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.6.8-9
- Autorebuild for GCC 4.3

* Sun Dec 09 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 2.6.8-8
- cosmetics

* Fri Aug 17 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 2.6.8-7
- update Source URL's

* Mon Jun 04 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 2.6.8-6
- 2.6.9 pulled, revert to 2.6.8 (for koffice)

* Tue May 22 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 2.6.9-1
- libpqxx-2.6.9

* Wed Dec 06 2006 Rex Dieter <rexdieter[AT]users.sf.net> 2.6.8-5
- re-enable visibility patch (bummer, still needed)

* Wed Dec 06 2006 Rex Dieter <rexdieter[AT]users.sf.net> 2.6.8-4
- respin for postgresql
- drop visibility patch

* Wed Oct 04 2006 Rex Dieter <rexdieter[AT]users.sf.net> 2.6.8-3
- respin

* Wed Sep 20 2006 Rex Dieter <rexdieter[AT]users.sf.net> 2.6.8-1
- fc6+: drop -Werror (for now)
- include %%check section (not used, by default)

* Fri Sep 15 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> 2.6.7-2
- version upgrade

* Thu Aug 03 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> 2.6.7-1
- version upgrade
- fix #192933

* Mon May 29 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> 2.6.6-1
- version upgrade

* Thu Feb 16 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> 2.5.5-7
- Rebuild for Fedora Extras 5

* Wed Sep 28 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> 2.5.5-6
- fix #169441

* Tue Sep 27 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> 2.5.5-5
- try fc5 build

* Tue Sep 27 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> 2.5.5-4
- version upgrade

* Tue Jul 05 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> 2.5.4-4
- add dist tag

* Fri Jul 01 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> 2.5.4-3
- add postgresql-devel to Requires for devel package
- get rid of -R option in pqxx-config
- don't need BuildRequires perl

* Thu Jun 30 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> 2.5.4-2
- Drop explicit Requires for ldconfig

* Sat Jun 25 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> 2.5.4-1
- Initial Release
