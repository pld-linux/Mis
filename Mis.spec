Summary:	GUI for poldek package manager
Summary(pl.UTF-8):   GUI dla menadżera pakietów poldek
Name:		Mis
Version:	0.0.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://mis.troll.one.pl/download/%{name}-%{version}.tar.gz
# Source0-md5:	b3347e63da0514e35b19c09aa811b49d
URL:		http://mis.troll.one.pl/
Requires:	poldek
Requires:	perl-gtk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mis is perl-gtk library based GUI for poldek package manager. It
provides basic functionality of poldek - package database searching,
installing, upgrading, uninstalling, etc.

%description -l en.UTF-8
Miś is perl-gtk library based GUI for poldek package manager. It
provides basic functionality of poldek - package database searching,
installing, upgrading, uninstalling, etc.

%description -l pl.UTF-8
Miś jest opartym o bibliotekę perl-gtk GUI dla menadżera pakietów
poldek. Zapewnia on podstawową funkcjonalność poldka - przeszukiwanie
bazy pakietów, instalacja, uaktualnianie, deinstalację, etc.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/mis,%{_bindir}}

install mis		$RPM_BUILD_ROOT%{_bindir}
install *.lang		$RPM_BUILD_ROOT%{_datadir}/mis

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/mis
%lang(pl) %{_datadir}/mis/pl_PL.lang
