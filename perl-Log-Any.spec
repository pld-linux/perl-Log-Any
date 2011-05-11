#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Log
%define		pnam	Any
%include	/usr/lib/rpm/macros.perl
Summary:	Log::Any -- Bringing loggers and listeners together
#Summary(pl.UTF-8):	
Name:		perl-Log-Any
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Log/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eaab5035d69af58eab72e19140c5f246
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Log-Any/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Any allows CPAN modules to safely and efficiently log messages, while
letting the application choose (or decline to choose) a logging mechanism such
as Log::Dispatch or Log::Log4perl.

Log::Any has a very tiny footprint and no dependencies beyond Perl 5.6,
which makes it appropriate for even small CPAN modules to use. It defaults to
'null' logging activity, so a module can safely log without worrying about
whether the application has chosen (or will ever choose) a logging mechanism.

The application, in turn, may choose one or more logging mechanisms via
Log::Any::Adapter.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%{perl_vendorlib}/Log/*.pm
%{perl_vendorlib}/Log/Any
%{_mandir}/man3/*
