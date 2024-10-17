Name:		texlive-dotarrow
Version:	15878
Release:	2
Summary:	Extendable dotted arrows
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dotarrow
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dotarrow.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dotarrow.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dotarrow.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
