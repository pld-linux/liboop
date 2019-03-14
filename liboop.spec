#
# Condional build:
%bcond_without	libwww	# W3C libwww binding
#
Summary:	Libraries for low-level event loop management
Summary(pl.UTF-8):	Biblioteki do zarządzania niskopoziomowymi pętlami
Name:		liboop
Version:	1.0
Release:	7
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://download.ofb.net/liboop/%{name}-%{version}.tar.bz2
# Source0-md5:	88fc8decf99fd75d2af40e0a005fa0d3
Patch0:		%{name}-libwww-fix.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-tcl.patch
Patch3:		%{name}-build.patch
URL:		http://liboop.ofb.net/
BuildRequires:	adns-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.7
BuildRequires:	glib-devel
BuildRequires:	glib2-devel
BuildRequires:	libtool >= 1.4
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	tcl-devel >= 8.3.4-10
%{?with_libwww:BuildRequires:	w3c-libwww-devel}
Obsoletes:	liboop-bindings
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
liboop is a low-level event loop management library for POSIX-based
operating systems. It supports the development of modular, multiplexed
applications which may respond to events from several sources. It
replaces the "select() loop" and allows the registration of event
handlers for file and network I/O, timers and signals. Since processes
use these mechanisms for almost all external communication, liboop can
be used as the basis for almost any application.

%description -l pl.UTF-8
liboop jest biblioteką do zarządzania niskopoziomowymi pętlami w
systemach opartych na POSIX. Zawiera ona wsparcie umożliwiające rozwój
modularnych, zwielokrotnionych aplikacji, które mogą reagować na
zdarzenia pochodzące z kilku źródeł. Zastępuje ona "pętlę select()" i
umożliwia rejestrację funkcji obsługi zdarzeń dla plikowego i
sieciowego we/wy, zegarów i sygnałów. Ze względu na to, że procesy
korzystają z tych mechanizmów przy praktycznie każdej komunikacji z
otoczeniem, można używać liboop jako podstawy dla prawie wszystkich
aplikacji.

%package devel
Summary:	Header files for liboop
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki liboop
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	liboop-bindings-devel

%description devel
liboop is a low-level event loop management library.

This package contains the header files needed to write or compile
programs that use liboop library.

%description devel -l pl.UTF-8
liboop jest biblioteką do zarządzania niskopoziomowymi pętlami.

Ten pakiet zawiera pliki nagłówkowe potrzebne do kompilowania
programów używających biblioteki liboop.

%package static
Summary:	Static liboop library
Summary(pl.UTF-8):	Statyczna biblioteka liboop
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liboop library.

%description static -l pl.UTF-8
Statyczna biblioteka liboop.

%package binding-adns
Summary:	liboop binding for adns library
Summary(pl.UTF-8):	Biblioteka wiążąca liboop z biblioteką adns
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description binding-adns
liboop binding for adns library.

%description binding-adns -l pl.UTF-8
Biblioteka wiążąca liboop z biblioteką adns.

%package binding-adns-devel
Summary:	Header file for liboop adns binding library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki wiążącej liboop z biblioteką adns
Group:		Development/Libraries
Requires:	%{name}-binding-adns = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	adns-devel

%description binding-adns-devel
liboop is a low-level event loop management library.

This package contains the header file needed to write or compile
programs that use liboop adns binding library.

%description binding-adns-devel -l pl.UTF-8
liboop jest biblioteką do zarządzania niskopoziomowymi pętlami.

Ten pakiet zawiera plik nagłówkowy potrzebny do kompilowania
programów używających biblioteki wiążącej liboop z adns.

%package binding-adns-static
Summary:	Static liboop adns binding library
Summary(pl.UTF-8):	Statyczna biblioteka wiążąca liboop z adns
Group:		Development/Libraries
Requires:	%{name}-binding-adns-devel = %{version}-%{release}

%description binding-adns-static
Static liboop adns binding library.

%description binding-adns-static -l pl.UTF-8
Statyczna biblioteka wiążąca liboop z adns.

%package binding-glib-common-devel
Summary:	Header file for liboop GLib bindings
Summary(pl.UTF-8):	Plik nagłówkowy wiązań liboop z bibliotekami GLib
Group:		Development/Librares
Requires:	%{name}-devel = %{version}-%{release}

%description binding-glib-common-devel
Header file for liboop GLib bindings.

%description binding-glib-common-devel -l pl.UTF-8
Plik nagłówkowy wiązań liboop z bibliotekami GLib.

%package binding-glib
Summary:	liboop binding for GLib 1.x library
Summary(pl.UTF-8):	Biblioteka wiążąca liboop z biblioteką GLib 1.x
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description binding-glib
liboop binding for GLib 1.x library.

%description binding-glib -l pl.UTF-8
Biblioteka wiążąca liboop z biblioteką GLib 1.x.

%package binding-glib-devel
Summary:	Development files for liboop GLib 1.x binding library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki wiążącej liboop z biblioteką GLib 1.x
Group:		Development/Libraries
Requires:	%{name}-binding-glib = %{version}-%{release}
Requires:	%{name}-binding-glib-common-devel = %{version}-%{release}
Requires:	glib-devel

%description binding-glib-devel
liboop is a low-level event loop management library.

This package contains development files needed to write or compile
programs that use liboop GLib 1.x binding library.

%description binding-glib-devel -l pl.UTF-8
liboop jest biblioteką do zarządzania niskopoziomowymi pętlami.

Ten pakiet zawiera pliki programistyczne potrzebne do kompilowania
programów używających biblioteki wiążącej liboop z GLib 1.x.

%package binding-glib-static
Summary:	Static liboop GLib 1.x binding library
Summary(pl.UTF-8):	Statyczna biblioteka wiążąca liboop z GLib 1.x
Group:		Development/Libraries
Requires:	%{name}-binding-glib-devel = %{version}-%{release}

%description binding-glib-static
Static liboop GLib 1.x binding library.

%description binding-glib-static -l pl.UTF-8
Statyczna biblioteka wiążąca liboop z GLib 1.x.

%package binding-glib2
Summary:	liboop binding for GLib 2.x library
Summary(pl.UTF-8):	Biblioteka wiążąca liboop z biblioteką GLib 2.x
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description binding-glib2
liboop binding for GLib 2.x library.

%description binding-glib2 -l pl.UTF-8
Biblioteka wiążąca liboop z biblioteką GLib 2.x.

%package binding-glib2-devel
Summary:	Development files for liboop GLib 2.x binding library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki wiążącej liboop z biblioteką GLib 2.x
Group:		Development/Libraries
Requires:	%{name}-binding-glib2 = %{version}-%{release}
Requires:	%{name}-binding-glib-common-devel = %{version}-%{release}
Requires:	glib2-devel

%description binding-glib2-devel
liboop is a low-level event loop management library.

This package contains development files needed to write or compile
programs that use liboop GLib 2.x binding library.

%description binding-glib2-devel -l pl.UTF-8
liboop jest biblioteką do zarządzania niskopoziomowymi pętlami.

Ten pakiet zawiera pliki programistyczne potrzebne do kompilowania
programów używających biblioteki wiążącej liboop z GLib 2.x.

%package binding-glib2-static
Summary:	Static liboop GLib 2.x binding library
Summary(pl.UTF-8):	Statyczna biblioteka wiążąca liboop z GLib 2.x
Group:		Development/Libraries
Requires:	%{name}-binding-glib2-devel = %{version}-%{release}

%description binding-glib2-static
Static liboop GLib 2.x binding library.

%description binding-glib2-static -l pl.UTF-8
Statyczna biblioteka wiążąca liboop z GLib 2.x.

%package binding-readline
Summary:	liboop binding for readline library
Summary(pl.UTF-8):	Biblioteka wiążąca liboop z biblioteką readline
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description binding-readline
liboop binding for readline library.

%description binding-readline -l pl.UTF-8
Biblioteka wiążąca liboop z biblioteką readline.

%package binding-readline-devel
Summary:	Header file for liboop readline binding library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki wiążącej liboop z biblioteką readline
Group:		Development/Libraries
Requires:	%{name}-binding-readline = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	readline-devel

%description binding-readline-devel
liboop is a low-level event loop management library.

This package contains the header file needed to write or compile
programs that use liboop readline binding library.

%description binding-readline-devel -l pl.UTF-8
liboop jest biblioteką do zarządzania niskopoziomowymi pętlami.

Ten pakiet zawiera plik nagłówkowy potrzebny do kompilowania
programów używających biblioteki wiążącej liboop z readline.

%package binding-readline-static
Summary:	Static liboop readline binding library
Summary(pl.UTF-8):	Statyczna biblioteka wiążąca liboop z readline
Group:		Development/Libraries
Requires:	%{name}-binding-readline-devel = %{version}-%{release}

%description binding-readline-static
Static liboop readline binding library.

%description binding-readline-static -l pl.UTF-8
Statyczna biblioteka wiążąca liboop z readline.

%package binding-tcl
Summary:	liboop binding for tcl library
Summary(pl.UTF-8):	Biblioteka wiążąca liboop z biblioteką tcl
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description binding-tcl
liboop binding for tcl library.

%description binding-tcl -l pl.UTF-8
Biblioteka wiążąca liboop z biblioteką tcl.

%package binding-tcl-devel
Summary:	Header file for liboop tcl binding library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki wiążącej liboop z tcl
Group:		Development/Libraries
Requires:	%{name}-binding-tcl = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	tcl-devel

