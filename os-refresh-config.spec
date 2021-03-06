Name:		os-refresh-config
Version:	XXX
Release:	XXX
Summary:	Refresh system configuration

License:	ASL 2.0
URL:		http://pypi.python.org/pypi/%{name}
Source0:	http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python2-devel
BuildRequires:  python-pbr

Requires:   dib-utils
Requires:	python-setuptools

%description
Tool to refresh openstack config changes to service.

#
# patches_base: 0.1.5
#

%prep

%setup -q -n %{name}-%{upstream_version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# remove tests
rm -fr %{buildroot}%{python_sitelib}/os_refresh_config/tests

%files
%doc README.rst
%doc LICENSE
%{_bindir}/os-refresh-config
%{python_sitelib}/os_refresh_config*

%changelog
