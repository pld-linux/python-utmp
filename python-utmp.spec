Summary:	Python modules for umtp records
Name:		python-utmp
Version:	0.7
Release:	3
License:	Copyright only
Group:		Libraries
Source0:	http://kassiopeia.juls.savba.sk/~garabik/software/python-utmp/old/%{name}_%{version}.tar.gz
# Source0-md5:	9ff7241fb388169bf0f5a8c3009145f9
URL:		http://kassiopeia.juls.savba.sk/~garabik/software/python-utmp/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
python-utmp consists of three modules, providing access to utmp
records. It is quite difficult to access utmp record portably, because
every UNIX has different structure of utmp files. Currently,
python-utmp works on platforms which provide getutent, getutid,
getutline, pututline, setutent, endutent and utmpname functions (such
as GNU systems (Linux and hurd) and System V unices) and on BSD
systems using simple utmp structure.

%prep
%setup -q

mv -f debian/copyright COPYING

%build
%{__make} -f Makefile.glibc \
	DEFINES=" \
		-D_HAVE_UT_SESSION -D_HAVE_UT_ADDR_V6 -D_HAVE_UT_EXIT \
		-D_HAVE_UT_HOST -D_HAVE_UT_ID -D_HAVE_UT_TV -D_HAVE_UT_USER \
		-D_HAVE_UTMPNAME -D_HAVE_SETUTENT -D_HAVE_GETUTENT -D_HAVE_ENDUTENT \
		-D_HAVE_GETUTID -D_HAVE_GETUTLINE -D_HAVE_PUTUTLINE \
		%{optflags}" \
	PYTHONVER=%{python_version}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PYTHONDIR=$RPM_BUILD_ROOT/%{py_sitescriptdir}/ \
	PYTHONVER=%{python_version} \

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README TODO
%attr(755,root,root) %{py_sitescriptdir}/utmpaccessmodule.so
