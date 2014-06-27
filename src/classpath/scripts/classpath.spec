# $Id: classpath.spec.in,v 1.3 2006/12/10 20:25:50 gnu_andrew Exp $

%define version_num 0.98
%define release_num 1

Summary: GNU Classpath Java class libraries
Name: classpath
Version: %{version_num}
Release: %{release_num}
Group: Development/Tools
Copyright: GPL+exception
URL: http://www.classpath.org/
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: jikes, zip
Packager: GNU Classpath <classpath@gnu.org>
Source: ftp://ftp.gnu.org/pub/gnu/classpath/classpath-%{version_num}.tar.gz

%description
GNU Classpath, Essential Libraries for Java, is a GNU project to create
free core class libraries for use with virtual machines and compilers
for the Java programming language.

%prep
%setup -n classpath-%{version_num}

%build
pushd ${RPM_BUILD_DIR}/classpath-%{version_num}
# Determine if we can build the GTK stuff
GTKPEER='disable'
if pkg-config --exists 'gtk+-2.0 >= 2.4 gthread-2.0 >= 2.2 gdk-pixbuf-2.0'; then
    GTKPEER='enable'
fi
%configure --with-jikes --enable-jni --${GTKPEER}-gtk-peer
make
popd

%install
pushd ${RPM_BUILD_DIR}/classpath-%{version_num}
%{makeinstall}
popd

pushd ${RPM_BUILD_ROOT}/%{_infodir}
rm -f dir
for i in *; do
    mv $i classpath-$i
done
popd

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING LICENSE README THANKYOU
%{_libdir}/classpath
%dir %{_datadir}/classpath
%{_libdir}/security/classpath.security
%{_datadir}/classpath/glibj.zip
%doc %{_datadir}/classpath/api
%doc %{_datadir}/classpath/examples
%doc %{_infodir}/*

