Name:           spice-protocol
Version:        0.12.6
Release:        1%{?dist}
Summary:        Spice protocol header files
Group:          Development/Libraries
# Main headers are BSD, controller / foreign menu are LGPL
License:        BSD and LGPLv2+
URL:            http://www.spice-space.org/
Source0:        http://www.spice-space.org/download/releases/%{name}-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  autoconf
BuildRequires:  automake

%description
Header files describing the spice protocol
and the para-virtual graphics card QXL.

%prep
%setup -q

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root,-)
%doc COPYING NEWS
%{_includedir}/spice-1
%{_datadir}/pkgconfig/spice-protocol.pc

%changelog
* Wed Jun 26 2013 Yonit Lublin <yhalperi@redhat.com> 0.12.6-1
- Rebase to upstream spice-protocol 0.12.6, which adds:
  0.12.6
  + Add adaptive video streaming support:
    control playback latency and receive playback
    reports from the client.
  + Add agent capabilities for signaling guest line ending.
  0.12.5
  + Add agent file xfer success status
  + Add a client-disconnected agent message
  0.12.4
  + Add agent file copy support.
  + Add agent sparse monitors capability.
  + Add controller proxy message.
  0.12.3
  +Add a generic "port" channel

* Thu Sep 20 2012 Uri Lublin <uril@redhat.com> 0.12.2-1
- Rebase to upstream spice-protocol 0.12.2, which adds:
  0.12.2:
  + Add A8 surface capability in display channel.
  + Add to qxl device support for:
    = client present
    = client capabilities
    = client monitors configuration
  0.12.1:
  + Support seamless migration.
  + New QXLComposite message for better X support.
  + Support arbitrary scancode message INPUTS_KEY_SCANCODE.
  0.12.0:
  + Add support for arbitrary resolution on Windows QXL with
    QXL_ESCAPE_SET_CUSTOM_DISPLAY
  + Add support for arbitrary resolution and multiple monitor per
    display channel with QXLMonitorsConfig and co
  + build cleanup
  Resolves: rhbz#842352
  Resolves: rhbz#846910
 

* Mon May 07 2012 Yonit Halperin <yhalperi@redhat.com> - 0.10.1-4
- Add autoreconf to spec in order to regenerate spice-protocol.pc
  Resolves: rhbz#815422

* Mon May 07 2012 Yonit Halperin <yhalperi@redhat.com> - 0.10.1-3
- Add support for video streams with frames of different sizes
  Resolves: rhbz#815422

* Thu Apr 05 2012 Christophe Fergeau <cfergeau@redhat.com> - 0.10.1-2
- Add controller message for smartcard support
  Related: rhbz#787447
- Add controller messages for WAN support
  Resolves: rhbz#787447
- Add controller messages for USB support
  Resolves: rhbz#807295

* Wed Jan 18 2012 Hans de Goede <hdegoede@redhat.com> - 0.10.1-1
- Update to upstream 0.10.1 release
  Resolves: rhbz#758088

* Tue Sep 27 2011 Uri Lublin <uril@redhat.com> - 0.8.1-2
- Support for spice client semi-seemless migration.
- Update to upstream spice-protocol 0.8.2 release without rebasing
- Added "BuildRequires: autoconf automake" for using autoreconf
  Resolves: rhbz#738262

* Fri Jul 22 2011 Uri Lublin <uril@redhat.com> - 0.8.1-1
- Update to upstream 0.8.1 release
  Resolves: rhbz#723480

* Wed Mar  2 2011 Hans de Goede <hdegoede@redhat.com> - 0.8.0-1
- Update to upstream 0.8.0 release
  Related: rhbz#662992

* Mon Feb 14 2011 Hans de Goede <hdegoede@redhat.com> - 0.7.1-1
- Update to upstream 0.7.1 release
  Related: rhbz#662992

* Wed Jan 12 2011 Hans de Goede <hdegoede@redhat.com> - 0.7.0-2
- Update License tag (controller and foreign menu headers are LGPL)
  Related: rhbz#662992

* Fri Dec 17 2010 Hans de Goede <hdegoede@redhat.com> - 0.7.0-1
- Update to upstream 0.7.0 release
  Related: rhbz#662992

* Thu Dec 16 2010 Hans de Goede <hdegoede@redhat.com> - 0.6.3-3
- Build for RHEL-6
  Resolves: rhbz#662992

* Wed Dec 15 2010 Hans de Goede <hdegoede@redhat.com> - 0.6.3-2
- Add utf8 controller menu text patch from upstream git
- Add smartcard channel patch from upstream git

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

