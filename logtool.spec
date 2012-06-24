Summary:	A handy syslog file(s) manipulation/monitoring/parsing tool
Summary(pl):	Por�czne narz�dzie do manipulowania/monitorowania/parsowania plik�w sysloga
Name:		logtool
Version:	1.1.0
Release:	3
License:	GPL
Group:		Applications/Text
Source0:	http://www.xjack.org/logtool/logtool/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_fixes.patch
URL:		http://www.xjack.org/logtool/
BuildRequires:	autoconf
BuildRequires:	automake
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir /etc/logtool

%description
Logtool is a handy little tool for manipulation/monitoring/parsing of
syslog (and syslog-like) files. It produces output in ANSI, ASCII,
CSV, HTML format, and is easily configured to your needs via the
/etc/logtool/* files. It is suitable for use in generating easy to
read logfile reports, webpages, and online monitoring of logfiles.

%description -l pl
Logtool jest por�cznym narz�dziem do obrabiania/monitorowania/
parsowania plik�w sysloga i podobnych. Mo�e produkowa� wyniki w
postaci ANSI, ASCII, CSV, HTML; jest �atwo konfigurowalny do potrzeb
poprzez pliki /etc/logtool/*. Nadaje si� do generowania �atwych do
czytania raport�w, stron WWW oraz monitorowania log�w on-line.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal
%{__autoconf}
automake -a -c || :
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man1}

install conf/{include,exclude,logtool.conf,green,yellow} \
	$RPM_BUILD_ROOT%{_sysconfdir}
install logtool/logtool logtail/logtail	$RPM_BUILD_ROOT%{_bindir}

ln -sf logtool $RPM_BUILD_ROOT%{_bindir}/lt

gzip -9nf README TODO CHANGES USAGE CREDITS doc/logtool.txt doc/examples/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz doc/examples
%attr(750,root,root) %dir %{_sysconfdir}
%config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
