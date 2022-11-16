Name:		texlive-latexcheat-de
Version:	35702
Release:	1
Summary:	A LaTeX cheat sheet, in German
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/latexcheat-de
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat-de.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat-de.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a translation to German of Winston Chang's LaTeX cheat
sheet (a reference sheet for writing scientific papers). It has
been adapted to German standards using the KOMA script document
classes.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/latexcheat-de

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
