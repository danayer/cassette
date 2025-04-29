%define xdg_name space.rirusha.Cassette

Name: cassette
Version: 0.2.1
Release: 1%{?dist}

Summary: GTK/Adwaita application that allows you to use Yandex Music service on Linux operating systems
License: GPL-3.0
Group: Applications/Multimedia
URL: https://gitlab.gnome.org/Rirusha/Cassette

Source0: https://gitlab.gnome.org/Rirusha/Cassette/-/archive/v%{version}/Cassette-v%{version}.tar.gz

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: gtk4-devel
BuildRequires: libadwaita-devel
BuildRequires: json-glib-devel
BuildRequires: sqlite-devel
BuildRequires: libgee-devel
BuildRequires: libxml2-devel
BuildRequires: gstreamer1-devel
BuildRequires: webkit2gtk4.1-devel

%description
%{summary}.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/cassette
%{_datadir}/glib-2.0/schemas/%{xdg_name}.gschema.xml
%{_datadir}/metainfo/%{xdg_name}.metainfo.xml
%{_datadir}/applications/%{xdg_name}.desktop
%{_datadir}/icons/hicolor/*/apps/*.svg

%changelog
* Tue Mar 04 2025 Alexey Volkov <qualimock@altlinux.org> - 0.2.1-1
- Update to version 0.2.1

* Fri Oct 4 2024 Alexey Volkov <qualimock@altlinux.org> - 0.2.0-2
- Change upstream sources to the current

* Thu Jul 11 2024 Alexey Volkov <qualimock@altlinux.org> - 0.2.0-1
- Update to version 0.2.0

* Sun Jan 28 2024 Alexey Volkov <qualimock@altlinux.org> - 0.1.4-1
- Update to version 0.1.4

* Wed Jan 3 2024 Alexey Volkov <qualimock@altlinux.org> - 0.1.1-1
- Initial build for Fedora
