
Summary: RCLocal Scripts
Name: rclocal
Version: 2.1.0
Release: 1
License: Distributable
Group: System Environment/Base
BuildArch: noarch

Packager: Nathan Neulinger <nneul@neulinger.org>

Source: rclocal.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This contains the init script for the /home/local/adm/rc-(start|stop) facility

%prep
%setup -c -q

%build

%install
mkdir -p $RPM_BUILD_ROOT/home/local/adm/rc-start
mkdir -p $RPM_BUILD_ROOT/home/local/adm/rc-stop

if [ -e "/etc/init.d" ]; then
	mkdir -p $RPM_BUILD_ROOT/etc/init.d
	cp -pr rclocal/rclocal $RPM_BUILD_ROOT/etc/init.d/
else if [ -e "/etc/rc.d/init.d" ]; then
	mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
	cp -pr rclocal/rclocal $RPM_BUILD_ROOT/etc/rc.d/init.d/
fi

%clean
%{__rm} -rf %{buildroot}

%post
chkconfig --del rclocal
chkconfig --add rclocal
chkconfig rclocal on

%files
%attr(0755, root, root) /*

%changelog
