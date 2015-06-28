# TODO:
# - atlas support
#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	scipy
Summary:	A library of scientific tools
Summary(pl.UTF-8):	Biblioteka narzędzi naukowych
Name:		python-%{module}
Version:	0.13.2
Release:	3
License:	BSD
Group:		Development/Languages/Python
Source0:	http://heanet.dl.sourceforge.net/sourceforge/scipy/scipy-%{version}.tar.gz
# Source0-md5:	fcd110802b0bf3505ba567cf831566e1
URL:		http://www.scipy.org/
BuildRequires:	UMFPACK-devel
BuildRequires:	blas-devel
BuildRequires:	gcc-fortran
BuildRequires:	lapack-devel
%if %{with python2}
BuildRequires:	f2py >= 1:1.5.1-3
BuildRequires:	python
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-numpy >= 1:1.5.1-3
BuildRequires:	python-numpy-devel >= 1:1.5.1-3
BuildRequires:	python-numpy-numarray-devel >= 1:1.5.1-3
BuildRequires:	python-numpy-oldnumeric >= 1:1.5.1-3
%pyrequires_eq	python-modules
%endif
%if %{with python3}
BuildRequires:	f2py3 >= 1:1.5.1-3
BuildRequires:	python3
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-numpy >= 1:1.5.1-3
BuildRequires:	python3-numpy-devel >= 1:1.5.1-3
BuildRequires:	python3-numpy-numarray-devel >= 1:1.5.1-3
BuildRequires:	python3-numpy-oldnumeric >= 1:1.5.1-3
%endif
BuildRequires:	swig-python
Suggests:	python-PIL
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

%package -n python3-%{module}
Summary:	A library of scientific tools
Summary(pl.UTF-8):	Biblioteka narzędzi naukowych
Group:		Libraries/Python
%pyrequires_eq	python3-modules

%description -n python3-%{module}
SciPy is an open source library of scientific tools for Python. SciPy
supplements the popular numpy module, gathering a variety of high
level science and engineering modules together as a single package.

%description -n python3-%{module} -l pl.UTF-8
SciPy to biblioteka narzędzi naukowych z otwartymi źródłami dla
Pythona. SciPy uzupełnia popularny moduł numpy, gromadząc razem
wiele wysokopoziomowych modułów naukowych i inżynierskich w jeden
pakiet.

%prep
%setup -q -n scipy-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
export BLAS=%{_libdir}
export LAPACK=%{_libdir}
export UMFPACK=%{_libdir}

%if %{with python2}
%{__python} setup.py build --fcompiler=gnu95 --build-base build-2
%endif

%if %{with python3}
%{__python3} setup.py build --fcompiler=gnu95 --build-base build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT
export BLAS=%{_libdir}
export LAPACK=%{_libdir}
export UMFPACK=%{_libdir}

