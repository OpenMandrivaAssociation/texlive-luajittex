Name:		texlive-luajittex
Version:	62774
Release:	2
Summary:	LuaTeX with just-in-time (jit) compiler, with and without HarfBuzz
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/luajittex
License:	
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luajittex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luajittex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/luajittex.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/luajittex.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/luajithbtex.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/luajithbtex.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
