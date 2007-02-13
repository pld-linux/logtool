Summary:	A handy syslog file(s) manipulation/monitoring/parsing tool
Summary(pl.UTF-8):	Poręczne narzędzie do manipulowania/monitorowania/parsowania plików sysloga
Name:		logtool
Version:	1.1.0
Release:	4
License:	GPL
Group:		Applications/Text
Source0:	http://www.xjack.org/logtool/logtool/%{name}-%{version}.tar.gz
# Source0-md5:	1c51da0ee599441200c74f761c617139
Patch0:		%{name}-ac_fixes.patch
URL:		http://www.xjack.org/logtool/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir /etc/logtool

%description
Logtool is a handy little tool for manipulation/monitoring/parsing of
syslog (and syslog-like) files. It produces output in ANSI, ASCII,
CSV, HTML format, and is easily configured to your needs via the
/etc/logtool/* files. It is suitable for use in generating easy to
read logfile reports, webpages, and online monitoring of logfiles.

%description -l pl.UTF-8
Logtool jest poręcznym narzędziem do obrabiania/monitorowania/
parsowania plików sysloga i podobnych. Może produkować wyniki w
postaci ANSI, ASCII, CSV, HTML; jest łatwo konfigurowalny do potrzeb
poprzez pliki /etc/logtool/*. Nadaje się do generowania łatwych do
czytania raportów, stron WWW oraz monitorowania logów on-line.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man1}

install conf/{include,exclude,logtool.conf,green,yellow} \
	$RPM_BUILD_ROOT%{_sysconfdir}
install logtool/logtool logtail/logtail	$RPM_BUILD_ROOT%{_bindir}

ln -sf logtool $RPM_BUILD_ROOT%{_bindir}/lt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO CHANGES USAGE CREDITS doc/logtool.txt doc/examples
%attr(750,root,root) %dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
