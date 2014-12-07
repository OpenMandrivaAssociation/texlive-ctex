# revision 22488
# category Package
# catalog-ctan /language/chinese/ctex
# catalog-date 2011-05-15 00:28:51 +0200
# catalog-license lppl
# catalog-version 1.02c
Name:		texlive-ctex
Version:	1.02c
Release:	9
Summary:	LaTeX classes and packages for Chinese typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/chinese/ctex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctex.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/ctex/back/ctexartutf8.cls
%{_texmfdistdir}/tex/latex/ctex/back/ctexbookutf8.cls
%{_texmfdistdir}/tex/latex/ctex/back/ctexcaputf8.sty
%{_texmfdistdir}/tex/latex/ctex/back/ctexreputf8.cls
%{_texmfdistdir}/tex/latex/ctex/back/ctexutf8.sty
%{_texmfdistdir}/tex/latex/ctex/cfg/ctex.cfg
%{_texmfdistdir}/tex/latex/ctex/cfg/ctexcap-gbk.cfg
%{_texmfdistdir}/tex/latex/ctex/cfg/ctexcap-utf8.cfg
%{_texmfdistdir}/tex/latex/ctex/cfg/ctexcap.cfg
%{_texmfdistdir}/tex/latex/ctex/cfg/ctexopts.cfg.template
%{_texmfdistdir}/tex/latex/ctex/ctex.sty
%{_texmfdistdir}/tex/latex/ctex/ctexart.cls
%{_texmfdistdir}/tex/latex/ctex/ctexbook.cls
%{_texmfdistdir}/tex/latex/ctex/ctexcap.sty
%{_texmfdistdir}/tex/latex/ctex/ctexrep.cls
%{_texmfdistdir}/tex/latex/ctex/def/ctex-article.def
%{_texmfdistdir}/tex/latex/ctex/def/ctex-book.def
%{_texmfdistdir}/tex/latex/ctex/def/ctex-caption.def
%{_texmfdistdir}/tex/latex/ctex/def/ctex-class.def
%{_texmfdistdir}/tex/latex/ctex/def/ctex-common.def
%{_texmfdistdir}/tex/latex/ctex/def/ctex-gbk.def
%{_texmfdistdir}/tex/latex/ctex/def/ctex-loadclass.def
%{_texmfdistdir}/tex/latex/ctex/def/ctex-report.def
%{_texmfdistdir}/tex/latex/ctex/def/ctex-utf8.def
%{_texmfdistdir}/tex/latex/ctex/engine/ctex-cct-engine.def
%{_texmfdistdir}/tex/latex/ctex/engine/ctex-cjk-common.def
%{_texmfdistdir}/tex/latex/ctex/engine/ctex-cjk-engine.def
%{_texmfdistdir}/tex/latex/ctex/engine/ctex-xecjk-engine.def
%{_texmfdistdir}/tex/latex/ctex/fd/c19gbsn.fd
%{_texmfdistdir}/tex/latex/ctex/fd/c19gbsn.fdx
%{_texmfdistdir}/tex/latex/ctex/fd/c19gkai.fd
%{_texmfdistdir}/tex/latex/ctex/fd/c19gkai.fdx
%{_texmfdistdir}/tex/latex/ctex/fd/c19rm.fd
%{_texmfdistdir}/tex/latex/ctex/fd/c19sf.fd
%{_texmfdistdir}/tex/latex/ctex/fd/c19tt.fd
%{_texmfdistdir}/tex/latex/ctex/fd/c70rm.fd
%{_texmfdistdir}/tex/latex/ctex/fd/c70sf.fd
%{_texmfdistdir}/tex/latex/ctex/fd/c70tt.fd
%{_texmfdistdir}/tex/latex/ctex/fontset/ctex-cjk-adobefonts.def
%{_texmfdistdir}/tex/latex/ctex/fontset/ctex-cjk-winfonts.def
%{_texmfdistdir}/tex/latex/ctex/fontset/ctex-xecjk-adobefonts.def
%{_texmfdistdir}/tex/latex/ctex/fontset/ctex-xecjk-winfonts.def
%{_texmfdistdir}/tex/latex/ctex/opt/ctex-caption-opts.def
%{_texmfdistdir}/tex/latex/ctex/opt/ctex-class-opts.def
%{_texmfdistdir}/tex/latex/ctex/opt/ctex-common-opts.def
%doc %{_texmfdistdir}/doc/latex/ctex/README
%doc %{_texmfdistdir}/doc/latex/ctex/ctex.pdf
%doc %{_texmfdistdir}/doc/latex/ctex/ctex.tex
%doc %{_texmfdistdir}/doc/latex/ctex/test/test-cjk.tex
%doc %{_texmfdistdir}/doc/latex/ctex/test/test-cjkutf8.tex
%doc %{_texmfdistdir}/doc/latex/ctex/test/test-xetex.tex
%doc %{_texmfdistdir}/doc/latex/ctex/test/test-xetexgbk.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.02c-2
+ Revision: 750665
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.02c-1
+ Revision: 718180
- texlive-ctex
- texlive-ctex
- texlive-ctex
- texlive-ctex

