%global debug_package   %{nil}
%global import_path     github.com/fsouza/go-dockerclient
%global gopath          %{_datadir}/gocode
%global commit          d639515f70e535d4bbff8499992beeb48d8bf340
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-fsouza-go-dockerclient
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Client for the Docker remote API
License:        BSD
URL:            https://%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/go-dockerclient-%{shortcommit}.tar.gz
%if 0%{?fedora} >= 19 
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
Requires:       golang
Summary:        Client for the Docker remote API
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/engine) = %{version}-%{release}
Provides:       golang(%{import_path}/testing) = %{version}-%{release}
Provides:       golang(%{import_path}/utils) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for building other packages
which use fsouza/go-dockerclient.

%prep
%setup -n go-dockerclient-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/{engine,testing,utils}
for d in . engine testing utils; do
    cp -av $d/*.go %{buildroot}/%{gopath}/src/%{import_path}/$d
done

%files devel
%defattr(-,root,root,-)
%doc LICENSE README.markdown
%dir %attr(755,root,root) %{gopath}
%dir %attr(755,root,root) %{gopath}/src
%dir %attr(755,root,root) %{gopath}/src/github.com
%dir %attr(755,root,root) %{gopath}/src/github.com/fsouza
%dir %attr(755,root,root) %{gopath}/src/github.com/fsouza/go-dockerclient
%{gopath}/src/%{import_path}/*.go
%{gopath}/src/%{import_path}/engine/*.go
%{gopath}/src/%{import_path}/testing/*.go
%{gopath}/src/%{import_path}/utils/*.go

%changelog
* Thu Apr 03 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.git
- Initial package
