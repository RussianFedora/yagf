Summary:    Yet Another Graphic Front-end for Cuneiform
Name:       yagf
Version:    0.9
Release:    1%{?dist}

License:    GPLv3
Group:      Applications/Multimedia
Summary:    Graphical frontend for Cuneiform OCR tool
URL:        http://symmetrica.net/cuneiform-linux/yagf-en.html

Source:     http://symmetrica.net/cuneiform-linux/%{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  qt-devel >= 4.6
BuildRequires:  aspell-devel
BuildRequires:  cmake

Requires:       xsane
Requires:       cuneiform


%description
YAGF is a graphical front-end for cuneiform OCR tool.

With YAGF you can open already scanned image files or obtain new images via
XSane (scanning results are automatically passed to YAGF). Once you have a
scanned image you can prepare it for recognition, select particular image
areas for recognition, set the recognition language and so no.

Recognized text is displayed in a editor window where it can be corrected,
saved to disk or copied to clipboard. 

YAGF also provides some facilities for a multi-page recognition (see the
online help for more details).


%prep
%setup -q


%build
cmake ./
make %{?_smp_mflags} CPACK_PREFX=/usr/

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}


%files 
%defattr(-, root, root, 0755)
%doc README COPYING DESCRIPTION AUTHORS ChangeLog
%{_bindir}/yagf
%{_libdir}/yagf/*
%{_datadir}/yagf/translations/*.qm
%{_datadir}/pixmaps/*.png
%{_datadir}/icons/hicolor/*
%{_datadir}/applications/*.desktop
    

%changelog
* Wed Mar 21 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.9-1.R
- update to 0.9.0

* Mon Dec 19 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.8.9-1.R
- update to 0.8.9

* Thu Jun  7 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.8.6-1
- update to 0.8.6

* Sat Jan 29 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.8.5-1
- update to 0.8.5

* Wed Jan 12 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.8.3-1
- update to 0.8.3

* Thu Nov  8 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.8.1-1
- initial build for Fedora
- review spec file from official src.rpm of Andrei Borovsky
- added R: cuneiform, xsane
