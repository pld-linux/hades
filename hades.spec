#
# Note that this is NOT a relocatable package
# $Id: hades.spec,v 1.5 2001-07-26 04:39:38 agaran Exp $
#
Summary:	Hades 
Name:		hades
Version:	0.1.0
Release:	1
License:	LGPL
Group:		Applications
Group(de):	Applikationen
Group(pl):	Aplikacje
Source0:	ftp://lumumba.luc.ac.be/pub/takis/sources/%{name}-%{version}.tar.gz
Obsoletes:	hades
URL:		http://lumumba.luc.ac.be/takis/hades
Prereq:		/sbin/install-info
Requires:	gdk-pixbuf >= 0.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hades: a video playing program.

GNOME is the GNU Network Object Model Environment. That's a fancy name
but really GNOME is a nice GUI desktop environment. It makes using
your computer easy, powerful, and easy to configure.

%prep
%setup -q

%build
LC_ALL=""
LINGUAS=""
LANG=""
export LC_ALL LINGUAS LANG

# Needed for snapshot releases.
if [ ! -f configure ]; then
CFLAGS="%{rpmcflags}" ./autogen.sh --prefix=%prefix --sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir}
else
CFLAGS="%{rpmcflags}" ./configure --prefix=%prefix --sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir}
fi

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Graphics//*
%{_pixmapsdir}/*

#%{_datadir}/oaf/*
#%config %{_sysconfdir}/CORBA/*
