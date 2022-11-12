Name:		texlive-ctex
Version:	63891
Release:	1
Summary:	LaTeX classes and packages for Chinese typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/chinese/ctex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-ttfutils

%description
TeXLive ctex package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ctex
%{_texmfdistdir}/tex/luatex/ctex
%{_texmfdistdir}/tex/generic/ctex
%doc %{_texmfdistdir}/doc/latex/ctex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
