#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v18
# autospec commit: eaa4f71
#
# Source0 file verified with key 0x50FE47277DC196FB (thurston@cs.queensu.ca)
#
Name     : ragel
Version  : 7.0.4
Release  : 8
URL      : https://www.colm.net/files/ragel/ragel-7.0.4.tar.gz
Source0  : https://www.colm.net/files/ragel/ragel-7.0.4.tar.gz
Source1  : https://www.colm.net/files/ragel/ragel-7.0.4.tar.gz.asc
Source2  : 50FE47277DC196FB.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: ragel-bin = %{version}-%{release}
Requires: ragel-data = %{version}-%{release}
Requires: ragel-lib = %{version}-%{release}
Requires: ragel-license = %{version}-%{release}
Requires: ragel-man = %{version}-%{release}
BuildRequires : asciidoc
BuildRequires : buildreq-configure
BuildRequires : colm
BuildRequires : colm-dev
BuildRequires : file
BuildRequires : gnupg
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: backport-ac-fix.patch
Patch2: backport-ensure-data-match.patch

%description
Colm.Net Suite of Programs
==========================
This package contains the Colm Programming Language, Ragel State Machine
Compiler 7.0+, and supporting libraries.

%package bin
Summary: bin components for the ragel package.
Group: Binaries
Requires: ragel-data = %{version}-%{release}
Requires: ragel-license = %{version}-%{release}

%description bin
bin components for the ragel package.


%package data
Summary: data components for the ragel package.
Group: Data

%description data
data components for the ragel package.


%package dev
Summary: dev components for the ragel package.
Group: Development
Requires: ragel-lib = %{version}-%{release}
Requires: ragel-bin = %{version}-%{release}
Requires: ragel-data = %{version}-%{release}
Provides: ragel-devel = %{version}-%{release}
Requires: ragel = %{version}-%{release}

%description dev
dev components for the ragel package.


%package doc
Summary: doc components for the ragel package.
Group: Documentation
Requires: ragel-man = %{version}-%{release}

%description doc
doc components for the ragel package.


%package lib
Summary: lib components for the ragel package.
Group: Libraries
Requires: ragel-data = %{version}-%{release}
Requires: ragel-license = %{version}-%{release}

%description lib
lib components for the ragel package.


%package license
Summary: license components for the ragel package.
Group: Default

%description license
license components for the ragel package.


%package man
Summary: man components for the ragel package.
Group: Default

%description man
man components for the ragel package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 50FE47277DC196FB' gpg.status
%setup -q -n ragel-7.0.4
cd %{_builddir}/ragel-7.0.4
%patch -P 1 -p1
%patch -P 2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1725906093
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%reconfigure --disable-static --with-colm=/usr/ \
--disable-manual
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1725906093
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ragel
cp %{_builddir}/ragel-%{version}/COPYING %{buildroot}/usr/share/package-licenses/ragel/18d0c1c269850a9f7731a4546df6b6e77bef0bfe || :
export GOAMD64=v2
GOAMD64=v2
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ragel
/usr/bin/ragel-asm
/usr/bin/ragel-c
/usr/bin/ragel-crack
/usr/bin/ragel-csharp
/usr/bin/ragel-d
/usr/bin/ragel-go
/usr/bin/ragel-java
/usr/bin/ragel-js
/usr/bin/ragel-julia
/usr/bin/ragel-ocaml
/usr/bin/ragel-ruby
/usr/bin/ragel-rust

%files data
%defattr(-,root,root,-)
/usr/share/out-go.lm
/usr/share/ragel.lm

%files dev
%defattr(-,root,root,-)
/usr/lib64/libragel.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/ragel/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libragel.so.0
/usr/lib64/libragel.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ragel/18d0c1c269850a9f7731a4546df6b6e77bef0bfe

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ragel.1
