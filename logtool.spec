Summary:	A handy syslog file(s) manipulation/monitoring/parsing tool
Vendor:		A.L.Lambert
Name:		logtool
Version:	1.0.5
Release:	1
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(pl):	Aplikacje/Tekst
License:	GPL
Source0:	%{name}-%{version}.tar.gz
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir /etc/logtool

%description
Logtool is a handy little tool for manipulation/monitoring/parsing of
syslog (and syslog-like) files. It produces output in ANSI, ASCII,
CSV, HTML format, and is easily configured to your needs via the
/etc/logtool/* files. It is suitable for use in generating easy to
read logfile reports, webpages, and online monitoring of logfiles.

Please see the included documentation files (which are located in
/usr/doc/%{name}-%{version}) for more details.

%prep
%setup -q  
%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man1}

install conf/{include,exclude,logtool.conf,green,yellow} \
					$RPM_BUILD_ROOT%{_sysconfdir}
install logtool/logtool logtail/logtail	$RPM_BUILD_ROOT%{_bindir}
install doc/logtool.1			$RPM_BUILD_ROOT%{_mandir}/man1

ln -sf %{_bindir}/logtool $RPM_BUILD_ROOT%{_bindir}/lt

gzip -9nf README TODO INSTALL CHANGES USAGE CREDITS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO,INSTALL,CHANGES,USAGE,CREDITS}.gz doc/examples
%attr(750,root,root) %dir %{_sysconfdir}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
