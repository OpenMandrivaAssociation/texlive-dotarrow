# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/dotarrow
# catalog-date 2008-08-18 13:49:16 +0200
# catalog-license lppl
# catalog-version 0.01a
Name:		texlive-dotarrow
Version:	0.01a
Release:	4
Summary:	Extendable dotted arrows
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dotarrow
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dotarrow.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dotarrow.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dotarrow.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package can draw dotted arrows that are extendable, in the
same was as \xrightarrow.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dotarrow/DotArrow.sty
%doc %{_texmfdistdir}/doc/latex/dotarrow/DotArrow.pdf
%doc %{_texmfdistdir}/doc/latex/dotarrow/DotArrow.tex
%doc %{_texmfdistdir}/doc/latex/dotarrow/README
#- source
%doc %{_texmfdistdir}/source/latex/dotarrow/DotArrow.dtx
%doc %{_texmfdistdir}/source/latex/dotarrow/DotArrow.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.01a-2
+ Revision: 751038
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.01a-1
+ Revision: 718249
- texlive-dotarrow
- texlive-dotarrow
- texlive-dotarrow
- texlive-dotarrow

