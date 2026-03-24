Name:           ferrumc
Version:        0.3.0
Release:        1%{?dist}
Summary:        Ferrum-language compiler with compile-time memory safety

License:        GPL-3.0-only
URL:            https://ferrum-language.github.io/Ferrum/
Source0:        https://github.com/Ferrum-Language/Ferrum/releases/download/v%{version}/ferrumc-v%{version}-linux-x86_64.tar.gz

ExclusiveArch:  x86_64 aarch64

%description
Ferrum-language is a systems programming language with C syntax and
compile-time memory safety via a borrow checker and ownership model,
compiled to native code through LLVM 18.

Features:
- Ownership and move semantics
- Immutable and mutable borrows enforced at compile time
- Opt-in unsafe blocks for raw pointer arithmetic and FFI
- C interoperability via #include
- Zero runtime overhead — no garbage collector

%prep
%setup -q -c

%install
install -Dm755 ferrumc %{buildroot}%{_bindir}/ferrumc

%files
%{_bindir}/ferrumc

%changelog
* Mon Mar 24 2026 Ferrum-Language <noreply@ferrum-lang.org> - 0.3.0-1
- Initial package
