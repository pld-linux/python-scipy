# TODO:
# - atlas support
%define		module	scipy
Summary:	A library of scientific tools
Summary(pl.UTF-8):	Biblioteka narzędzi naukowych
Name:		python-%{module}
Version:	0.9.0
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://heanet.dl.sourceforge.net/sourceforge/scipy/scipy-%{version}.tar.gz
# Source0-md5:	ebfef6e8e82d15c875a4ee6a46d4e1cd
URL:		http://www.scipy.org/
BuildRequires:	UMFPACK-devel
BuildRequires:	blas-devel
BuildRequires:	f2py
BuildRequires:	gcc-fortran
BuildRequires:	lapack-devel
BuildRequires:	python
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-numpy >= 1:1.5.1-3
BuildRequires:	python-numpy-numarray-devel >= 1:1.5.1-3
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SciPy is an open source library of scientific tools for Python. SciPy
supplements the popular numpy module, gathering a variety of high
level science and engineering modules together as a single package.

%description -l pl.UTF-8
SciPy to biblioteka narzędzi naukowych z otwartymi źródłami dla
Pythona. SciPy uzupełnia popularny moduł numpy, gromadząc razem
wiele wysokopoziomowych modułów naukowych i inżynierskich w jeden
pakiet.

%prep
%setup -q -n scipy-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build --fcompiler=gnu95

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{py_sitedir}/%{module}/maxentropy/examples \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/maxentropy
mv $RPM_BUILD_ROOT%{py_sitedir}/%{module}/weave/examples \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/weave

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*.txt
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*/{benchmarks,tests,doc}
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*/*/{benchmarks,tests}
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*/*/*/tests
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*/*/*/*/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL.txt LATEST.txt README.txt THANKS.txt TOCHANGE.txt
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/cluster
%attr(755,root,root) %{py_sitedir}/%{module}/cluster/*.so
%{py_sitedir}/%{module}/cluster/*.py
%{py_sitedir}/%{module}/cluster/*.py[co]
%dir %{py_sitedir}/%{module}/constants
%{py_sitedir}/%{module}/constants/*.py
%{py_sitedir}/%{module}/constants/*.py[co]
%dir %{py_sitedir}/%{module}/fftpack
%attr(755,root,root) %{py_sitedir}/%{module}/fftpack/*.so
%{py_sitedir}/%{module}/fftpack/*.py
%{py_sitedir}/%{module}/fftpack/*.py[co]
%dir %{py_sitedir}/%{module}/integrate
%attr(755,root,root) %{py_sitedir}/%{module}/integrate/*.so
%{py_sitedir}/%{module}/integrate/*.py
%{py_sitedir}/%{module}/integrate/*.py[co]
%dir %{py_sitedir}/%{module}/interpolate
%attr(755,root,root) %{py_sitedir}/%{module}/interpolate/*.so
%{py_sitedir}/%{module}/interpolate/*.py
%{py_sitedir}/%{module}/interpolate/*.py[co]
%dir %{py_sitedir}/%{module}/io
%{py_sitedir}/%{module}/io/*.py
%{py_sitedir}/%{module}/io/*.py[co]
%dir %{py_sitedir}/%{module}/io/arff
%{py_sitedir}/%{module}/io/arff/*.py
%{py_sitedir}/%{module}/io/arff/*.py[co]
%dir %{py_sitedir}/%{module}/io/matlab
%attr(755,root,root) %{py_sitedir}/%{module}/io/matlab/*.so
%{py_sitedir}/%{module}/io/matlab/*.py
%{py_sitedir}/%{module}/io/matlab/*.py[co]
%dir %{py_sitedir}/%{module}/lib
%{py_sitedir}/%{module}/lib/*.py
%{py_sitedir}/%{module}/lib/*.py[co]
%dir %{py_sitedir}/%{module}/lib/blas
%attr(755,root,root) %{py_sitedir}/%{module}/lib/blas/*.so
%{py_sitedir}/%{module}/lib/blas/*.py
%{py_sitedir}/%{module}/lib/blas/*.py[co]
%dir %{py_sitedir}/%{module}/lib/lapack
%attr(755,root,root) %{py_sitedir}/%{module}/lib/lapack/*.so
%{py_sitedir}/%{module}/lib/lapack/*.py
%{py_sitedir}/%{module}/lib/lapack/*.py[co]
%dir %{py_sitedir}/%{module}/linalg
%attr(755,root,root) %{py_sitedir}/%{module}/linalg/*.so
%{py_sitedir}/%{module}/linalg/*.py
%{py_sitedir}/%{module}/linalg/*.py[co]
%dir %{py_sitedir}/%{module}/maxentropy
%{py_sitedir}/%{module}/maxentropy/*.py
%{py_sitedir}/%{module}/maxentropy/*.py[co]
%dir %{py_sitedir}/%{module}/misc
%{py_sitedir}/%{module}/misc/lena.dat
%{py_sitedir}/%{module}/misc/*.py
%{py_sitedir}/%{module}/misc/*.py[co]
%dir %{py_sitedir}/%{module}/ndimage
%attr(755,root,root) %{py_sitedir}/%{module}/ndimage/*.so
%{py_sitedir}/%{module}/ndimage/*.py
%{py_sitedir}/%{module}/ndimage/*.py[co]
%dir %{py_sitedir}/%{module}/odr
%attr(755,root,root) %{py_sitedir}/%{module}/odr/*.so
%{py_sitedir}/%{module}/odr/*.py
%{py_sitedir}/%{module}/odr/*.py[co]
%dir %{py_sitedir}/%{module}/optimize
%attr(755,root,root) %{py_sitedir}/%{module}/optimize/*.so
%{py_sitedir}/%{module}/optimize/*.py
%{py_sitedir}/%{module}/optimize/*.py[co]
%dir %{py_sitedir}/%{module}/signal
%attr(755,root,root) %{py_sitedir}/%{module}/signal/*.so
%{py_sitedir}/%{module}/signal/*.py
%{py_sitedir}/%{module}/signal/*.py[co]
%dir %{py_sitedir}/%{module}/sparse
%{py_sitedir}/%{module}/sparse/*.py
%{py_sitedir}/%{module}/sparse/*.py[co]
%dir %{py_sitedir}/%{module}/sparse/linalg
%{py_sitedir}/%{module}/sparse/linalg/*.py
%{py_sitedir}/%{module}/sparse/linalg/*.py[co]
%dir %{py_sitedir}/%{module}/sparse/linalg/dsolve
%attr(755,root,root) %{py_sitedir}/%{module}/sparse/linalg/dsolve/*.so
%{py_sitedir}/%{module}/sparse/linalg/dsolve/*.py
%{py_sitedir}/%{module}/sparse/linalg/dsolve/*.py[co]
%dir %{py_sitedir}/%{module}/sparse/linalg/dsolve/umfpack
%attr(755,root,root) %{py_sitedir}/%{module}/sparse/linalg/dsolve/umfpack/*.so
%{py_sitedir}/%{module}/sparse/linalg/dsolve/umfpack/*.py
%{py_sitedir}/%{module}/sparse/linalg/dsolve/umfpack/*.py[co]
%dir %{py_sitedir}/%{module}/sparse/linalg/eigen
%{py_sitedir}/%{module}/sparse/linalg/eigen/*.py
%{py_sitedir}/%{module}/sparse/linalg/eigen/*.py[co]
%dir %{py_sitedir}/%{module}/sparse/linalg/eigen/arpack
%attr(755,root,root) %{py_sitedir}/%{module}/sparse/linalg/eigen/arpack/*.so
%{py_sitedir}/%{module}/sparse/linalg/eigen/arpack/*.py
%{py_sitedir}/%{module}/sparse/linalg/eigen/arpack/*.py[co]
%dir %{py_sitedir}/%{module}/sparse/linalg/eigen/lobpcg
%{py_sitedir}/%{module}/sparse/linalg/eigen/lobpcg/*.py
%{py_sitedir}/%{module}/sparse/linalg/eigen/lobpcg/*.py[co]
%dir %{py_sitedir}/%{module}/sparse/linalg/isolve
%attr(755,root,root) %{py_sitedir}/%{module}/sparse/linalg/isolve/*.so
%{py_sitedir}/%{module}/sparse/linalg/isolve/*.py
%{py_sitedir}/%{module}/sparse/linalg/isolve/*.py[co]
%dir %{py_sitedir}/%{module}/sparse/sparsetools
%attr(755,root,root) %{py_sitedir}/%{module}/sparse/sparsetools/*.so
%{py_sitedir}/%{module}/sparse/sparsetools/*.py
%{py_sitedir}/%{module}/sparse/sparsetools/*.py[co]
%dir %{py_sitedir}/%{module}/spatial
%attr(755,root,root) %{py_sitedir}/%{module}/spatial/*.so
%{py_sitedir}/%{module}/spatial/*.py
%{py_sitedir}/%{module}/spatial/*.py[co]
%dir %{py_sitedir}/%{module}/special
%attr(755,root,root) %{py_sitedir}/%{module}/special/*.so
%{py_sitedir}/%{module}/special/*.py
%{py_sitedir}/%{module}/special/*.py[co]
%dir %{py_sitedir}/%{module}/stats
%attr(755,root,root) %{py_sitedir}/%{module}/stats/*.so
%{py_sitedir}/%{module}/stats/*.py
%{py_sitedir}/%{module}/stats/*.py[co]
%dir %{py_sitedir}/%{module}/weave
%{py_sitedir}/%{module}/weave/*.py
%{py_sitedir}/%{module}/weave/*.py[co]
%{py_sitedir}/%{module}/weave/blitz
%{py_sitedir}/%{module}/weave/scxx
%if "%{py_ver}" > "2.4"
%{py_sitedir}/%{module}-%{version}-py*.egg-info
%endif
%{_examplesdir}/%{name}-%{version}
