Summary:	Libraries for low-level event loop management
Summary(pl):	Biblioteki do zarz±dzania niskopoziomowymi pêtlami
Name:		liboop
Version:	0.8
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.liboop.org/%{name}-%{version}.tar.gz
URL:		http://www.liboop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	readline-devel
BuildRequires:	tcl-devel
BuildRequires:	ncurses-devel
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
wszystkich aplikacji

%package devel
Summary:	Header files for liboop
Summary(pl):	Pliki nag³ówkowe liboop
Group:		Development/Libraries
Requires:	%{name} >= %{version}
#Requires:	glib-devel

%description devel
liboop is a low-level event loop management library.

This package contains the header files and libraries needed to write
or compile programs that use liboop.

%description devel -l pl
liboop jest bibliotek± do zarz±dzania niskopoziomowymi pêtlami.

Ten pakiet zawiera pliki nag³ówkowe potrzebne do kompilowania
programów u¿ywaj±cych liboop.

%package static
Summary:	Static liboop libraries
Summary(pl):	Statyczne biblioteki liboop
Group:		Development/Libraries
Requires:	%{name}-devel >= %{version}

%description static
Static liboop libraries.

%description static -l pl
Statyczne biblioteki liboop.

%prep
%setup -q

%build
rm -f missing
libtoolize --copy --force
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

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
