%define module hxt

Name: haskell-%{module}
Version: 8.3.2
Release: %mkrel 2
Summary: XML haskell module 
Group: Development/Other
License: MIT
Url: https://www.fh-wedel.de/~si/HXmlToolbox/index.html
Source: http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: haskell-macros
BuildRequires: haskell(HTTP)
BuildRequires: haskell(curl) >= 1.3
BuildRequires: haskell(tagsoup) >= 0.6
BuildRequires: haddock
BuildRequires: ghc
Obsoletes: haskell-HXT < 8.3.2
Requires(preun): ghc
Requires(post): ghc

%description
An haskell module to parse and write XML files.

%prep
%setup -q -n %{module}-%{version}

%build
%define _cabal_setup Setup.lhs
%_cabal_build

%_cabal_genscripts

%check
%_cabal_check

%install
%_cabal_install

rm -rf %buildroot%{_datadir}/%{module}-%{version}/doc

%_cabal_rpm_gen_deps

%_cabal_scriptlets

%files
%defattr(-,root,root)
%_libdir/%{module}-%{version}
%{_docdir}/%{module}-%{version}
%_cabal_rpm_files

%clean
rm -fr %buildroot
