Summary:	Hades - MPEG-video player
Summary(pl):	Hades - odtwarzacz filmów MPEG
Name:		hades
Version:	0.1.0
Release:	1
License:	LGPL
Group:		X11/Applications/Multimedia
Source0:	http://lumumba.luc.ac.be/takis/hades/%{name}-%{version}.tar.gz
# Source0-md5:	fb99e94a26c6afa3b72b557aa07a8d09
URL:		http://lumumba.luc.ac.be/takis/hades/
Patch0:		%{name}-headers.patch
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gtk+-devel
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
LC_ALL=""
LINGUAS=""
LANG=""
export LC_ALL LINGUAS LANG
# Needed for snapshot releases.
if [ ! -f configure ]; then
CFLAGS="%{rpmcflags}" ./autogen.sh --prefix=%{_prefix} --sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir}
else
CFLAGS="%{rpmcflags}" ./configure --prefix=%{_prefix} --sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir}
fi

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
%{_desktopdir}/*
%{_pixmapsdir}/*

#%%{_datadir}/oaf/*
#%config %{_sysconfdir}/CORBA/*
