%define name gnome-js-common
%define version 0.2
%define git 20090529
%if %git
%define release %mkrel 1
%else
%define release %mkrel 1
%endif

Summary: Common JavaScript modules for GNOME
Name: %{name}
Version: %{version}
Release: %{release}
%if %git
Source0:       %{name}-%{git}.tar.bz2
%else
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
%endif
License: GPLv3
Group: Development/Other
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: seed-devel
BuildRequires: gjs-devel
BuildRequires: intltool
BuildRequires: libtool

%description
gnome-js-common is a module holding tests and JavaScript code useful
or common to both Seed and gjs.

%prep
%if %git
%setup -q -n %name
./autogen.sh -V
%else
%setup -q
%endif

%build
./configure --prefix=%_prefix --datadir=%_datadir --libdir=%_datadir
%make

%install
rm -rf %{buildroot}
%makeinstall_std gnome_js_commondocdir=%_datadir/doc/%name

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %_datadir/doc/%name
%_datadir/gnome-js
%_datadir/pkgconfig/gnome-js-common.pc
