%global tl_name luajittex
%global tl_revision 78968

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LuaTeX with just-in-time (jit) compiler, with and without HarfBuzz
Group:		Publishing
URL:		https://www.ctan.org/pkg/luajittex
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luajittex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luajittex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(cm)
Requires:	texlive(etex)
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive(knuth-lib)
Requires:	texlive(luajittex.bin)
Requires:	texlive(luatex)
Requires:	texlive(plain)
Requires:	texlive(tex-ini-files)
Requires:	texlive(unicode-data)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LuaTeX with just-in-time (jit) compiler, with and without HarfBuzz

