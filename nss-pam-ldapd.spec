#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
#
Name     : nss-pam-ldapd
Version  : 0.9.12
Release  : 13
URL      : https://github.com/arthurdejong/nss-pam-ldapd/archive/0.9.12/nss-pam-ldapd-0.9.12.tar.gz
Source0  : https://github.com/arthurdejong/nss-pam-ldapd/archive/0.9.12/nss-pam-ldapd-0.9.12.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: nss-pam-ldapd-bin = %{version}-%{release}
Requires: nss-pam-ldapd-data = %{version}-%{release}
Requires: nss-pam-ldapd-lib = %{version}-%{release}
Requires: nss-pam-ldapd-license = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : cyrus-sasl-dev
BuildRequires : krb5-dev
BuildRequires : openldap-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
nss-pam-ldapd - NSS and PAM libraries for name lookups and authentication
using LDAP

%package bin
Summary: bin components for the nss-pam-ldapd package.
Group: Binaries
Requires: nss-pam-ldapd-data = %{version}-%{release}
Requires: nss-pam-ldapd-license = %{version}-%{release}

%description bin
bin components for the nss-pam-ldapd package.


%package data
Summary: data components for the nss-pam-ldapd package.
Group: Data

%description data
data components for the nss-pam-ldapd package.


%package lib
Summary: lib components for the nss-pam-ldapd package.
Group: Libraries
Requires: nss-pam-ldapd-data = %{version}-%{release}
Requires: nss-pam-ldapd-license = %{version}-%{release}

%description lib
lib components for the nss-pam-ldapd package.


%package license
Summary: license components for the nss-pam-ldapd package.
Group: Default

%description license
license components for the nss-pam-ldapd package.


%prep
%setup -q -n nss-pam-ldapd-0.9.12
cd %{_builddir}/nss-pam-ldapd-0.9.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688580336
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%autogen --disable-static --with-pam-seclib-dir=/usr/lib/security
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1688580336
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nss-pam-ldapd
cp %{_builddir}/nss-pam-ldapd-%{version}/COPYING %{buildroot}/usr/share/package-licenses/nss-pam-ldapd/caeb68c46fa36651acf592771d09de7937926bb3 || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/chsh.ldap
/usr/bin/getent.ldap
/usr/bin/nslcd

%files data
%defattr(-,root,root,-)
/usr/share/nslcd-utils/chsh.py
/usr/share/nslcd-utils/cmdline.py
/usr/share/nslcd-utils/constants.py
/usr/share/nslcd-utils/getent.py
/usr/share/nslcd-utils/nslcd.py
/usr/share/nslcd-utils/shells.py
/usr/share/nslcd-utils/users.py

%files lib
%defattr(-,root,root,-)
/usr/lib/security/pam_ldap.so
/usr/lib64/libnss_ldap.so.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nss-pam-ldapd/caeb68c46fa36651acf592771d09de7937926bb3
