%define rel 1

Summary:    A transparent application input fuzzer	
Name:		zzuf
Version:	0.8.1
Release:	%mkrel %rel
Source0:	http://sam.zoy.org/%name/%name-%version.tar.bz2
License:	DWTFYWTPL
Group:		Development/Other
Url:		http://sam.zoy.org/%name/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	autoconf2.5

%description
zzuf is a transparent application input fuzzer. Its purpose is to find bugs in 
applications by corrupting their user-contributed data (which more than often
comes from untrusted sources on the Internet). It works by intercepting file 
and network operations and changing random bits in the program?s input. 

zzuf's behaviour is deterministic, making it easier to reproduce bugs. Its 
main areas of use are: 
   quality assurance: use zzuf to test existing software, or integrate it 
      into your own software?s testsuite
   security: very often, segmentation faults or memory corruption issues 
      mean a potential security hole, zzuf helps exposing some of them

zzuf's primary target is media players, image viewers and web browsers, 
because the data they process is inherently insecure, but it was also 
successfully used to find bugs in system utilities such as objdump.
%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -f %_libdir/%name/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root) 
%_bindir/*
%_mandir/man1/*
%_libdir/%name/*


