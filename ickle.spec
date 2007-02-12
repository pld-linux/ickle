#
# TODO:
#	ickle.desktop

Summary:	A Gtk-- ICQ2000 Client
Summary(pl.UTF-8):   Klient ICQ2000 przeznaczony dla Gtk--
Name:		ickle
Version:	0.3.2
Release:	1
License:	GPL v2
Group:		Applications/Communications
# Source0-md5:	c59acbc24ac90cfc7fd21c49038481ed
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://ickle.sourceforge.net/
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gtkmm1-devel >= 1.2.0
BuildRequires:	libicq2000-devel >= 0.3.2
BuildRequires:	libstdc++-devel
BuildRequires:	libsigc++1-devel >= 1.0.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ickle is an open-source project implementing the ICQ2000 protocol. The
aim is to bring the most useful features of ICQ2000 to non-windows
platforms.

%description -l pl.UTF-8
ickle to projekt open-source implementujący protokół ICQ2000. Celem
jest dostarczenie wszelkich możliwości ICQ2000 dla nie-windowsowych
platform.

%prep
%setup -q

%build
%configure \
	--with-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_applnkdir}/Network/Communications}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install ickle/ickle_applet.desktop $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

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
%{_applnkdir}/Network/Communications/*
%{_datadir}/%{name}
%{_mandir}/man1/*
