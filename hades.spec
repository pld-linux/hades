#
# Note that this is NOT a relocatable package
# $Id: hades.spec,v 1.3 2001-02-02 17:50:34 kloczek Exp $
#
%define prefix   /usr

Summary:	Hades 
Name:		hades
Version:	0.1.0
Release:	1
License:	LGPL
Group:		System Environment/Base
######		Unknown group!
Source0:	ftp://lumumba.luc.ac.be/pub/takis/sources/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	hades
URL:		http://lumumba.luc.ac.be/takis/hades
Prereq:		/sbin/install-info
Requires:	gdk-pixbuf >= 0.8.0

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
CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=%prefix --sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir}
else
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix --sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir}
fi

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Graphics//*
%{_pixmapsdir}/*
#%{_datadir}/oaf/*
#%config %{_sysconfdir}/CORBA/*
