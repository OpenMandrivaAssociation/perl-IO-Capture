%define upstream_name    IO-Capture
%define upstream_version 0.05
Name:		perl-%{upstream_name}
Version:	0.04
Release:	1

Summary:	IO::Capture- Abstract Base Class to build modules to capture output
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://metacpan.org/dist/IO-Capture
Source0:	https://cpan.metacpan.org/authors/id/R/RE/REYNOLDS/IO-Capture-0.05.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:  perl-Test-Simple
BuildArch:	noarch

%description
The IO::Capture Module defines an abstract base class that can be
used to create any number of useful sub-classes that capture
output being sent on a filehandle such as STDOUT or STDERR.

Several modules come with the distribution that define subclasses
of IO::Capture to do just that. (I.e., capture STDOUT and STDERR)
See the man page IO::Capture::Overview for a discussion of these
modules and how to build a module to sub-class the B<IO::Capture>
class yourself.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes
%dir %{perl_vendorlib}/IO/Capture
%{perl_vendorlib}/IO/Capture.pm
%{perl_vendorlib}/IO/Capture/*
%{_mandir}/*/*


