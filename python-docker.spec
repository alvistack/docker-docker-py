# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-docker
Epoch: 100
Version: 7.1.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Docker API Client
License: Apache-2.0
URL: https://github.com/docker/docker-py/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
It lets you do anything the docker command does, but from within Python
apps - run containers, manage containers, manage Swarms, etc.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-docker
Summary: Docker API Client
Requires: python3
Requires: python3-paramiko >= 2.4.3
Requires: python3-requests >= 2.26.0
Requires: python3-urllib3 >= 1.26.0
Requires: python3-websocket-client >= 1.3.0
Provides: python3-docker = %{epoch}:%{version}-%{release}
Provides: python3dist(docker) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-docker = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(docker) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-docker = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(docker) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-docker
It lets you do anything the docker command does, but from within Python
apps - run containers, manage containers, manage Swarms, etc.

%files -n python%{python3_version_nodots}-docker
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-docker
Summary: Docker API Client
Requires: python3
Requires: python3-paramiko >= 2.4.3
Requires: python3-requests >= 2.26.0
Requires: python3-urllib3 >= 1.26.0
Requires: python3-websocket-client >= 1.3.0
Provides: python3-docker = %{epoch}:%{version}-%{release}
Provides: python3dist(docker) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-docker = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(docker) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-docker = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(docker) = %{epoch}:%{version}-%{release}

%description -n python3-docker
It lets you do anything the docker command does, but from within Python
apps - run containers, manage containers, manage Swarms, etc.

%files -n python3-docker
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
