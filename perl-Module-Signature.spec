%define	modname	Module-Signature
%define modver	0.68

Summary:	Check and create SIGNATURE files for CPAN distributions
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	7
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Module/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(PAR::Dist)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(IPC::Run)
BuildRequires:	perl-devel

%description
This is a perl module to check and create SIGNATURE files
for CPAN distributions.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor --skipdeps </dev/null
%make

%check
%make test

%install
%makeinstall_std

%files
%doc AUTHORS Changes README
%{_bindir}/*
%{perl_vendorlib}/Module
%{_mandir}/man1/*
%{_mandir}/man3/*

