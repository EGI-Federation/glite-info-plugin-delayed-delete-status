Name:           glite-info-plugin-delayed-delete-status
Version:        1.0.1
Release:        2%{?dist}
Summary:        Updates GLUE state attributes of delayed delete entries in the Top BDII
Group:          Development/Libraries
License:        ASL 2.0
URL:            https://github.com/EGI-Federation/glite-info-plugin-delayed-delete-status      
Source:         %{name}-%{version}.src.tgz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Requires: openldap-servers

%description
Updates GLUE state attributes of delayed delete entries in the Top BDII

%prep
%setup -q

%build
# Nothing to build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%post
touch /var/log/glite/glite-info-plugin-delayed-delete-status.log
chmod 0644 /var/log/glite/glite-info-plugin-delayed-delete-status.log 
chown ldap:ldap /var/log/glite/glite-info-plugin-delayed-delete-status.log

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/libexec/glite-info-plugin-delayed-delete-status
%doc /usr/share/doc/glite-info-plugin-delayed-delete-status/README

%changelog
* Tue Nov 16 2021 Andrea Manzi <andrea.manzi@egi.eu> - 1.0.1-2
- Add missing dependency to openldap-servers

* Wed Sep 02 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.0.1-1
- Fixed wrong attribute name GlueCEStatus to GlueCEStateStatus

* Fri Aug 02 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.0.0-1
- Initial release


