%{?_javapackages_macros:%_javapackages_macros}
Name:             rmic-maven-plugin
Version:          1.2.1
Release:          6.0%{?dist}
Summary:          Uses the java rmic compiler to generate classes used in remote method invocation
License:          MIT

URL:              http://mojo.codehaus.org/%{name}

Source0:          http://repo2.maven.org/maven2/org/codehaus/mojo/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:           pom-compiler-source-target.patch

BuildArch:        noarch

BuildRequires:    java-devel >= 1:1.6.0
BuildRequires:    maven-local
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-invoker-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    maven-checkstyle-plugin

%description
This plugin works with Maven 2 and uses the java rmic compiler to generate
classes used in remote method invocation.

%package javadoc
Summary:          Javadoc for %{name}


%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
sed -i -e "s|groupId>plexus|groupId>org.codehaus.plexus|g" pom.xml

%patch0 -p0

%mvn_file :rmic-maven-plugin rmic-maven-plugin

%build
# Unit tests pass, but for some reason the integrations fail in mock
%mvn_build -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%doc License.txt

%files javadoc -f .mfiles-javadoc
%doc License.txt

%changelog
* Wed Aug 07 2013 Mat Booth <fedora@matbooth.co.uk> - 1.2.1-6
- Update for newer guidelines

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 29 2013 Mat Booth <fedora@matbooth.co.uk> - 1.2.1-4
- Fix FTBFS rhbz #914442

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2.1-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Dec 28 2012 Chris Spike <spike@fedoraproject.org> 1.2.1-1
- Update to latest upstream.

* Sat Dec 8 2012 Chris Spike <spike@fedoraproject.org> 1.2.0-2
- Removed BR 'plexus-container-default' (#878579)
- R/BR cleanup
- Removed all 'jpackage-utils' dependencies

* Mon Jul 23 2012 Alexander Kurtakov <akurtako@redhat.com> 1.2.0-1
- Update to latest upstream.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed May 18 2011 Chris Spike <spike@fedoraproject.org> 1.1-7
- Adapted to current java packaging guidelines

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 5 2010 Chris Spike <spike@fedoraproject.org> 1.1-5
- Consistently using 'buildroot' macro instead of 'RPM_BUILD_ROOT' now

* Thu Jul 15 2010 Chris Spike <spike@fedoraproject.org> 1.1-4
- Set maven2.jpp.mode to true
- Extensive use of buildroot-macro
- Moved from Development/Tools -> Development/Libraries
- Set maven.test.failure.ignore to true (do tests again, but ignore failures)
- Changed summary to be more descriptive
- Removed BuildArch from javadoc subpackage
- Added BR mojo-parent to fix FTBFS (#631167)

* Mon Jul 12 2010 Chris Spike <spike@fedoraproject.org> 1.1-3
- Changed 'Source0' to match upstream source release zip-file

* Mon Jul 12 2010 Chris Spike <spike@fedoraproject.org> 1.1-2
- Skipping tests

* Fri Jul 9 2010 Chris Spike <spike@fedoraproject.org> 1.1-1
- Initial version of the package
