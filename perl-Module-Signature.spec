%define	upstream_name	 Module-Signature
%define upstream_version 0.68

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:	Check and create SIGNATURE files for CPAN distributions
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(PAR::Dist)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(IPC::Run)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This is a perl module to check and create SIGNATURE files
for CPAN distributions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps </dev/null
%make

%check
%make test

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
