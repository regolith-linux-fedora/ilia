Name:           ilia
Version:        0.18.0
Release:        1%{?dist}
Summary:        General purpose desktop executor
License:        Apache-2.0
URL:            https://github.com/regolith-linux/ilia
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# The dependencies meson.build asks for. Debian's Build-Depends also list
# jsonrpc-glib, gettext and intltool, which this build doesn't use.
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  vala
# tinysparql-devel provides the tracker-sparql-3.0 .pc and .vapi as well
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
# --pkg GtkLayerShell-0.1 reads the GIR from gtk-layer-shell-devel
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(x11)
BuildRequires:  /usr/bin/glib-compile-schemas

%description
Invoke actions upon apps, commands, notifications, and keybindings via a
simple filterable menu.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
# meson_scripts/install_data.sh copies the CMakeLists.txt placeholders of
# data/local/ and doc/ into the package; nothing reads them.
rm %{buildroot}%{_datadir}/%{name}/CMakeLists.txt
rm %{buildroot}%{_docdir}/%{name}/CMakeLists.txt

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/glib-2.0/schemas/org.regolith-linux.ilia.gschema.xml

%changelog
* Thu Nov 05 2026 Regolith Fedora Port <port@regolith.invalid> - 0.18.0-1
- Initial package
