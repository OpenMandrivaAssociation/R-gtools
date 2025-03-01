%global packname  gtools
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          3.3.0
Release:          2
Summary:          Various R programming tools
Group:            Sciences/Mathematics
License:          LGPL-2.1
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/gtools_3.3.0.tar.gz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 

%description
Various R programming tools

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Sat Feb 18 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.6.2-1
+ Revision: 777009
- Import R-gtools
- Import R-gtools






