#
Summary:	Spatial GNOME editor
Name:		scratchpad
Version:	0.3.0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.chorse.org/stuff/scratchpad/%{name}-%{version}.tar.bz2
# Source0-md5:	12ec467f5670150a79964c00f593157c
URL:		http://dborg.wordpress.com/scratchpad/
BuildRequires:	libgnomeui-devel >= 2.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

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
%{_sysconfdir}/gconf/schemas/scratchpad.schemas
%attr(755,root,root) %{_bindir}/scratchpad
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_datadir}/%{name}
