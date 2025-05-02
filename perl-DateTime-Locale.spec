%define	upstream_name    DateTime-Locale

Name:       perl-%{upstream_name}
Version:    1.45
Release:    1

Summary:	Localization support for DateTime
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/release/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{version}.tar.gz

BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(File::ShareDir::Install)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
The DateTime::Locale perl module is primarily a factory for the various locale
subclasses used by DateTime. It also provides some functions for getting
information on available locales.

If you want to know what methods are available for locale objects, then please
read the DateTime::Locale::Base documentation.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor destdir=%{buildroot}
%make_build

# (tpg) disable it as this module needs a lot of packages to install to finish test
%if 0
%check
make test
%endif

%install
%make_install

%files
%{perl_vendorlib}/auto
%{perl_vendorlib}/DateTime
%{_mandir}/*/*
