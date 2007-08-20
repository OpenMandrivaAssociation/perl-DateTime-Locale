%define	module		DateTime-Locale
%define	modprefix	DateTime
%define	name		perl-%{module}
%define	version		0.34
%define	release		%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Localization support for DateTime
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://www.cpan.org/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Params::Validate) >= 0.72
Epoch:		2

%description
The DateTime::Locale perl module is primarily a factory for the various locale
subclasses used by DateTime. It also provides some functions for getting
information on available locales.

If you want to know what methods are available for locale objects, then please
read the DateTime::Locale::Base documentation.

%prep
%setup -q -n %{module}-%{version}

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
%{perl_vendorlib}/%{modprefix}
%{_mandir}/*/*


