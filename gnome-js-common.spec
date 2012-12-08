%define major 0.1
%define minor 2

Summary:	Common JavaScript modules for GNOME
Name:		gnome-js-common
Version:	%{major}.%{minor}
Release:	3
Epoch:		1
License:	GPLv3
Group:		Development/Other
Url:		http://www.gnome.org
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{major}/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	intltool

%description
gnome-js-common is a module holding tests and JavaScript code useful
or common to both Seed and gjs.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --datadir=%{_datadir} --libdir=%{_datadir}
%make

%install
%makeinstall_std gnome_js_commondocdir=%{_datadir}/doc/%{name}

%check
make check

%files
%doc %{_datadir}/doc/%{name}
%{_datadir}/gnome-js
%{_datadir}/pkgconfig/gnome-js-common.pc


%changelog
* Fri Apr 13 2012 Franck Bui <franck.bui@mandriva.com> 1:0.1.2-2mdv2012.0
+ Revision: 790483
- Remove seed and gjs BRs, they're optional and used by %%check if present
- libtool BR is no more needed (./autogen.sh is gone)
- Clean up only: whitespaces, curly braces added...

* Fri Apr 13 2012 Götz Waschk <waschk@mandriva.org> 1:0.1.2-1
+ Revision: 790476
- use real release 0.1.2 and add epoch

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2-3
+ Revision: 664869
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-2mdv2011.0
+ Revision: 605471
- rebuild

* Fri Jan 01 2010 Götz Waschk <waschk@mandriva.org> 0.2-1mdv2010.1
+ Revision: 484675
- update to new version 0.2

* Sat Jul 11 2009 Götz Waschk <waschk@mandriva.org> 0.1.1-1mdv2010.0
+ Revision: 394710
- update to new version 0.1.1

* Fri May 29 2009 Götz Waschk <waschk@mandriva.org> 0.1-0.20090529.1mdv2010.0
+ Revision: 381105
- import gnome-js-common


