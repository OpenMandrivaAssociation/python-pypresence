%define module    pypresence

Name:           python-%{module}
Version:        4.2.1
Release:        2
Summary:        A complete Discord RPC and Rich Presence wrapper library in Python
Group:          Development/Python
License:        BSD 3-Clause
URL:            https://github.com/qwertyquerty/pypresence
Source0:        https://files.pythonhosted.org/packages/source/p/pypresence/pypresence-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)


%{?python_provide:%python_provide python3-%{module}}

%description
A complete Discord IPC and Rich Presence wrapper library in Python!

#----------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%install
%py_install

%files
#doc CHANGELOG.md README.md
#license LICENSE.txt
#{_bindir}/qta-browser
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-%{version}-py%{python_version}.egg-info
