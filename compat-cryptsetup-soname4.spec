#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : compat-cryptsetup-soname4
Version  : 1.7.5
Release  : 23
URL      : https://www.kernel.org/pub/linux/utils/cryptsetup/v1.7/cryptsetup-1.7.5.tar.xz
Source0  : https://www.kernel.org/pub/linux/utils/cryptsetup/v1.7/cryptsetup-1.7.5.tar.xz
Summary  : cryptsetup library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: compat-cryptsetup-soname4-bin
Requires: compat-cryptsetup-soname4-python3
Requires: compat-cryptsetup-soname4-lib
Requires: compat-cryptsetup-soname4-man
Requires: compat-cryptsetup-soname4-python
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : pkgconfig(devmapper)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(pwquality)
BuildRequires : popt-dev
BuildRequires : python3-dev
Patch1: 0001-pycryptsetup-test.py-change-python-interpreter.patch

%description
cryptsetup
setup cryptographic volumes for dm-crypt (including LUKS extension)
WEB PAGE:

%package bin
Summary: bin components for the compat-cryptsetup-soname4 package.
Group: Binaries
Requires: compat-cryptsetup-soname4-man

%description bin
bin components for the compat-cryptsetup-soname4 package.


%package dev
Summary: dev components for the compat-cryptsetup-soname4 package.
Group: Development
Requires: compat-cryptsetup-soname4-lib
Requires: compat-cryptsetup-soname4-bin
Provides: compat-cryptsetup-soname4-devel

%description dev
dev components for the compat-cryptsetup-soname4 package.


%package lib
Summary: lib components for the compat-cryptsetup-soname4 package.
Group: Libraries

%description lib
lib components for the compat-cryptsetup-soname4 package.


%package man
Summary: man components for the compat-cryptsetup-soname4 package.
Group: Default

%description man
man components for the compat-cryptsetup-soname4 package.


%package python
Summary: python components for the compat-cryptsetup-soname4 package.
Group: Default
Requires: compat-cryptsetup-soname4-python3

%description python
python components for the compat-cryptsetup-soname4 package.


%package python3
Summary: python3 components for the compat-cryptsetup-soname4 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the compat-cryptsetup-soname4 package.


%prep
%setup -q -n cryptsetup-1.7.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526396381
%configure  --enable-python --with-python_version=3 --enable-static --disable-nls
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1526396381
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/cryptsetup
%exclude /usr/bin/veritysetup

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/libcryptsetup.h
%exclude /usr/lib64/libcryptsetup.a
%exclude /usr/lib64/libcryptsetup.so
%exclude /usr/lib64/pkgconfig/libcryptsetup.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcryptsetup.so.4
/usr/lib64/libcryptsetup.so.4.7.0

%files man
%defattr(-,root,root,-)
%exclude /usr/share/man/man8/cryptsetup.8
%exclude /usr/share/man/man8/veritysetup.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
%exclude /usr/lib/python3.6/site-packages/pycryptsetup.so
