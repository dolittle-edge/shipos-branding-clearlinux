Name     : shipos-branding
Version  : 1.0.0
Release  : 1
License  : MIT
Summary  : shipOS branding package
URL      : https://github.com/dolittle-edge/shipos-branding-clearlinux
Source0  : ./shipos.issue
Source1  : ./getty.conf

%description

%prep

%build

%install
install -D -m 644 %{SOURCE0} %{buildroot}/usr/share/defaults/etc/issue
install -D -m 644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/getty@.service.d/default-issue.conf

%post

%preun

%postun

%files
%defattr(-, root, root, -)

/usr/share/defaults/etc/issue
/usr/lib/systemd/system/getty@.service.d/default-issue.conf

%changelog

