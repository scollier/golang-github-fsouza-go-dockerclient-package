%global debug_package	%{nil}
%global goname		go-dockerclient
%global import_path	github.com/fsouza/%{goname}
%global gopath		%{_datadir}/gocode
%global commit		1f11e8a150726e38edba83abe7bf3ea4d81ca737
%global shortcommit	%(c=%{commit}; echo ${c:0:8})

Name:		golang-github-fsouza-%{goname}
Version:	0
Release:	0.4.git%{shortcommit}%{?dist}
Summary:	Client for the Docker remote API
License:	BSD
URL:		https://%{import_path}
Source0:	https://%{import_path}/archive/%{commit}/%{goname}-%{shortcommit}.tar.gz
%if 0%{?fedora} >= 19 
BuildArch:	noarch
%else
ExclusiveArch:	%{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
Requires:	golang
Summary:	Client for the Docker remote API
Provides:	golang(%{import_path}) = %{version}-%{release}
Provides:	golang(%{import_path}/engine) = %{version}-%{release}
Provides:	golang(%{import_path}/testing) = %{version}-%{release}
Provides:	golang(%{import_path}/utils) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for building other packages
which use fsouza/go-dockerclient.

%prep
%setup -n %{goname}-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
install -t %{buildroot}/%{gopath}/src/%{import_path} *.go
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/testing
install -t %{buildroot}/%{gopath}/src/%{import_path}/testing testing/*.go

%files devel
%defattr(-,root,root,-)
%doc LICENSE README.markdown
%dir %attr(755,root,root) %{gopath}
%dir %attr(755,root,root) %{gopath}/src
%dir %attr(755,root,root) %{gopath}/src/github.com
%dir %attr(755,root,root) %{gopath}/src/github.com/fsouza
%dir %attr(755,root,root) %{gopath}/src/github.com/fsouza/go-dockerclient
%{gopath}/src/%{import_path}/*.go
%{gopath}/src/%{import_path}/testing/*.go

%changelog
* Fri Aug 8 2014 Eric Paris <eparis@redhat.com>
- Update to newer version for Kubernetes (Paused support)

* Tue Jul 22 2014 Colin Walters <walters@redhat.com>
- Update to newer version for Kubernetes work

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.gitd639515
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 03 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.git
- Initial package
