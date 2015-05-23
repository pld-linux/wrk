Summary:	A modern HTTP benchmarking tool
Name:		wrk
Version:	3.1.1
Release:	0.1
License:	Apache v2.0
Group:		Networking/Utilities
Source0:	https://github.com/wg/wrk/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	bf25e174845bad36fefd66f9be71889e
Patch0:		makefile.patch
URL:		https://github.com/wg/wrk
BuildRequires:	luajit-devel >= 2.0.2
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wrk is a modern HTTP benchmarking tool capable of generating
significant load when run on a single multi-core CPU. It combines a
multithreaded design with scalable event notification systems such as
epoll and kqueue.

An optional LuaJIT script can perform HTTP request generation,
response processing, and custom reporting.

%prep
%setup -q
%patch0 -p1

rm -r deps/luajit

%build
CFLAGS="%{rpmcflags}" \
%{__make} V=1 \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NOTICE
