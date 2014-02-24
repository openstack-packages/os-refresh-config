Name:		os-refresh-config
Version:	0.0.8
Release:	2%{?dist}
Summary:	Refresh system configuration

License:	ASL 2.0
URL:		http://pypi.python.org/pypi/%{name}
Source0:	http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python2-devel

Requires:	python-setuptools

%description
Tool to refresh openstack config changes to service.

%prep

%setup -q -n %{name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst
%doc LICENSE
%{_bindir}/os-refresh-config
%{python_sitelib}/os_refresh_config*

%changelog
* Thu Feb 20 2014 Steven Dake <sdake@redhat.com> - 0.0.8-2
- Properly formatted changelog

* Wed Feb 19 2014 Steven Dake <sdake@redhat.com> - 0.0.8-1
- Update to version 0.0..8
- add python2-devel BuildRequires
- quiet setup

* Tue Oct 15 2013 Lucas Alvares Gomes <lgomes@redhat.com> - 0.0.2-1
- Update to version 0.0.2

* Fri Sep 6 2013 Lucas Alvares Gomes <lgomes@redhat.com> - 0.0.1-1
- Initial version
