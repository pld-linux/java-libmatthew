%include	/usr/lib/rpm/macros.java
Summary:	Selection of Java libraries by Matthew Johnson
Summary(pl.UTF-8):	Wybrane biblioteki Javy autorstwa Matthew Johnsona
Name:		java-libmatthew
Version:	0.7.2
Release:	1
License:	LGPL v2.1
Group:		Libraries/Java
Source0:	http://www.matthew.ath.cx/projects/java/libmatthew-java-%{version}.tar.gz
# Source0-md5:	774e0b0b9c021acd1f2280c908865c3c
URL:		http://www.matthew.ath.cx/projects/java/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Selection of Java libraries by Matthew Johnson, including:
- Unix Sockets Library,
- Debug Library,
- CGI Library,
- I/O Library.

%description -l pl.UTF-8
Wybrane biblioteki Javy autorstwa Matthew Johnsona, w tym:
- Unix Sockets Library - biblioteka gniazd uniksowych,
- Debug Library - biblioteka diagnostyczna,
- CGI Library - biblioteka CGI,
- I/O Library - biblioteka wejścia/wyjścia.

%prep
%setup -q -n libmatthew-java-%{version}

%build
%{__make} \
	JAVA_HOME="%{java_home}" \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC -std=c99 -Wall" \
	LD="%{__cc}" \
	LDFLAGS="%{rpmldflags} -shared" \
	JCFLAGS="-source 1.5"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_jnidir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README changelog
%attr(755,root,root) %{_jnidir}/libcgi-java.so
%attr(755,root,root) %{_jnidir}/libunix-java.so
%{_javadir}/cgi*.jar
%{_javadir}/debug-disable*.jar
%{_javadir}/debug-enable*.jar
%{_javadir}/hexdump*.jar
%{_javadir}/io*.jar
%{_javadir}/unix*.jar
