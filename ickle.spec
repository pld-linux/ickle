Summary:	A Gtk-- ICQ2000 Client
Summary(pl):	Klient ICQ2000 przeznaczony dla Gtk--
Name:		ickle
Version:	0.3.1
Release:	3
License:	GPL v2
Group:		Applications/Communications
Source0:	http://unc.dl.sourceforge.net/sourceforge/ickle/%{name}-%{version}.tar.gz
URL:		http://ickle.sourceforge.net/
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gtkmm-devel >= 1.2.0
BuildRequires:	libicq2000-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libsigc++-devel >= 1.0.0
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

%prep
%setup -q

%build
%configure \
	--with-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Network/Communications

# why it is not installed by the command above ?
install ickle/ickle_applet.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO scripts/*.pl
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/CORBA/servers/*
%{_applnkdir}/Network/Communications/*
%{_datadir}/%{name}
%{_mandir}/man1/*
