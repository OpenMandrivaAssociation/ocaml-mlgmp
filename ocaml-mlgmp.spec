Name:           ocaml-mlgmp
Version:        0.13
Release:        3
Summary:        OCaml bindings for the GNU multiprecision arithmetic library
License:        LGPL + linking exception
Group:          Development/Other
URL:            http://www-verimag.imag.fr/~monniaux/programmes.html.en
Source0:        http://www-verimag.imag.fr/~monniaux/download/mlgmp.tar.gz
Source1:        META.in
Patch0:         10_config.dpatch
#Patch1:         11_Makefile.dpatch
Patch1:         Makefile.patch
Patch2:         15_bugfixes.dpatch
BuildRequires:  ocaml
BuildRequires:  gmp-devel
BuildRequires:  ncurses-devel

%description
This package provides bindings for the GNU multiprecision library 
(GNU MP) for the language OCaml (caml.inria.fr).
It is mostly a 1-1 mapping of the C functions into the OCaml namespace,
but also includes some infix operators to make for a cleaner syntax.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n mlgmp
%patch0 -p 1
%patch1 -p 1
%patch2 -p 1
sed -e 's/@VERSION@/%{version}/' < %{SOURCE1} > META

%build
make GMP_INCLUDES=-I/usr/include GMP_LIBDIR=/usr/lib
mkdir html
ocamldoc -colorize-code -html gmp.mli -d html

%install
install -d %{buildroot}/`ocamlc -where`/gmp/
install -m 0644 -c gmp.{cmi,mli,cma,cmxa} *.a \
           %{buildroot}/`ocamlc -where`/gmp/
install -d %{buildroot}/`ocamlc -where`/stublibs
install -m 0755 -c *.so %{buildroot}/`ocamlc -where`/stublibs
install -m 0644 META %{buildroot}/`ocamlc -where`/gmp/

%files
%defattr(-,root,root)
%doc ChangeLog README benchmarks.txt
%dir %{_libdir}/ocaml/gmp
%{_libdir}/ocaml/gmp/META
%{_libdir}/ocaml/gmp/*.cma
%{_libdir}/ocaml/gmp/*.cmi
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%doc html
%{_libdir}/ocaml/gmp/*.a
%{_libdir}/ocaml/gmp/*.cmxa
%{_libdir}/ocaml/gmp/*.mli


%changelog
* Fri Aug 20 2010 Florent Monnier <blue_prawn@mandriva.org> 0.13-1mdv2011.0
+ Revision: 571523
- BuildRequires: ncurses-devel
- import ocaml-mlgmp

