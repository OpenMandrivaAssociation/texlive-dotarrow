%global tl_name dotarrow
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.01a
Release:	%{tl_revision}.1
Summary:	Extendable dotted arrows
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dotarrow
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dotarrow.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dotarrow.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dotarrow.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package can draw dotted arrows that are extendable, in the same was
as \xrightarrow.

