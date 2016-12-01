Name:           qwt
Version:        6.1.3
Release:        1%{?dist}
Summary:        2D plotting widget extension to the Qt GUI

License:        LGPL
URL:            http://qwt.sourceforge.net/
Source0:        http://downloads.sourceforge.net/qwt/qwt-%{version}.tar.bz2
Patch0:         qwt6-install-paths.patch
Patch1:         qwt6-pkgconfig.patch
Patch2:         designer-disable-rpath.patch

BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(QtSvg)
BuildRequires:  pkgconfig(QtDesigner)


%description
The Qwt library contains GUI Components and utility classes which are primarily
useful for programs with a technical background. Beside a framework for 2D plots
it provides scales, sliders, dials, compasses, thermometers, wheels and knobs to
control or display values, arrays, or ranges of type double.


%package        devel
Summary:        Development files and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
Headers and libraries for developing applications that use %{name}
functionality.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1


%build
%{qmake_qt4} QWT_CONFIG+=QwtPkgConfig
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install INSTALL_ROOT=%{buildroot}

mv %{buildroot}%{_qt4_docdir}/html/html \
   %{buildroot}%{_qt4_docdir}/html/qwt

rm -rf %{buildroot}%{_qt4_docdir}/html/man/


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc CHANGES-6.1 COPYING README
%{_qt4_libdir}/libqwt.so.6*
%{_qt4_libdir}/libqwtmathml.so.6*
%{?_qt4_plugindir}/designer/libqwt_designer_plugin.so

%files devel
%{_qt4_headerdir}/qwt/
%{_qt4_libdir}/libqwt.so
%{_qt4_libdir}/libqwtmathml.so
%{_qt4_libdir}/qt4/mkspecs/features/*
%{_qt4_libdir}/pkgconfig/qwt.pc
%{_qt4_libdir}/pkgconfig/qwtmathml.pc
%dir %{_qt4_docdir}
%dir %{_qt4_docdir}/html/
%{_qt4_docdir}/html/qwt/


%changelog
* Thu Dec 01 2016 Jajauma's Packages <jajauma@yandex.ru> - 6.1.3-1
- Public release
