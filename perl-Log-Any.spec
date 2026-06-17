#
# Conditional build:
%bcond_without	tests		# unit tests

%define		pdir	Log
%define		pnam	Any
Summary:	Log::Any -- Bringing loggers and listeners together
Summary(pl.UTF-8):	Log::Any - połączenie mechanizmów logujących i nasłuchujących
Name:		perl-Log-Any
Version:	1.720
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Log/PREACTION/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d501159dea15564229a9cc85d62a9568
URL:		https://metacpan.org/dist/Log-Any
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Any allows CPAN modules to safely and efficiently log messages,
while letting the application choose (or decline to choose) a logging
mechanism such as Log::Dispatch or Log::Log4perl.

Log::Any has a very tiny footprint and no dependencies beyond Perl
5.6, which makes it appropriate for even small CPAN modules to use. It
defaults to 'null' logging activity, so a module can safely log
without worrying about whether the application has chosen (or will
ever choose) a logging mechanism.

The application, in turn, may choose one or more logging mechanisms
via Log::Any::Adapter.

%description -l pl.UTF-8
Log::Any pozwala modułom CPAN bezpiecznie i wydajnie logować
komunikaty, pozwalając aplikacjon wybrać mechanizm logujący (lub
odmówić jego wyboru), jak np. Log::Dispatch lub Log::Log4perl.

Log::Any ma bardzo mały narzut i brak zależności poza Perlem 5.6, co
czyni go odpowiednim do użycia nawet w małych modułach CPAN. Domyślnie
wybierana jest aktywność logowania "null", więc moduł może bezpiecznie
logować bez obawy, czy aplikacja wybrała (lub kiedykolwiek wybierze)
mechanizm logowania.

Aplikacja z kolei może wybrać jeden lub więcej mechanizmów logowania
poprzez Log::Any::Adapter.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%if %{with tests}
%{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Log/Any.pm
%{perl_vendorlib}/Log/Any
%{_mandir}/man3/Log::Any*.3pm*
