Summary:	GUI for poldek package manager
Summary(pl):	GUI dla menad¿era pakietów poldek
Name:		Mis
Version:	0.0.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://mis.troll.one.pl/download/%{name}-%{version}.tar.gz
URL:		http://mis.troll.one.pl/
Requires:	poldek
Requires:	perl-gtk
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mi¶ is perl-gtk library based GUI for poldek package manager. It
provides basic functionality of poldek - package database searching,
installing, upgrading, uninstalling, etc.

%description -l pl
Mi¶ jest opartym o bibliotekê perl-gtk GUI dla menad¿era pakietów
poldek. Zapewnia on podstawow± funkcjonalno¶æ poldka - przeszukiwanie
bazy pakietów, instalacja, uaktualnianie, deinstalacjê, etc.

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/mis/,%{_bindir}}

install mis		$RPM_BUILD_ROOT%{_bindir}
install *.lang		$RPM_BUILD_ROOT%{_datadir}/mis/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO 
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/mis/*
