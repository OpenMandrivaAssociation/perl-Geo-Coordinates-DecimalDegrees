%define upstream_name    Geo-Coordinates-DecimalDegrees
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Convert between degrees/minutes/seconds and decimal degrees
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Geo/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::Number::Delta)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


