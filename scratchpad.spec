Summary:	Spatial GNOME editor
Summary(pl.UTF-8):	Przestrzenny edytor dla GNOME
Name:		scratchpad
Version:	0.3.0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.chorse.org/stuff/scratchpad/%{name}-%{version}.tar.bz2
# Source0-md5:	12ec467f5670150a79964c00f593157c
URL:		http://dborg.wordpress.com/scratchpad/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	dbus-glib-devel >= 0.33
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gnome-vfs2-devel >= 2.16.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	gtksourceview-devel >= 1.8.0
BuildRequires:	libgnomeui-devel >= 2.16.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spatial GNOME editor.

%description -l pl.UTF-8
Przestrzenny edytor dla GNOME.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/scratchpad
%{_datadir}/%{name}
%{_sysconfdir}/gconf/schemas/scratchpad.schemas
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
