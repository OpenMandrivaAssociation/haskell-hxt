%define module HXT
%define mdirname hxt

Name: haskell-%{module}
Version: 7.1
Release: %mkrel 5
Summary: XML haskell module 
Group: Development/Other
License: MIT
Url: http://www.fh-wedel.de/~si/HXmlToolbox/index.html
Source: http://www.fh-wedel.de/~si/HXmlToolbox/%{module}-%{version}.tar.bz2
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: haskell-HTTP
BuildRequires: haddock
BuildRequires: ghc
Requires(preun): ghc
Requires(post): ghc

%description
An haskell module to parse and write XML files.

%prep
%setup -q -n %{module}-%{version}

%build
runhaskell Setup.lhs configure --prefix=%{_prefix}
runhaskell Setup.lhs build
runhaskell Setup.lhs haddock

%check
runhaskell Setup.lhs test

%install
runhaskell Setup.lhs copy --destdir=%{buildroot}

mkdir -p %buildroot%_libdir/%{mdirname}-%{version}
install -m 755 .installed-pkg-config %buildroot%_libdir/%{mdirname}-%{version}/installed-pkg-config

%post
ghc-pkg update %_libdir/%{mdirname}-%{version}/installed-pkg-config

%preun
ghc-pkg unregister hxt

%files
%defattr(-,root,root)
%doc dist/doc/html
%doc README
%_libdir/%{mdirname}-%{version}
%_datadir/%mdirname-%version/

%clean
rm -fr %buildroot



