# TODO:
# - atlas, lapack support
# - rework files
%define		module	scipy
Summary:	A library of scientific tools
Summary(pl):	Biblioteka narzêdzi naukowych
Name:		python-%{module}
Version:	0.5.1
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://heanet.dl.sourceforge.net/sourceforge/scipy/scipy-%{version}.tar.gz
# Source0-md5:	48442a427f0556ad2ad1721dd62e401c
URL:		http://www.scipy.org/
BuildRequires:	X11-devel
BuildRequires:	blas-devel
BuildRequires:	lapack-devel
BuildRequires:	f2py
BuildRequires:	python
BuildRequires:	python-Numeric-devel
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-numpy >= 1:1.0
BuildRequires:	python-numpy-numarray >= 1:1.0
BuildRequires:	gcc-g77
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SciPy is an open source library of scientific tools for Python. SciPy
supplements the popular Numeric module, gathering a variety of high
level science and engineering modules together as a single package.

%description -l pl
SciPy to biblioteka narzêdzi naukowych z otwartymi ¼ród³ami dla
Pythona. SciPy uzupe³nia popularny modu³ Numeric, gromadz±c razem
wiele wysokopoziomowych modu³ów naukowych i in¿ynierskich w jeden
pakiet.

%prep
%setup -q -n scipy-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name '*.py' | \
	grep -v examples | \
	xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DEVELOPERS.txt THANKS.txt
%dir %{py_sitedir}/*
%{py_sitedir}/*/*
