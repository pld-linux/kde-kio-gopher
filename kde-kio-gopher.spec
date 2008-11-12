Summary:	Gopher support for KDE
Summary(pl.UTF-8):	Obsługa protokołu gopher dla KDE
Name:		kde-kio-gopher
Version:	20040214
Release:	4
License:	GPL
Group:		Applications
Source0:	http://download.berlios.de/kgopher/kio_gopher-%{version}.tar.bz2
# Source0-md5:	3e0ce7b35f48a8f7af64cd8789a332b2
Patch0:		%{name}-admin.patch
Patch1:		%{name}-am.patch
Patch2:		kde-ac260.patch
Patch3:		kde-ac260-lt.patch
URL:		http://kgopher.berlios.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gopher support for KDE.

%description -l pl.UTF-8
Obsługa protokołu gopher dla KDE.

%prep
%setup -q -n kio_gopher-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

rm -rf po/xx

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},%{_datadir}/services}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

%find_lang kio_gopher --with-kde
mv $RPM_BUILD_ROOT{%{_desktopdir},%{_datadir}/services}/gopher.protocol
rm -f $RPM_BUILD_ROOT%{_libdir}/kde3/kio_gopher.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kio_gopher.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/kio_gopher.so
%{_datadir}/services/gopher.protocol
