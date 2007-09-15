%define	module	Module-Signature
%define	name	perl-%{module}
%define	version	0.55
%define	release	%mkrel 2

Version:	%{version}
Name:		%{name}
Release:	%{release}
Summary:	Check and create SIGNATURE files for CPAN distributions
License:	Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Module/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(PAR::Dist)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is a perl module to check and create SIGNATURE files
for CPAN distributions.

%prep
%setup -q -n %{module}-%{version}

%build
(echo -n y; yes n) | \
(%{__perl} Makefile.PL INSTALLDIRS=vendor
%make)

%check
yes n | %__make test

%install
rm -rf %{buildroot}
yes n | %{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS Changes README
%{_bindir}/*
%{_mandir}/man*/*
%{perl_vendorlib}/Module

