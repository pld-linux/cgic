Summary:	A C library for CGI programming
Summary(pl):	Biblioteka C do programowania CGI
Name:		cgic
Version:	204
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://www.boutell.com/%{name}/%{name}%{version}.tar.gz
# Source0-md5:	4e4ed95f3f49ada0fb92a5e0d20283b3
Patch0:		%{name}-shared.patch
URL:		http://www.boutell.com/cgic/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cgic is an ANSI C-language library for the creation of CGI-based
World Wide Web applications.

%description -l pl
cgic jest bibliotek� j�zyka ANSI-C s�u��c� tworzeniu aplikacji WWW
opartych na CGI.

%package devel
Summary:	A C library for CGI programming - header files
Summary(pl):	Biblioteka C do programowania CGI - pliki nag��wkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for cgic library.

%description devel -l pl
Pliki nag��wkowe biblioteki cgic.

%package static
Summary:	A C library for CGI programming - static version
Summary(pl):	Biblioteka C do programowania CGI - wersja statyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of cgic library.

%description static -l pl
Statyczna wersja biblioteki cgic.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install libcgic.* $RPM_BUILD_ROOT%{_libdir}
install *.h $RPM_BUILD_ROOT%{_includedir}
cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libcgic.so.* libcgic.so

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc license.txt support.txt
%{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%doc *.html
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
