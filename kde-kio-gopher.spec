%define		_name	gopher
Summary:	Gopher support for KDE
Summary(pl):	Obs³uga protoko³u gopher dla KDE
Name:		kde-kio-%{_name}
Version:	20040214
Release:	1
License:	GPL
Group:		Applications
Source0:	http://download.berlios.de/kgopher/kio_%{_name}-%{version}.tar.bz2
# Source0-md5:	3e0ce7b35f48a8f7af64cd8789a332b2
Patch0:		kde-common-PLD.patch
URL:		http://kgopher.berlios.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
#BuildRequires:	unsermake >= 040805
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gopher support for KDE.

%description -l pl
Obs³uga protoko³u gopher dla KDE.

%prep
%setup -q -n kio_%{_name}-%{version}
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
#export PATH=/usr/share/unsermake:$PATH
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
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/apps/%{name}.png
%{_datadir}/mimelnk/application/*
%{_datadir}/apps/%{name}
