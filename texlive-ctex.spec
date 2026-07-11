%global tl_name ctex
%global tl_revision 79569

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.6.1
Release:	%{tl_revision}.1
Summary:	LaTeX classes and packages for Chinese typesetting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/chinese/ctex
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ctex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ctex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ctex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(adobemapping)
Requires:	texlive(atbegshi)
Requires:	texlive(beamer)
Requires:	texlive(chinese-jfm)
Requires:	texlive(cjk)
Requires:	texlive(cjkpunct)
Requires:	texlive(ec)
Requires:	texlive(epstopdf-pkg)
Requires:	texlive(etoolbox)
Requires:	texlive(everyhook)
Requires:	texlive(fandol)
Requires:	texlive(fontspec)
Requires:	texlive(iftex)
Requires:	texlive(infwarerr)
Requires:	texlive(kvoptions)
Requires:	texlive(kvsetkeys)
Requires:	texlive(latex-bin)
Requires:	texlive(ltxcmds)
Requires:	texlive(luatexja)
Requires:	texlive(mptopdf)
Requires:	texlive(pdftexcmds)
Requires:	texlive(platex-tools)
Requires:	texlive(svn-prov)
Requires:	texlive(tipa)
Requires:	texlive(tools)
Requires:	texlive(ttfutils)
Requires:	texlive(ulem)
Requires:	texlive(uplatex)
Requires:	texlive(xcjk2uni)
Requires:	texlive(xecjk)
Requires:	texlive(xetex)
Requires:	texlive(xkeyval)
Requires:	texlive(xpinyin)
Requires:	texlive(xunicode)
Requires:	texlive(zhmetrics)
Requires:	texlive(zhmetrics-uptex)
Requires:	texlive(zhnumber)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
ctex is a bundle of LaTeX classes and packages for typesetting documents
in Chinese. It works with the (pdf)LaTeX, XeLaTeX and LuaLaTeX engines,
supports GB2312 / UTF-8 / Unicode input, integrates Chinese punctuation
kerning, multi-engine font configuration, and provides Chinese-style
section heading commands for the standard article / book / report
classes.

