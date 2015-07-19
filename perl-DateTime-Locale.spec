%define	upstream_name    DateTime-Locale
%define upstream_version 0.45

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    14
Epoch:		2

Summary:	Localization support for DateTime
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Params::Validate) >= 0.72
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
The DateTime::Locale perl module is primarily a factory for the various locale
subclasses used by DateTime. It also provides some functions for getting
information on available locales.

If you want to know what methods are available for locale objects, then please
read the DateTime::Locale::Base documentation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor destdir=%{buildroot}
./Build

%check
./Build test

%install
./Build install

%files
%doc Changes README
%{perl_vendorlib}/DateTime
%{_mandir}/*/*


%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 2:0.450.0-2mdv2011.0
+ Revision: 681392
- mass rebuild

* Mon Mar 22 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:0.450.0-1mdv2011.0
+ Revision: 526444
- update to 0.45

* Mon Sep 14 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:0.440.0-1mdv2010.0
+ Revision: 439431
- update to 0.44

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:0.430.0-1mdv2010.0
+ Revision: 406976
- rebuild using %%perl_convert_version

* Wed Jul 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2:0.43-1mdv2010.0
+ Revision: 391182
- update to new version 0.43

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2:0.42-1mdv2009.1
+ Revision: 292132
- update to new version 0.42

* Wed Jul 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2:0.41-1mdv2009.0
+ Revision: 236267
- fix build dependencies
- update to new version 0.41

* Tue Jan 22 2008 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:0.35-2mdv2008.1
+ Revision: 156519
- force 5.10.0 rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2:0.35-1mdv2008.1
+ Revision: 98028
- update to new version 0.35
- update to new version 0.35

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 2:0.34-2mdv2008.0
+ Revision: 67817
- rebuild

* Sun Apr 29 2007 Olivier Thauvin <nanardon@mandriva.org> 2:0.34-1mdv2008.0
+ Revision: 19317
- 0.34


* Sun Jan 28 2007 Scott Karns <scottk@mandriva.org> 0.33-2mdv2007.0
+ Revision: 114571
- Bumped revision
- \- Updated source URL- Updated dependencies per META.yml- Fixed file ownership

* Mon Jan 08 2007 Olivier Thauvin <nanardon@mandriva.org> 2:0.33-1mdv2007.1
+ Revision: 106112
- 0.33

* Sat Dec 09 2006 Olivier Thauvin <nanardon@mandriva.org> 2:0.32-1mdv2007.1
+ Revision: 93933
- 0.32
- Import perl-DateTime-Locale

* Tue Jun 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2:0.22-1mdk
- 0.22
- Make rpmbuildhappy

* Sat Apr 02 2005 Olivier Thauvin <nanardon@mandrake.org> 0.21-4mdk
- put epoch to get this package upload

* Sat Apr 02 2005 Olivier Thauvin <nanardon@mandrake.org> 0.21-3mdk
- create %%check section

* Sat Apr 02 2005 Olivier Thauvin <nanardon@mandrake.org> 0.21-2mdk
- BuildRequires

* Mon Mar 07 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.21-1mdk
- 0.21

* Mon Nov 01 2004 Michael Scherer <misc@mandrake.org> 0.09-2mdk
- BuildRequires

* Fri Aug 27 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.09-1mdk
- Initial MDK release.

