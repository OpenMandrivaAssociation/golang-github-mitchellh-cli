# http://github.com/mitchellh/cli

%global goipath         github.com/mitchellh/cli
%global commit          c48282d14eba4b0817ddef3f832ff8d13851aefd


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.7%{?dist}
Summary:        Go library for implementing command-line interfaces
# Detected licences
# - *No copyright* MPL (v2.0) at 'LICENSE'
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(golang.org/x/crypto/ssh/terminal)
BuildRequires: golang-github-armon-go-radix-devel
BuildRequires: golang-github-bgentry-speakeasy-devel
BuildRequires: golang-github-fatih-color-devel
BuildRequires: golang-github-mattn-go-colorable-devel
BuildRequires: golang-github-mattn-go-isatty-devel
BuildRequires: golang-github-posener-complete-devel
BuildRequires: golang-github-shiena-ansicolor-devel

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Thu Aug 02 2018 Michael Cronenworth <mike@cchtml.com> - 0-0.7.gitc48282d
- Update to 20180414 git checkout

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git8102d0e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.5.git8102d0e
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git8102d0e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git8102d0e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git8102d0e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.git8102d0e
- First package for Fedora
  resolves: #1060502

