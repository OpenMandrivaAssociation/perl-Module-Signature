%define	upstream_name	 Module-Signature
%define upstream_version 0.68

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Check and create SIGNATURE files for CPAN distributions
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(PAR::Dist)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(IPC::Run)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is a perl module to check and create SIGNATURE files
for CPAN distributions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/man*/*
%{perl_vendorlib}/Module


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.680.0-4mdv2012.0
+ Revision: 765492
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 0.680.0-2
+ Revision: 763093
- rebuild

* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.680.0-1
+ Revision: 674666
- update to new version 0.68

* Thu May 05 2011 Funda Wang <fwang@mandriva.org> 0.670.0-2
+ Revision: 669257
- add br

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 0.67

* Sun Nov 07 2010 Shlomi Fish <shlomif@mandriva.org> 0.660.0-1mdv2011.0
+ Revision: 594706
- New version

* Mon Sep 06 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.650.0-1mdv2011.0
+ Revision: 576303
- update to 0.65

* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.640.0-1mdv2011.0
+ Revision: 552415
- update to 0.64

* Sun Mar 28 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.630.0-1mdv2010.1
+ Revision: 528435
- update to 0.63

* Wed Mar 24 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.620.0-1mdv2010.1
+ Revision: 527095
- update to 0.62

* Thu Nov 19 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.610.0-1mdv2010.1
+ Revision: 467359
- update to 0.61

* Tue Nov 17 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.600.0-1mdv2010.1
+ Revision: 466750
- update to 0.60

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.550.0-1mdv2010.0
+ Revision: 407806
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.55-4mdv2009.0
+ Revision: 268619
- rebuild early 2009.0 package (before pixel changes)
- kill re-definition of %%buildroot on Pixel's request

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - patch: skip rpm-generated files when checking module signature

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.55-2mdv2008.0
+ Revision: 86655
- rebuild


* Sat Sep 02 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-02 18:24:56 (59619)
- 0.55

* Sat Sep 02 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-02 18:12:53 (59618)
Import perl-Module-Signature

* Thu Jun 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.54-1mdv2007.0
- New release 0.54
- spec cleanup
- don't ship empty directories

* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.53-2mdk
- Fix According to perl Policy
	- BuildRequires

* Fri Feb 10 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.53-1mdk
- 0.53

* Thu Jan 19 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.52-1mdk
- 0.52

* Tue Jan 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.51-1mdk
- 0.51

* Mon Aug 22 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.50-1mdk
- 0.50

* Thu Aug 18 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.45-1mdk
- 0.45

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.44-2mdk
- fix deps

* Thu Dec 16 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.44-1mdk
- 0.44

* Thu Dec 09 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.42-1mdk
- 0.42

* Thu Jul 08 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 0.41-1mdk
- 0.41

* Thu Jul 01 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.40-1mdk
- 0.40

* Sat Jun 19 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 0.39-1mdk
- 0.39
- drop redundant requires
- cosmetics

* Fri May 21 2004 Florin <florin@mandrakesoft.com> 0.42-1mdk
- first Mandrake Release

