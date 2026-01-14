#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Rose
%define	pnam	DateTime
Summary:	Rose::DateTime - DateTime helper functions and objects.
#Summary(pl.UTF-8):	
Name:		perl-Rose-DateTime
Version:	0.537
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Rose/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3215b1185f8668f257a324efb464853e
URL:		http://search.cpan.org/dist/Rose-DateTime/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
# FAIL: circular dependency
#BuildRequires:	perl(Rose::Object) >= 0.82
BuildRequires:	perl-DateTime
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Rose::DateTime::* modules provide a few convenience functions
and objects for use with DateTime dates.

Rose::DateTime::Util contains a simple date parser and a slightly
customized date formatter.

Rose::DateTime::Parser encapsulates a date parser with an associated
default time zone.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

# the "||:" added due to the circular dependency with perl-Rose-Object
%{?with_tests:%{__make} test ||:}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Rose/*.pm
%{perl_vendorlib}/Rose/DateTime
%{_mandir}/man3/*
