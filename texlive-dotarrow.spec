# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/dotarrow
# catalog-date 2008-08-18 13:49:16 +0200
# catalog-license lppl
# catalog-version 0.01a
Name:		texlive-dotarrow
Version:	0.01a
Release:	1
Summary:	Extendable dotted arrows
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dotarrow
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dotarrow.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dotarrow.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dotarrow.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package can draw dotted arrows that are extendable, in the
same was as \xrightarrow.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
