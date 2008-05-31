%define	module	Module-Signature
%define	name	perl-%{module}
%define	version	0.55
%define	release	%mkrel 3

Version:	%{version}
Name:		%{name}
Release:	%{release}
Summary:	Check and create SIGNATURE files for CPAN distributions
License:	Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Module/%{module}-%{version}.tar.gz
Patch:      Module-Signature-0.55-skip-rpm-files.patch
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(PAR::Dist)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is a perl module to check and create SIGNATURE files
for CPAN distributions.

%prep
%setup -q -n %{module}-%{version}
%patch -p 1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps </dev/null
%make

%check
%__make test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS Changes README
%{_bindir}/*
%{_mandir}/man*/*
%{perl_vendorlib}/Module

