Summary:	Hades - MPEG-video player
Summary(pl):	Hades - odtwarzacz filmów MPEG
Name:		hades
Version:	0.1.0
Release:	1
License:	LGPL
Group:		X11/Applications/Multimedia
Source0:	ftp://lumumba.luc.ac.be/pub/linux_software/various/%{name}-%{version}.tar.gz
# Source0-md5:	950a1f52a6a56d1ea55e05339a026a17
URL:		http://lumumba.luc.ac.be/takis/hades/
Patch0:		%{name}-headers.patch
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gtk+-devel
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
	prefix=$RPM_BUILD_ROOT%{_prefix}

mv -f $RPM_BUILD_ROOT%{_datadir}/gnome/apps/Graphics/*.desktop \
      $RPM_BUILD_ROOT%{_desktopdir}
	
%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/*

#%%{_datadir}/oaf/*
#%config %{_sysconfdir}/CORBA/*
