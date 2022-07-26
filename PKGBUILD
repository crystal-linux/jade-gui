pkgname=jade-gui
pkgver=1.0.0
pkgrel=1
pkgdesc="Libadwaita based gui frontend for jade"
license=('GPL3')
arch=('any')
url="https://git.tar.black/crystal/programs/jade-gui"
depends=('jade' 'openssl' 'flatpak')
makedepends=('flatpak-builder' 'flatpak')
install=jadegui.install
source=("gui::git+${url}.git")
sha256sums=('SKIP')



build() {
    cd ${srcdir}
    flatpak remote-add flathub https://flathub.org/repo/flathub.flatpakrepo
    flatpak-builder --repo=../build-repo --force-clean ../build-dir al.getcryst.jadegui.yml
    flatpak build-bundle ../build-repo --runtime-repo=https://flathub.org/repo/flathub.flatpakrepo ../jade-gui.flatpak al.getcryst.jadegui
}

package() {
    mkdir -p ${pkgdir}/usr/share/jade-gui
    mkdir -p ${pkgdir}/usr/bin/
    cp jade-gui.flatpak ${pkgdir}/usr/share/jade-gui/jade-gui.flatpak
    echo "#!/usr/bin/env bash\nflatpak run al.getcryst.jadegui" > ${pkgdir}/usr/bin/jade-gui
    chmod +x ${pkgdir}/usr/bin/jade-gui
}

