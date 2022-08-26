pkgname=jade-gui
pkgver=1.1.4
pkgrel=3
pkgdesc="Libadwaita based gui frontend for jade"
license=('GPL3')
arch=('any')
url="https://github.com/crystal-linux/jade-gui"
depends=('jade' 'openssl' 'flatpak')
makedepends=('flatpak-builder' 'flatpak')
source=("git+${url}.git")
sha256sums=('SKIP')

build() {
    cd ${srcdir}/jade-gui
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
    flatpak-builder --install-deps-from=flathub --repo=../build-repo --force-clean ../build-dir al.getcryst.jadegui.yml
    flatpak build-bundle ../build-repo --runtime-repo=https://flathub.org/repo/flathub.flatpakrepo ../jade-gui.flatpak al.getcryst.jadegui
}

package() {
    mkdir -p ${pkgdir}/usr/share/jade-gui
    mkdir -p ${pkgdir}/usr/bin/
    cp jade-gui.flatpak ${pkgdir}/usr/share/jade-gui/jade-gui.flatpak
    echo -e "#!/usr/bin/env bash\nflatpak run al.getcryst.jadegui" > ${pkgdir}/usr/bin/jade-gui
    chmod +x ${pkgdir}/usr/bin/jade-gui
}
