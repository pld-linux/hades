#
# Note that this is NOT a relocatable package
# $Id: hades.spec,v 1.1 2000-11-07 20:05:30 kloczek Exp $
#
%define ver      0.1.0
%define rel      1
%define prefix   /usr
%define name	 hades

Summary: Hades 
Name: %name
Version: %ver
Release: %rel
Copyright: LGPL
Group: System Environment/Base
Source: ftp://lumumba.luc.ac.be/pub/takis/sources/hades-%{ver}.tar.gz
BuildRoot: /var/tmp/hades
Obsoletes: hades
Packager: Panagiotis Issaris <takis@beta.luc.ac.be>
URL: http://lumumba.luc.ac.be/takis/hades
Prereq: /sbin/install-info
Prefix: %{prefix}
Docdir: %{prefix}/doc
Requires: gdk-pixbuf >= 0.8.0

%description
Hades: a video playing program.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%changelog

* Wed Oct 4 2000  Panagiotis Issaris <takis@lumumba.luc.ac.be>

- Created the .spec file

%prep
%setup

%build
LC_ALL=""
LINGUAS=""
LANG=""
export LC_ALL LINGUAS LANG

# Needed for snapshot releases.
if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=%prefix --sysconfdir=$RPM_BUILD_ROOT/etc
else
  CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix --sysconfdir=$RPM_BUILD_ROOT/etc
fi

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{prefix}/bin/*
%{prefix}/share/gnome/apps/Graphics//*
%{prefix}/share/pixmaps/*
#%{prefix}/share/oaf/*
#%config /etc/CORBA/*