%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__mv} $RPM_BUILD_ROOT%{py_sitedir}/%{module}/weave/examples \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/weave

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*.txt
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*/{benchmarks,tests,doc}
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*/*/{benchmarks,tests}
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*/*/*/tests
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*/*/*/*/tests
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/%{module}/*.txt
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/%{module}/*/{benchmarks,tests}
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/%{module}/*/*/{benchmarks,tests}
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/%{module}/*/*/*/tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/%{module}/*/*/*/*/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc INSTALL.txt doc/README.txt THANKS.txt
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/_build_utils
%{py_sitedir}/%{module}/_build_utils/*.py
%{py_sitedir}/%{module}/_build_utils/*.py[co]
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
%dir %{py_sitedir}/%{module}/io/harwell_boeing
%{py_sitedir}/%{module}/io/harwell_boeing/*.py
%{py_sitedir}/%{module}/io/harwell_boeing/*.py[co]
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
%dir %{py_sitedir}/%{module}/misc
%{py_sitedir}/%{module}/misc/ascent.dat
%{py_sitedir}/%{module}/misc/face.dat
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
%dir %{py_sitedir}/%{module}/sparse/csgraph
%{py_sitedir}/%{module}/sparse/csgraph/*.py
%{py_sitedir}/%{module}/sparse/csgraph/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/sparse/csgraph/*.so
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
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc INSTALL.txt doc/README.txt THANKS.txt
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/%{module}/*.py
%{py3_sitedir}/%{module}/__pycache__
%dir %{py3_sitedir}/%{module}/_build_utils
%{py3_sitedir}/%{module}/_build_utils/*.py
%{py3_sitedir}/%{module}/_build_utils/__pycache__
%dir %{py3_sitedir}/%{module}/cluster
%attr(755,root,root) %{py3_sitedir}/%{module}/cluster/*.so
%{py3_sitedir}/%{module}/cluster/*.py
%{py3_sitedir}/%{module}/cluster/__pycache__
%dir %{py3_sitedir}/%{module}/constants
%{py3_sitedir}/%{module}/constants/*.py
%{py3_sitedir}/%{module}/constants/__pycache__
%dir %{py3_sitedir}/%{module}/fftpack
%attr(755,root,root) %{py3_sitedir}/%{module}/fftpack/*.so
%{py3_sitedir}/%{module}/fftpack/*.py
%{py3_sitedir}/%{module}/fftpack/__pycache__
%dir %{py3_sitedir}/%{module}/integrate
%attr(755,root,root) %{py3_sitedir}/%{module}/integrate/*.so
%{py3_sitedir}/%{module}/integrate/*.py
%{py3_sitedir}/%{module}/integrate/__pycache__
%dir %{py3_sitedir}/%{module}/interpolate
%attr(755,root,root) %{py3_sitedir}/%{module}/interpolate/*.so
%{py3_sitedir}/%{module}/interpolate/*.py
%{py3_sitedir}/%{module}/interpolate/__pycache__
%dir %{py3_sitedir}/%{module}/io
%{py3_sitedir}/%{module}/io/*.py
%{py3_sitedir}/%{module}/io/__pycache__
%dir %{py3_sitedir}/%{module}/io/arff
%{py3_sitedir}/%{module}/io/arff/*.py
%{py3_sitedir}/%{module}/io/arff/__pycache__
%dir %{py3_sitedir}/%{module}/io/matlab
%attr(755,root,root) %{py3_sitedir}/%{module}/io/matlab/*.so
%{py3_sitedir}/%{module}/io/matlab/*.py
%{py3_sitedir}/%{module}/io/matlab/__pycache__
%dir %{py3_sitedir}/%{module}/io/harwell_boeing
%{py3_sitedir}/%{module}/io/harwell_boeing/*.py
%{py3_sitedir}/%{module}/io/harwell_boeing/__pycache__
%dir %{py3_sitedir}/%{module}/lib
%{py3_sitedir}/%{module}/lib/*.py
%{py3_sitedir}/%{module}/lib/__pycache__
%dir %{py3_sitedir}/%{module}/lib/blas
%attr(755,root,root) %{py3_sitedir}/%{module}/lib/blas/*.so
%{py3_sitedir}/%{module}/lib/blas/*.py
%{py3_sitedir}/%{module}/lib/blas/__pycache__
%dir %{py3_sitedir}/%{module}/lib/lapack
%attr(755,root,root) %{py3_sitedir}/%{module}/lib/lapack/*.so
%{py3_sitedir}/%{module}/lib/lapack/*.py
%{py3_sitedir}/%{module}/lib/lapack/__pycache__
%dir %{py3_sitedir}/%{module}/linalg
%attr(755,root,root) %{py3_sitedir}/%{module}/linalg/*.so
%{py3_sitedir}/%{module}/linalg/*.py
%{py3_sitedir}/%{module}/linalg/__pycache__
%dir %{py3_sitedir}/%{module}/misc
%{py3_sitedir}/%{module}/misc/ascent.dat
%{py3_sitedir}/%{module}/misc/face.dat
%{py3_sitedir}/%{module}/misc/lena.dat
%{py3_sitedir}/%{module}/misc/*.py
%{py3_sitedir}/%{module}/misc/__pycache__
%dir %{py3_sitedir}/%{module}/ndimage
%attr(755,root,root) %{py3_sitedir}/%{module}/ndimage/*.so
%{py3_sitedir}/%{module}/ndimage/*.py
%{py3_sitedir}/%{module}/ndimage/__pycache__
%dir %{py3_sitedir}/%{module}/odr
%attr(755,root,root) %{py3_sitedir}/%{module}/odr/*.so
%{py3_sitedir}/%{module}/odr/*.py
%{py3_sitedir}/%{module}/odr/__pycache__
%dir %{py3_sitedir}/%{module}/optimize
%attr(755,root,root) %{py3_sitedir}/%{module}/optimize/*.so
%{py3_sitedir}/%{module}/optimize/*.py
%{py3_sitedir}/%{module}/optimize/__pycache__
%dir %{py3_sitedir}/%{module}/signal
%attr(755,root,root) %{py3_sitedir}/%{module}/signal/*.so
%{py3_sitedir}/%{module}/signal/*.py
%{py3_sitedir}/%{module}/signal/__pycache__
%dir %{py3_sitedir}/%{module}/sparse
%{py3_sitedir}/%{module}/sparse/*.py
%{py3_sitedir}/%{module}/sparse/__pycache__
%dir %{py3_sitedir}/%{module}/sparse/linalg
%{py3_sitedir}/%{module}/sparse/linalg/*.py
%{py3_sitedir}/%{module}/sparse/linalg/__pycache__
%dir %{py3_sitedir}/%{module}/sparse/csgraph
%{py3_sitedir}/%{module}/sparse/csgraph/*.py
%{py3_sitedir}/%{module}/sparse/csgraph/__pycache__
%attr(755,root,root) %{py3_sitedir}/%{module}/sparse/csgraph/*.so
%dir %{py3_sitedir}/%{module}/sparse/linalg/dsolve
%attr(755,root,root) %{py3_sitedir}/%{module}/sparse/linalg/dsolve/*.so
%{py3_sitedir}/%{module}/sparse/linalg/dsolve/*.py
%{py3_sitedir}/%{module}/sparse/linalg/dsolve/__pycache__
%dir %{py3_sitedir}/%{module}/sparse/linalg/dsolve/umfpack
%attr(755,root,root) %{py3_sitedir}/%{module}/sparse/linalg/dsolve/umfpack/*.so
%{py3_sitedir}/%{module}/sparse/linalg/dsolve/umfpack/*.py
%{py3_sitedir}/%{module}/sparse/linalg/dsolve/umfpack/__pycache__
%dir %{py3_sitedir}/%{module}/sparse/linalg/eigen
%{py3_sitedir}/%{module}/sparse/linalg/eigen/*.py
%{py3_sitedir}/%{module}/sparse/linalg/eigen/__pycache__
%dir %{py3_sitedir}/%{module}/sparse/linalg/eigen/arpack
%attr(755,root,root) %{py3_sitedir}/%{module}/sparse/linalg/eigen/arpack/*.so
%{py3_sitedir}/%{module}/sparse/linalg/eigen/arpack/*.py
%{py3_sitedir}/%{module}/sparse/linalg/eigen/arpack/__pycache__
%dir %{py3_sitedir}/%{module}/sparse/linalg/eigen/lobpcg
%{py3_sitedir}/%{module}/sparse/linalg/eigen/lobpcg/*.py
%{py3_sitedir}/%{module}/sparse/linalg/eigen/lobpcg/__pycache__
%dir %{py3_sitedir}/%{module}/sparse/linalg/isolve
%attr(755,root,root) %{py3_sitedir}/%{module}/sparse/linalg/isolve/*.so
%{py3_sitedir}/%{module}/sparse/linalg/isolve/*.py
%{py3_sitedir}/%{module}/sparse/linalg/isolve/__pycache__
%dir %{py3_sitedir}/%{module}/sparse/sparsetools
%attr(755,root,root) %{py3_sitedir}/%{module}/sparse/sparsetools/*.so
%{py3_sitedir}/%{module}/sparse/sparsetools/*.py
%{py3_sitedir}/%{module}/sparse/sparsetools/__pycache__
%dir %{py3_sitedir}/%{module}/spatial
%attr(755,root,root) %{py3_sitedir}/%{module}/spatial/*.so
%{py3_sitedir}/%{module}/spatial/*.py
%{py3_sitedir}/%{module}/spatial/__pycache__
%dir %{py3_sitedir}/%{module}/special
%attr(755,root,root) %{py3_sitedir}/%{module}/special/*.so
%{py3_sitedir}/%{module}/special/*.py
%{py3_sitedir}/%{module}/special/__pycache__
%dir %{py3_sitedir}/%{module}/stats
%attr(755,root,root) %{py3_sitedir}/%{module}/stats/*.so
%{py3_sitedir}/%{module}/stats/*.py
%{py3_sitedir}/%{module}/stats/__pycache__
%{py3_sitedir}/%{module}-%{version}-py*.egg-info
%endif
