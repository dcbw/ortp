Name:           ortp
Version:        5.4.21
Release:        1.dcbw%{?dist}
Summary:        A C library implementing the RTP protocol (RFC3550)
License:        AGPLv3

URL:            http://www.linphone.org/eng/documentation/dev/ortp.html

BuildRequires:  git gcc-c++ cmake doxygen graphviz libtool
BuildRequires:  libsrtp-devel openssl-devel bctoolbox-devel

Source0: %{name}-%{version}.tar.gz

%description
oRTP is a C library that implements RTP (RFC3550).

%package        devel
Summary:        Development libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       bctoolbox-devel


%description    devel
Libraries and headers required to develop software with %{name}.


%prep
%autosetup -p1
# epel
sed -i 's|cmake_minimum_required(VERSION.*|cmake_minimum_required(VERSION 3.20)|g' CMakeLists.txt


%build
sed -i 's|WARN_AS_ERROR.*=.*YES|WARN_AS_ERROR = NO|' ortp.doxygen.in
%global optflags %(echo %optflags | sed 's|-Wp,-D_GLIBCXX_ASSERTIONS||g')
%cmake -Wno-dev \
       -DCMAKE_SKIP_RPATH=ON \
       -DCMAKE_VERBOSE_MAKEFILE=OFF \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DENABLE_SHARED=ON \
       -DENABLE_STATIC=OFF \
       -DENABLE_TESTS=OFF \
       -DENABLE_STRICT=NO \
       -DENABLE_UNIT_TESTS=OFF
%cmake_build


%install
%cmake_install
rm -rf %{buildroot}/%{_datadir}/doc


%ldconfig_scriptlets


%files
%doc README.md
%doc AUTHORS.md
%doc CHANGELOG.md
%license LICENSE.txt
%{_libdir}/libortp.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/libortp.so
%{_libdir}/pkgconfig/ortp.pc
%{_datadir}/Ortp/*


%changelog
* Sun Jun  8 2025 Dan Williams <dan@ioncontrol.co>
- Update to 5.4.21

* Mon Apr 11 2022 Cristian Balint <cristian.balint@gmail.com>
- github upstream releases

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.23.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild
