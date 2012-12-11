Summary:    A transparent application input fuzzer
Name:		zzuf
Version:	0.13
Release:	%mkrel 2
Source0:	http://libcaca.zoy.org/files/%name/%name-%version.tar.gz
License:	WTFPL
Group:		Development/Other
Url:		http://libcaca.zoy.org/wiki/%name
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
%_mandir/man3/*
%_libdir/%name/*




%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.13-2mdv2011.0
+ Revision: 615784
- the mass rebuild of 2010.1 packages

* Mon Feb 01 2010 Oden Eriksson <oeriksson@mandriva.com> 0.13-1mdv2010.1
+ Revision: 499071
- 0.13

* Sun Jun 21 2009 Oden Eriksson <oeriksson@mandriva.com> 0.12-2mdv2010.0
+ Revision: 387577
- rebuild

* Sat Jun 14 2008 Pascal Terjan <pterjan@mandriva.org> 0.12-1mdv2009.0
+ Revision: 219182
- 0.12
- change license to its official canonical name

* Wed Jun 11 2008 Michael Scherer <misc@mandriva.org> 0.11-1mdv2009.0
+ Revision: 217987
- update to 0.11
- new url and new source url

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Jérôme Soyer <saispo@mandriva.org> 0.10-1mdv2008.1
+ Revision: 132020
- New release

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 18 2007 Michael Scherer <misc@mandriva.org> 0.9-1mdv2008.0
+ Revision: 53265
- new version

* Sat Apr 21 2007 Pascal Terjan <pterjan@mandriva.org> 0.8.1-1mdv2008.0
+ Revision: 16551
- 0.8.1
- Use autoconf2.5


* Mon Feb 26 2007 Pascal Terjan <pterjan@mandriva.org> 0.8-1mdv2007.0
+ Revision: 125870
- 0.8

* Sun Jan 28 2007 Michael Scherer <misc@mandriva.org> 0.6.1-1mdv2007.1
+ Revision: 114451
- version 0.6.1
- update to 0.6

* Thu Jan 18 2007 Michael Scherer <misc@mandriva.org> 0.5-1mdv2007.1
+ Revision: 110161
- Import zzuf

