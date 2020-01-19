Name:           spice-protocol
Version:        0.12.14
Release:        1%{?dist}
Summary:        Spice protocol header files
Group:          Development/Libraries
# Main headers are BSD, controller / foreign menu are LGPL
License:        BSD and LGPLv2+
URL:            https://www.spice-space.org/
Source0:        https://www.spice-space.org/download/releases/%{name}-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  automake autoconf git-core

%description
Header files describing the spice protocol
and the para-virtual graphics card QXL.


%prep
%autosetup -S git_am


%build
autoreconf -fi
%configure
make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install


%files
%doc COPYING NEWS
%{_includedir}/spice-1
%{_datadir}/pkgconfig/spice-protocol.pc


%changelog
* Fri Jun 08 2018 Victor Toso <victortoso@redhat.com> - 0.12.14-1
- Update to 0.12.14
  Related: rhbz#1562129

* Thu Oct 12 2017 Christophe Fergeau <cfergeau@redhat.com> - 0.12.13-2
- Add streaming patches for use in combination with spice-streaming-agent
  Related: rhbz#1471000

* Thu Jul 20 2017 Uri Lublin <uril@redhat.com> - 0.12.13-1
- Update to 0.12.13
- Related: rhbz#1471000

* Mon Mar 13 2017 Pavel Grunt <pgrunt@redhat.com> - 0.12.12-2
- Rebuilt with correct hardening flags due to bug 1387475
- Resolves: rhbz#1420779

* Fri Dec 16 2016 Pavel Grunt <pgrunt@redhat.com> - 0.12.12-1
- Update to 0.12.12
- Resolves: rhbz#1402729

* Fri Apr 29 2016 Victor Toso <victortoso@redhat.com> - 0.12.11-1
- Update to 0.12.11
- Resolves: rhbz#1322363

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.12.6-2
- Mass rebuild 2013-12-27

* Wed Jul  3 2013 Hans de Goede <hdegoede@redhat.com> - 0.12.6-1
- Update to 0.12.6

* Thu Mar  7 2013 Hans de Goede <hdegoede@redhat.com> - 0.12.5-1
- Update to 0.12.5

* Fri Feb  1 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.12.4-1
- Update to 0.12.4

* Thu Dec 20 2012 Hans de Goede <hdegoede@redhat.com> - 0.12.3-1
- Update to 0.12.3

* Fri Sep 28 2012 Hans de Goede <hdegoede@redhat.com> - 0.12.2-1
- Update to 0.12.2

* Thu Sep 6 2012 Soren Sandmann <ssp@redhat.com> - 0.12.1-1
- Add patch1 and patch2 to support capability bits

* Thu Sep 6 2012 Soren Sandmann <ssp@redhat.com> - 0.12.1-1
- Update to 0.12.1

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 16 2012 Hans de Goede <hdegoede@redhat.com> - 0.10.1-1
- Update to 0.10.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 13 2011 Alon Levy <alevy@redhat.com> - 0.10.0-1
- Update to 0.10.0

* Sun Oct 23 2011 Alon Levy <alevy@redhat.com> - 0.9.1-1
- Update to 0.9.1

* Thu Aug 25 2011 Hans de Goede <hdegoede@redhat.com> - 0.9.0-1
- Update to 0.9.0

* Mon Jul 25 2011 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.8.1-2
- Added spice-protocol-0.8.1-define-INLINE.patch

* Tue Jul 19 2011 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.8.1-1
- Update to 0.8.1

* Tue Mar  1 2011 Hans de Goede <hdegoede@redhat.com> - 0.8.0-1
- Update to 0.8.0

* Fri Feb 11 2011 Hans de Goede <hdegoede@redhat.com> - 0.7.1-1
- Update to 0.7.1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 12 2011 Hans de Goede <hdegoede@redhat.com> - 0.7.0-2
- Update License tag (controller and foreign menu headers are LGPL)

* Fri Dec 17 2010 Hans de Goede <hdegoede@redhat.com> - 0.7.0-1
- Update to 0.7.0

* Mon Oct 18 2010 Hans de Goede <hdegoede@redhat.com> - 0.6.3-1
- Update to 0.6.3

* Thu Sep 30 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.6.1-1
- Update to 0.6.1.

* Tue Aug 31 2010 Alexander Larsson <alexl@redhat.com> - 0.6.0-1
- Update to 0.6.0 (stable release)

* Tue Jul 20 2010 Alexander Larsson <alexl@redhat.com> - 0.5.3-1
- Update to 0.5.3

* Mon Jul 12 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.5.2-2
- Fix license: It is BSD, not GPL.
- Cleanup specfile, drop bits not needed any more with
  recent rpm versions (F13+).

* Fri Jul 9 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.5.2-1
- initial package.

