Summary:	A Gtk-- ICQ2000 Client
Summary(fr):	Klient ICQ2000 przeznaczony dla Gtk--
Name:		ickle
Version:	0.3.1
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://unc.dl.sourceforge.net/sourceforge/ickle/%{name}-%{version}.tar.gz
URL:		http://ickle.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gtkmm-devel >= 1.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libsigc++-devel >= 1.0.0
BuildRequires:	ORBit-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define         _sysconfdir     /etc/X11

%description
ickle is an open-source project implementing the ICQ2000 protocol. The
aim is to bring the most useful features of ICQ2000 to non-windows
platforms.

%description -l pl
ickle to projekt open-source implementuj±cy protokó³ ICQ2000. Celem
jest dostarczenie wszelkich mo¿liwo¶ci ICQ2000 dla nie-windowsowych
platform.

%package devel
Summary:	Header files and develpment documentation for libicq2000
Summary(pl):	Pliki nag³ówkowe i dokumetacja do libicq2000
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libsigc++-devel
Requires:	libstdc++-devel

%description devel
Header files and develpment documentation for libicq2000.

%description devel -l pl
Pliki nag³ówkowe i dokumetacja do libicq2000.

%package static
Summary:	Static libicq2000 library
Summary(pl):	Biblioteka statyczna libicq2000
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libicq2000 library.

%description static -l pl
Biblioteka statyczna libicq2000.

%prep
%setup -q

%build
%configure \
	--with-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Network/Communications

gzip -9nf AUTHORS ChangeLog NEWS README TODO scripts/*.pl

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz scripts/*.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_sysconfdir}/CORBA/servers/*
%{_applnkdir}/Network/Communications/*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
