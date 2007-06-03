Summary:	A handy syslog file(s) manipulation/monitoring/parsing tool
Summary(pl.UTF-8):	Poręczne narzędzie do manipulowania/monitorowania/parsowania plików sysloga
Name:		logtool
Version:	1.2.8
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.xjack.org/logtool/logtool/%{name}-%{version}.tar.gz
# Source0-md5:	f596fd2057fe5f3293ca054dd14a3c10
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
sed -i 's/-o root //'  src/Makefile.in

%build
#rm -f missing
#%{__aclocal}
%{__autoconf}
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING TODO INSTALL CHANGES USAGE CREDITS doc/* scripts/*
%attr(750,root,root) %dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
