%define real_name IO-Capture

Summary:	IO::Capture- Abstract Base Class to build modules to capture output
Name:		perl-%{real_name}
Version:	0.05
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%setup -q -n %{real_name}-%{version} 

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

