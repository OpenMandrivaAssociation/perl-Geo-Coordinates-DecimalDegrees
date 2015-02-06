%define upstream_name    Geo-Coordinates-DecimalDegrees
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Convert between degrees/minutes/seconds and decimal degrees
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Geo/Geo-Coordinates-DecimalDegrees-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Number::Delta)
BuildArch:	noarch

%description
Latitudes and longitudes are most often presented in two common formats:
decimal degrees, and degrees, minutes and seconds. There are 60 minutes in
a degree, and 60 seconds in a minute. In decimal degrees, the minutes and
seconds are presented as a fractional number of degrees. For example, 1
degree 30 minutes is 1.5 degrees, and 30 minutes 45 seconds is 0.5125
degrees.

This module provides functions for converting between these two formats.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.80.0-2mdv2011.0
+ Revision: 654967
- rebuild for updated spec-helper

* Mon Jun 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 381784
- adding missing buildrequires:
- import perl-Geo-Coordinates-DecimalDegrees


* Sun May 31 2009 cpan2dist 0.08-1mdv
- initial mdv release, generated with cpan2dist


