Summary:	Hades - MPEG-video player
Summary(pl):	Hades - odtwarzacz filmów MPEG
Name:		hades
Version:	0.1.0
Release:	1
License:	LGPL
Group:		X11/Applications/Multimedia
Source0:	http://lumumba.luc.ac.be/takis/hades/%{name}-%{version}.tar.gz
# Source0-md5:	fb99e94a26c6afa3b72b557aa07a8d09
Patch0:		%{name}-ac.patch
URL:		http://lumumba.luc.ac.be/takis/hades/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel >= 0.8.0
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libmpeg3-devel
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	sgml-tools
Requires:	gdk-pixbuf-devel >= 0.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hades: a video playing program.

%description -l pl
Hades - odtwarzacz filmów MPEG.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/gnome/apps/Graphics/*.desktop \
      $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
