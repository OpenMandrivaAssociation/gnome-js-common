%define name gnome-js-common
%define version 0.1.2
%define release %mkrel 1

Summary: Common JavaScript modules for GNOME
Name: %{name}
Version: %{version}
Release: %{release}
Epoch: 1
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
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
%setup -q

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
