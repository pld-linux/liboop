Summary:	Libraries for low-level event loop management
Summary(pl):	Biblioteki do zarz±dzania niskopoziomowymi pêtlami
Name:		liboop
Version:	0.8
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://www.liboop.org/%{name}-%{version}.tar.gz
Patch0:		%{name}-libwww-fix.patch
URL:		http://www.liboop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	tcl-devel
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

%description -l pl
liboop jest bibliotek± do zarz±dzania niskopoziomowymi pêtlami w
systemach opartych na POSIX. Zawiera ona wsparcie umo¿liwiaj±ce rozwój
modularnych, zwielokrotnionych aplikacji, które mog± reagowaæ na
zdarzênia pochodz±ce z kilku ¼róde³. Zastêpuje ona "pêtlê select()" i
umo¿liwia rejestracjê funkcji obs³ugi zdarzeñ dla plikowego i
sieciowego we/wy, zegarów i sygna³ów. Ze wzglêdu na to, ¿e procesy
korzystaj± z tych mechanizmów przy praktycznie ka¿dej komunikacji z
otoczeniem, Since processes use these mechanisms for almost all
external communication, mo¿na u¿ywaæ liboop jako podstawy dla prawie
wszystkich aplikacji.

%package bindings
Summary:	liboop bindings for specific libraries
Summary(pl):	Biblioteki wi±¿±ce liboop z innymi bibliotekami
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description bindings
liboop bindings for specific libraries (dns, glib, readline).

%description bindings -l pl
Biblioteki wi±¿±ce liboop z innymi bibliotekami (dns, glib, readline).

%package binding-tcl
Summary:	liboop binding for tcl library
Summary(pl):	Biblioteka wi±¿±ca liboop z bibliotek± tcl
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description binding-tcl
liboop binding for tcl library.

%description binding-tcl -l pl
Biblioteka wi±¿±ca liboop z bibliotek± tcl.

%package binding-www
Summary:	liboop binding for w3c-libwww library
Summary(pl):	Biblioteka wi±¿±ca liboop z bibliotek± w3c-libwww
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description binding-www
liboop binding for w3c-libwww library.

%description binding-www -l pl
Biblioteka wi±¿±ca liboop z bibliotek± w3c-libwww.

%package devel
Summary:	Header files for liboop
Summary(pl):	Pliki nag³ówkowe liboop
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
liboop is a low-level event loop management library.

This package contains the header files and libraries needed to write
or compile programs that use liboop.

%description devel -l pl
liboop jest bibliotek± do zarz±dzania niskopoziomowymi pêtlami.

Ten pakiet zawiera pliki nag³ówkowe potrzebne do kompilowania
programów u¿ywaj±cych liboop.

%package bindings-devel
Summary:	Header files for liboop binding libraries
Summary(pl):	Pliki nag³ówkowe bibliotek wi±¿±cych liboop
Group:		Development/Libraries
Requires:	%{name}-bindings = %{version}
Requires:	%{name}-devel = %{version}

%description bindings-devel
liboop is a low-level event loop management library.

This package contains the header files and libraries needed to write
or compile programs that use liboop binding libraries.

%description bindings-devel -l pl
liboop jest bibliotek± do zarz±dzania niskopoziomowymi pêtlami.

Ten pakiet zawiera pliki nag³ówkowe potrzebne do kompilowania
programów u¿ywaj±cych bibliotek wi±¿±cych liboop.

%package binding-tcl-devel
Summary:	Header file for liboop tcl binding library
Summary(pl):	Plik nag³ówkowy biblioteki wi±¿±cej liboop z tcl
Group:		Development/Libraries
Requires:	%{name}-binding-tcl = %{version}
Requires:	%{name}-devel = %{version}
Requires:	tcl-devel

%description binding-tcl-devel
This package contains the header file needed to write or compile
programs that use liboop tcl binding library.

%description binding-tcl-devel -l pl
Ten pakiet zawiera plik nag³ówkowy potrzebny do kompilowania
programów u¿ywaj±cych biblioteki wi±¿±cej liboop z tcl.

%package binding-www-devel
Summary:	Header file for liboop w3c-libwww binding libraries
Summary(pl):	Plik nag³ówkowy biblioteki wi±¿±cej liboop z w3c-libwww
Group:		Development/Libraries
Requires:	%{name}-bindings = %{version}
Requires:	%{name}-devel = %{version}
Requires:	w3c-libwww-devel

%description binding-www-devel
This package contains the header file needed to write or compile
programs that use liboop w3c-libwww binding library.

%description binding-www-devel -l pl
Ten pakiet zawiera plik nag³ówkowy potrzebny do kompilowania
programów u¿ywaj±cych biblioteki wi±¿±cej liboop z w3c-libwww.

%package static
Summary:	Static liboop libraries
Summary(pl):	Statyczne biblioteki liboop
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Requires:	%{name}-bindings-devel = %{version}

%description static
Static liboop libraries.

%description static -l pl
Statyczne biblioteki liboop.

%prep
%setup -q
%patch -p1

%build
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_libdir}/liboop.la
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
%attr(755,root,root) %{_libdir}/liboop-adns.la
%attr(755,root,root) %{_libdir}/liboop-glib.so
%attr(755,root,root) %{_libdir}/liboop-glib.la
%attr(755,root,root) %{_libdir}/liboop-rl.so
%attr(755,root,root) %{_libdir}/liboop-rl.la
%{_includedir}/oop-adns.h
%{_includedir}/oop-glib.h
%{_includedir}/oop-rl.h

%files binding-tcl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop-tcl.so
%attr(755,root,root) %{_libdir}/liboop-tcl.la
%{_includedir}/oop-tcl.h

%files binding-www-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboop-www.so
%attr(755,root,root) %{_libdir}/liboop-www.la
%{_includedir}/oop-www.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
