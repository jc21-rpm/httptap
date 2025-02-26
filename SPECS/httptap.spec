%define debug_package %{nil}

%global gh_user monasticacademy

Name:           httptap
Version:        0.1.0
Release:        1%{?dist}
Summary:        View HTTP/HTTPS requests made by any Linux program
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
BuildRequires:  git golang

%description
View the HTTP and HTTPS requests made by any linux program by running httptap -- <command>.
https://www.monasticacademy.org/

%prep
%setup -q -n %{name}-%{version}

%build
go build -o %{_builddir}/bin/%{name}

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc LICENSE README.md

%changelog
* Thu Feb 27 2025 Jamie Curnow <jc@jc21.com> 0.1.0-1
- v0.1.0

* Thu Feb 6 2025 Jamie Curnow <jc@jc21.com> 0.0.8-1
- v0.0.8
