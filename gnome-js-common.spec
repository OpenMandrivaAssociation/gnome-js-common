%define major 0.1
%define minor 2
%define version %{major}.%{minor}

Summary:	Common JavaScript modules for GNOME
Name:		gnome-js-common
Epoch:		1
Version:	0.1.2
Release:	2
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

