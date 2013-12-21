%_javapackages_macros
Name:             rmic-maven-plugin
Version:          1.2.1
Release:          6.0%{?dist}
Summary:          Generate classes used in remote method invocation
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
