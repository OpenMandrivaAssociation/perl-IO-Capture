%define upstream_name    IO-Capture
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	IO::Capture- Abstract Base Class to build modules to capture output
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%dir %{perl_vendorlib}/IO/Capture
%{perl_vendorlib}/IO/Capture.pm
%{perl_vendorlib}/IO/Capture/*
%{_mandir}/*/*
