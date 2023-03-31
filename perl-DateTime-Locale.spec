%define	upstream_name    DateTime-Locale
%define upstream_version 1.25

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    4
Epoch:		2

Summary:	Localization support for DateTime
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/release/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Params::Validate) >= 0.72
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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor destdir=%{buildroot}
%make

# (tpg) disable it as this module needs a lot of packages to install to finish test
%if 0
%check
make test
%endif

%install
%makeinstall_std

%files
%{perl_vendorlib}/auto
%{perl_vendorlib}/DateTime
%{_mandir}/*/*
