%define	modname	Module-Signature
%define modver 0.83

Summary:	Check and create SIGNATURE files for CPAN distributions
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Module/Module-Signature-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(inc::Module::Install)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(PAR::Dist)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(IPC::Run)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
This is a perl module to check and create SIGNATURE files
for CPAN distributions.

%prep
%autosetup -n %{modname}-%{modver} -p1

%build
%__perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" --skipdeps </dev/null
%make_build

%check
%make test

%install
%make_install

%files
%doc AUTHORS Changes README
%{_bindir}/*
%{perl_vendorlib}/Module
%{_mandir}/man1/*
%{_mandir}/man3/*


