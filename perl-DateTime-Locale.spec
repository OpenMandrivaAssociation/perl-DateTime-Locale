%define	upstream_name    DateTime-Locale
%define upstream_version 0.45

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2
Epoch:		2

Summary:	Localization support for DateTime
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Params::Validate) >= 0.72
BuildRequires:	perl(List::MoreUtils)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The DateTime::Locale perl module is primarily a factory for the various locale
subclasses used by DateTime. It also provides some functions for getting
information on available locales.

If you want to know what methods are available for locale objects, then please
read the DateTime::Locale::Base documentation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor destdir=%{buildroot}
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/DateTime
%{_mandir}/*/*
