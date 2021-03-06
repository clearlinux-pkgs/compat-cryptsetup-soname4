#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : compat-cryptsetup-soname4
Version  : 1.7.5
Release  : 37
URL      : https://www.kernel.org/pub/linux/utils/cryptsetup/v1.7/cryptsetup-1.7.5.tar.xz
Source0  : https://www.kernel.org/pub/linux/utils/cryptsetup/v1.7/cryptsetup-1.7.5.tar.xz
Summary  : cryptsetup library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: compat-cryptsetup-soname4-lib = %{version}-%{release}
Requires: compat-cryptsetup-soname4-license = %{version}-%{release}
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : pkgconfig(devmapper)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(pwquality)
BuildRequires : popt-dev
BuildRequires : python3-dev
# Suppress generation of debuginfo
%global debug_package %{nil}
Patch1: 0001-pycryptsetup-test.py-change-python-interpreter.patch

%description
cryptsetup
setup cryptographic volumes for dm-crypt (including LUKS extension)
WEB PAGE:

%package lib
Summary: lib components for the compat-cryptsetup-soname4 package.
Group: Libraries
Requires: compat-cryptsetup-soname4-license = %{version}-%{release}

%description lib
lib components for the compat-cryptsetup-soname4 package.


%package license
Summary: license components for the compat-cryptsetup-soname4 package.
Group: Default

%description license
license components for the compat-cryptsetup-soname4 package.


%prep
%setup -q -n cryptsetup-1.7.5
cd %{_builddir}/cryptsetup-1.7.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576092129
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure  --enable-python --with-python_version=3 --enable-static --disable-nls
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1576092129
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-cryptsetup-soname4
cp %{_builddir}/cryptsetup-1.7.5/COPYING %{buildroot}/usr/share/package-licenses/compat-cryptsetup-soname4/c0d79c59a1dae23cf8331a810a5df9f5ab6a709d
cp %{_builddir}/cryptsetup-1.7.5/COPYING.LGPL %{buildroot}/usr/share/package-licenses/compat-cryptsetup-soname4/6ce6cfc2dfacf60e153e5f61c4c8accc999d322d
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/bin/cryptsetup
rm -f %{buildroot}/usr/bin/veritysetup
rm -f %{buildroot}/usr/include/libcryptsetup.h
rm -f %{buildroot}/usr/lib/python3.8/site-packages/pycryptsetup.so
rm -f %{buildroot}/usr/lib64/libcryptsetup.a
rm -f %{buildroot}/usr/lib64/libcryptsetup.so
rm -f %{buildroot}/usr/lib64/pkgconfig/libcryptsetup.pc
rm -f %{buildroot}/usr/share/man/man8/cryptsetup.8
rm -f %{buildroot}/usr/share/man/man8/veritysetup.8

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcryptsetup.so.4
/usr/lib64/libcryptsetup.so.4.7.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-cryptsetup-soname4/6ce6cfc2dfacf60e153e5f61c4c8accc999d322d
/usr/share/package-licenses/compat-cryptsetup-soname4/c0d79c59a1dae23cf8331a810a5df9f5ab6a709d
