Summary:	Libraries for low-level event loop management
Summary(pl.UTF-8):	Biblioteki do zarządzania niskopoziomowymi pętlami
Name:		liboop
Version:	0.8
Release:	9
License:	LGPL
Group:		Libraries
Source0:	http://www.liboop.org/%{name}-%{version}.tar.gz
# Source0-md5:	903f8d2f9b94e7b0ac73be61d6a5442f
Patch0:		%{name}-libwww-fix.patch
Patch1:		%{name}-nolibs.patch
URL:		http://www.liboop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	glib-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	tcl-devel >= 8.3.4-10
BuildRequires:	w3c-libwww-devel
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

%package bindings
Summary:	liboop bindings for specific libraries
Summary(pl.UTF-8):	Biblioteki wiążące liboop z innymi bibliotekami
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description bindings
liboop bindings for specific libraries (dns, glib, readline).

%description bindings -l pl.UTF-8
Biblioteki wiążące liboop z innymi bibliotekami (dns, glib, readline).

%package binding-tcl
Summary:	liboop binding for tcl library
Summary(pl.UTF-8):	Biblioteka wiążąca liboop z biblioteką tcl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description binding-tcl
liboop binding for tcl library.

%description binding-tcl -l pl.UTF-8
Biblioteka wiążąca liboop z biblioteką tcl.

%package binding-www
Summary:	liboop binding for w3c-libwww library
Summary(pl.UTF-8):	Biblioteka wiążąca liboop z biblioteką w3c-libwww
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description binding-www
liboop binding for w3c-libwww library.

%description binding-www -l pl.UTF-8
Biblioteka wiążąca liboop z biblioteką w3c-libwww.

%package devel
Summary:	Header files for liboop
Summary(pl.UTF-8):	Pliki nagłówkowe liboop
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
liboop is a low-level event loop management library.

This package contains the header files and libraries needed to write
or compile programs that use liboop.

%description devel -l pl.UTF-8
liboop jest biblioteką do zarządzania niskopoziomowymi pętlami.

Ten pakiet zawiera pliki nagłówkowe potrzebne do kompilowania
programów używających liboop.

%package bindings-devel
Summary:	Header files for liboop binding libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek wiążących liboop
Group:		Development/Libraries
Requires:	%{name}-bindings = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description bindings-devel
liboop is a low-level event loop management library.

This package contains the header files and libraries needed to write
or compile programs that use liboop binding libraries.

%description bindings-devel -l pl.UTF-8
liboop jest biblioteką do zarządzania niskopoziomowymi pętlami.

Ten pakiet zawiera pliki nagłówkowe potrzebne do kompilowania
programów używających bibliotek wiążących liboop.

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

%package binding-www-devel
Summary:	Header file for liboop w3c-libwww binding libraries
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki wiążącej liboop z w3c-libwww
Group:		Development/Libraries
Requires:	%{name}-bindings = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	w3c-libwww-devel

%description binding-www-devel
This package contains the header file needed to write or compile
programs that use liboop w3c-libwww binding library.

%description binding-www-devel -l pl.UTF-8
Ten pakiet zawiera plik nagłówkowy potrzebny do kompilowania programów
używających biblioteki wiążącej liboop z w3c-libwww.

%package static
Summary:	Static liboop libraries
Summary(pl.UTF-8):	Statyczne biblioteki liboop
Group:		Development/Libraries
Requires:	%{name}-bindings-devel = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liboop libraries.

%description static -l pl.UTF-8
Statyczne biblioteki liboop.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	bindings -p /sbin/ldconfig
%postun	bindings -p /sbin/ldconfig

%post	binding-tcl -p /sbin/ldconfig
%postun	binding-tcl -p /sbin/ldconfig

%post	binding-www -p /sbin/ldconfig
%postun	binding-www -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop.so
%{_libdir}/liboop.la
%{_includedir}/oop.h
%{_includedir}/oop-read.h

%files bindings
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop-adns.so.*.*
%attr(755,root,root) %{_libdir}/liboop-glib.so.*.*
%attr(755,root,root) %{_libdir}/liboop-rl.so.*.*

%files binding-tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop-tcl.so.*.*

%files binding-www
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop-www.so.*.*

%files bindings-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop-adns.so
%{_libdir}/liboop-adns.la
%attr(755,root,root) %{_libdir}/liboop-glib.so
%{_libdir}/liboop-glib.la
%attr(755,root,root) %{_libdir}/liboop-rl.so
%{_libdir}/liboop-rl.la
%{_includedir}/oop-adns.h
%{_includedir}/oop-glib.h
%{_includedir}/oop-rl.h

%files binding-tcl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop-tcl.so
%{_libdir}/liboop-tcl.la
%{_includedir}/oop-tcl.h

%files binding-www-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop-www.so
%{_libdir}/liboop-www.la
%{_includedir}/oop-www.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
