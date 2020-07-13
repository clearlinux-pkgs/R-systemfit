#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-systemfit
Version  : 1.1.24
Release  : 28
URL      : https://cran.r-project.org/src/contrib/systemfit_1.1-24.tar.gz
Source0  : https://cran.r-project.org/src/contrib/systemfit_1.1-24.tar.gz
Summary  : Estimating Systems of Simultaneous Equations
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-car
Requires: R-lmtest
Requires: R-sandwich
BuildRequires : R-car
BuildRequires : R-carData
BuildRequires : R-lmtest
BuildRequires : R-sandwich
BuildRequires : R-zoo
BuildRequires : buildreq-R

%description
systems of linear and nonlinear equations using Ordinary Least
 Squares (OLS), Weighted Least Squares (WLS), Seemingly Unrelated
 Regressions (SUR), Two-Stage Least Squares (2SLS), Weighted
 Two-Stage Least Squares (W2SLS), and Three-Stage Least Squares (3SLS)

%prep
%setup -q -c -n systemfit
cd %{_builddir}/systemfit

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589774854

%install
export SOURCE_DATE_EPOCH=1589774854
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library systemfit
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library systemfit
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library systemfit
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/systemfit/CITATION
/usr/lib64/R/library/systemfit/DESCRIPTION
/usr/lib64/R/library/systemfit/INDEX
/usr/lib64/R/library/systemfit/Meta/Rd.rds
/usr/lib64/R/library/systemfit/Meta/data.rds
/usr/lib64/R/library/systemfit/Meta/features.rds
/usr/lib64/R/library/systemfit/Meta/hsearch.rds
/usr/lib64/R/library/systemfit/Meta/links.rds
/usr/lib64/R/library/systemfit/Meta/nsInfo.rds
/usr/lib64/R/library/systemfit/Meta/package.rds
/usr/lib64/R/library/systemfit/Meta/vignette.rds
/usr/lib64/R/library/systemfit/NAMESPACE
/usr/lib64/R/library/systemfit/NEWS
/usr/lib64/R/library/systemfit/R/systemfit
/usr/lib64/R/library/systemfit/R/systemfit.rdb
/usr/lib64/R/library/systemfit/R/systemfit.rdx
/usr/lib64/R/library/systemfit/data/GrunfeldGreene.rda
/usr/lib64/R/library/systemfit/data/KleinI.txt.gz
/usr/lib64/R/library/systemfit/data/Kmenta.txt.gz
/usr/lib64/R/library/systemfit/data/ppine.txt.gz
/usr/lib64/R/library/systemfit/doc/index.html
/usr/lib64/R/library/systemfit/doc/systemfit.R
/usr/lib64/R/library/systemfit/doc/systemfit.Rnw
/usr/lib64/R/library/systemfit/doc/systemfit.bib
/usr/lib64/R/library/systemfit/doc/systemfit.pdf
/usr/lib64/R/library/systemfit/help/AnIndex
/usr/lib64/R/library/systemfit/help/aliases.rds
/usr/lib64/R/library/systemfit/help/paths.rds
/usr/lib64/R/library/systemfit/help/systemfit.rdb
/usr/lib64/R/library/systemfit/help/systemfit.rdx
/usr/lib64/R/library/systemfit/html/00Index.html
/usr/lib64/R/library/systemfit/html/R.css
/usr/lib64/R/library/systemfit/tests/KleinI.R
/usr/lib64/R/library/systemfit/tests/KleinI.Rout.save
/usr/lib64/R/library/systemfit/tests/KleinI_noMat.R
/usr/lib64/R/library/systemfit/tests/KleinI_noMat.Rout.save
/usr/lib64/R/library/systemfit/tests/test_2sls.R
/usr/lib64/R/library/systemfit/tests/test_2sls.Rout.save
/usr/lib64/R/library/systemfit/tests/test_3sls.R
/usr/lib64/R/library/systemfit/tests/test_3sls.Rout.save
/usr/lib64/R/library/systemfit/tests/test_hausman.R
/usr/lib64/R/library/systemfit/tests/test_hausman.Rout.save
/usr/lib64/R/library/systemfit/tests/test_ols.R
/usr/lib64/R/library/systemfit/tests/test_ols.Rout.save
/usr/lib64/R/library/systemfit/tests/test_panel.R
/usr/lib64/R/library/systemfit/tests/test_panel.Rout.save
/usr/lib64/R/library/systemfit/tests/test_sur.R
/usr/lib64/R/library/systemfit/tests/test_sur.Rout.save
/usr/lib64/R/library/systemfit/tests/test_w2sls.R
/usr/lib64/R/library/systemfit/tests/test_w2sls.Rout.save
/usr/lib64/R/library/systemfit/tests/test_wls.R
/usr/lib64/R/library/systemfit/tests/test_wls.Rout.save
