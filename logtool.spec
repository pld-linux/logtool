Summary:	A handy syslog file(s) manipulation/monitoring/parsing tool
Vendor:		A.L.Lambert <al@9b.com>
Name:		logtool
Version:	1.1.0
Release:	1
License:	GPL
Source0:	http://users.digitex.net/~max/logtool/%{name}-%{version}.tar.gz
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(pl):	Aplikacje/Tekst
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir /etc/logtool

%description
Logtool is a handy little tool for manipulation/monitoring/parsing of
syslog (and syslog-like) files. It produces output in ANSI, ASCII,
CSV, HTML format, and is easily configured to your needs via the
/etc/logtool/* files. It is suitable for use in generating easy to
read logfile reports, webpages, and online monitoring of logfiles.

%prep
%setup -q  

%build
%{__make} clean
%configure 
%{__make} CFLAGS="%{rpmcflags} -ansi -pedantic -DHAVE_CONFIG_H"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man1}

install conf/{include,exclude,logtool.conf,green,yellow} \
					$RPM_BUILD_ROOT%{_sysconfdir}
install logtool/logtool logtail/logtail	$RPM_BUILD_ROOT%{_bindir}

ln -sf ./logtool $RPM_BUILD_ROOT%{_bindir}/lt


gzip -9nf README TODO CHANGES USAGE CREDITS doc/logtool.txt doc/examples/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO,CHANGES,USAGE,CREDITS}.gz doc/*.gz doc/examples
%attr(750,root,root) %dir %{_sysconfdir}
%config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
