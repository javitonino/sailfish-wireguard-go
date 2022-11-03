Name:       wireguard-go
Summary:    Userspace implementation of WireGuard in Go
Version:    0.0.20220316
Release:    1
License:    MIT
URL:        https://www.wireguard.com

%description

%build
if [[ ! -d ~/go ]]
then
    curl -L https://go.dev/dl/go1.19.2.linux-386.tar.gz | tar xzC ~
fi

case %{_arch} in
    "aarch64") export GOARCH=arm64;;
    "armv7hl") export GOARCH=arm;;
    "i386") export GOARCH=386; export GOROOT=~/go; export GOPATH=~/go;;
esac
~/go/bin/go install golang.zx2c4.com/wireguard@%{version}

%install
case %{_arch} in
    "aarch64") export ARCH_PREFIX="linux_arm64/";;
    "armv7hl") export ARCH_PREFIX="linux_arm/";;
    "i486") export ARCH_PREFIX="";;
esac
install -d %{buildroot}%{_bindir}
install ~/go/bin/${ARCH_PREFIX}wireguard %{buildroot}%{_bindir}/wireguard

%files
%defattr(-,root,root,-)
%{_bindir}/wireguard
