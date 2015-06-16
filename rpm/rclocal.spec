
Summary: RCLocal Scripts
Name: rclocal
Version: 2.1.0
Release: 1
License: Distributable
Group: System Environment/Base
BuildArch: noarch

Packager: Nathan Neulinger <nneul@neulinger.org>

Source: rclocal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This contains the init script for the /home/local/adm/rc-(start|stop) facility

%prep
%setup -c -q -n rclocal

%build
cd rclocal-%{version}
make DESTDIR=$RPM_BUILD_ROOT

%install

cd rclocal-%{version}
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT/home/local/adm/rc-start
mkdir -p $RPM_BUILD_ROOT/home/local/adm/rc-stop

mkdir -p $RPM_BUILD_ROOT/etc/init.d
cp -pr files/rclocal $RPM_BUILD_ROOT/etc/init.d/

%clean
%{__rm} -rf %{buildroot}

%triggerpostun -- rclocal
echo "triggerpostun running with $1" >&2

chkconfig rclocal off >/dev/null 2>/dev/null || true
chkconfig --del rclocal >/dev/null 2>/dev/null || true

if [ "$1" != 0 ]; then
	chkconfig --add rclocal >/dev/null 2>/dev/null || true
	chkconfig rclocal on >/dev/null 2>/dev/null || true
fi
echo "triggerpostun finished with $1" >&2

%files

%attr(0755, root, root) /etc/init.d/rclocal

%changelog