%description binding-tcl-devel
This package contains the header file needed to write or compile
programs that use liboop tcl binding library.

%description binding-tcl-devel -l pl.UTF-8
Ten pakiet zawiera plik nagłówkowy potrzebny do kompilowania programów
używających biblioteki wiążącej liboop z tcl.

%package binding-tcl-static
Summary:	Static liboop readline tcl library
Summary(pl.UTF-8):	Statyczna biblioteka wiążąca liboop z tcl
Group:		Development/Libraries
Requires:	%{name}-binding-tcl-devel = %{version}-%{release}

%description binding-tcl-static
Static liboop tcl binding library.

%description binding-tcl-static -l pl.UTF-8
Statyczna biblioteka wiążąca liboop z tcl.

%package binding-www
Summary:	liboop binding for w3c-libwww library
Summary(pl.UTF-8):	Biblioteka wiążąca liboop z biblioteką w3c-libwww
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description binding-www
liboop binding for w3c-libwww library.

%description binding-www -l pl.UTF-8
Biblioteka wiążąca liboop z biblioteką w3c-libwww.

%package binding-www-devel
Summary:	Header file for liboop w3c-libwww binding libraries
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki wiążącej liboop z w3c-libwww
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	w3c-libwww-devel

%description binding-www-devel
This package contains the header file needed to write or compile
programs that use liboop w3c-libwww binding library.

%description binding-www-devel -l pl.UTF-8
Ten pakiet zawiera plik nagłówkowy potrzebny do kompilowania programów
używających biblioteki wiążącej liboop z w3c-libwww.

%package binding-www-static
Summary:	Static liboop readline w3c-libwww library
Summary(pl.UTF-8):	Statyczna biblioteka wiążąca liboop z w3c-libwww
Group:		Development/Libraries
Requires:	%{name}-binding-tcl-devel = %{version}-%{release}

%description binding-www-static
Static liboop w3c-libwww binding library.

%description binding-www-static -l pl.UTF-8
Statyczna biblioteka wiążąca liboop z w3c-libwww.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	PROG_LDCONFIG=/bin/true \
	%{?with_libwww:--with-libwww}

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	binding-adns -p /sbin/ldconfig
%postun	binding-adns -p /sbin/ldconfig

%post	binding-glib -p /sbin/ldconfig
%postun	binding-glib -p /sbin/ldconfig

%post	binding-glib2 -p /sbin/ldconfig
%postun	binding-glib2 -p /sbin/ldconfig

%post	binding-readline -p /sbin/ldconfig
%postun	binding-readline -p /sbin/ldconfig

%post	binding-tcl -p /sbin/ldconfig
%postun	binding-tcl -p /sbin/ldconfig

%post	binding-www -p /sbin/ldconfig
%postun	binding-www -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboop.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop.so
%{_libdir}/liboop.la
%{_includedir}/oop.h
%{_includedir}/oop-read.h
%{_pkgconfigdir}/liboop.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liboop.a

%files binding-adns
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop-adns.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboop-adns.so.3

%files binding-adns-devel
%attr(755,root,root) %{_libdir}/liboop-adns.so
%{_libdir}/liboop-adns.la
%{_includedir}/oop-adns.h

%files binding-adns-static
%defattr(644,root,root,755)
%{_libdir}/liboop-adns.a

%files binding-glib-common-devel
%defattr(644,root,root,755)
%{_includedir}/oop-glib.h

%files binding-glib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop-glib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboop-glib.so.0

%files binding-glib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop-glib.so
%{_libdir}/liboop-glib.la

%files binding-glib-static
%defattr(644,root,root,755)
%{_libdir}/liboop-glib.a

%files binding-glib2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop-glib2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboop-glib2.so.0

%files binding-glib2-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop-glib2.so
%{_libdir}/liboop-glib2.la
%{_pkgconfigdir}/liboop-glib2.pc

%files binding-glib2-static
%defattr(644,root,root,755)
%{_libdir}/liboop-glib2.a

%files binding-readline
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop-rl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboop-rl.so.0

%files binding-readline-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop-rl.so
%{_libdir}/liboop-rl.la
%{_includedir}/oop-rl.h

%files binding-readline-static
%defattr(644,root,root,755)
%{_libdir}/liboop-rl.a

%files binding-tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop-tcl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboop-tcl.so.0

%files binding-tcl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop-tcl.so
%{_libdir}/liboop-tcl.la
%{_includedir}/oop-tcl.h

%files binding-tcl-static
%defattr(644,root,root,755)
%{_libdir}/liboop-tcl.a

%if %{with libwww}
%files binding-www
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop-www.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboop-www.so.0

%files binding-www-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop-www.so
%{_libdir}/liboop-www.la
%{_includedir}/oop-www.h

%files binding-www-static
%defattr(644,root,root,755)
%{_libdir}/liboop-www.a
%endif
