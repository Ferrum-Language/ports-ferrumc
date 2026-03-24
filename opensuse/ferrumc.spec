Name:           ferrumc
Version:        0.3.0
Release:        1
Summary:        Ferrum-language compiler with compile-time memory safety
License:        GPL-3.0-only
URL:            https://ferrum-language.github.io/Ferrum/
Source0:        https://github.com/Ferrum-Language/Ferrum/releases/download/v%{version}/ferrumc-v%{version}-linux-x86_64.tar.gz

ExclusiveArch:  x86_64 aarch64

%description
Ferrum-language is a systems programming language with C syntax and
compile-time memory safety via a borrow checker and ownership model,
compiled to native code through LLVM 18.

%prep
%setup -q -c

%install
install -Dm755 ferrumc %{buildroot}%{_bindir}/ferrumc

%files
%{_bindir}/ferrumc

%changelog
