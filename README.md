<p align="center">
  <a href="https://github.com/crystal-linux/todo/">
    <img src="https://github.com/crystal-linux/branding/blob/main/logos/crystal-logo-minimal.png?raw=true" alt="Logo" width="150" height="150">
  </a>
</p>

<h2 align="center">Jade</h2>

<p align="center">
    <a href="https://github.com/crystal-linux/.github/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-GPL--3.0-blue.svg" alt="License">
    <a href="https://github/crystal-linux/jade_gui"><img alt="GitHub isses" src="https://img.shields.io/github/issues-raw/crystal-linux/jade_gui"></a>
    <a href="https://github/crystal-linux/jade_gui"><img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr-raw/crystal-linux/jade_gui"></a><br>
    <a href="https://twitter.com/intent/user?screen_name=crystal_linux"><img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/crystal_linux?style=flat?color=blue">
    <a href="https://discord.gg/hYJgu8K5aA"><img alt="Discord" src="https://img.shields.io/discord/825473796227858482?color=blue&label=Discord&logo=Discord&logoColor=white"> </a>
    <a href="https://github.com/axtloss"><a href="https://github.com/axtloss"><img src="https://img.shields.io/badge/Maintainer-@axtloss-brightgreen" alt="The maintainer of this repository" href="https://github.com/axtloss"></a></a><br>
    <a href="https://fosstodon.org/@crystal_linux"><img alt="Mastodon Follow" src="https://img.shields.io/mastodon/follow/108618426259408142?domain=https%3A%2F%2Ffosstodon.org">
    <a href="https://twitter.com/crystal_linux"><img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/crystal_linux"></a>
    <a href="https://stopthemingmy.app/"><img alt="Please don't theme" src="https://stopthemingmy.app/badge.svg"><br>
    <a href="https://www.codefactor.io/repository/github/crystal-linux/jade-gui"><img src="https://www.codefactor.io/repository/github/crystal-linux/jade-gui/badge" alt="CodeFactor" /></a>
    
</p>

<p align="center"> The libadwaita/gtk based gui installer using jade as the backend.
</p>

<p align="center"><a  href="https://github.com/crystal-linux/demos-mockups/blob/main/jade_gui/preview.pdf">The jade gui mockups</p></a>


![](main-page-screenshot.png)


### Building
Building as a flatpak (recommended for development)
```sh
git clone https://github.com/crystal-linux/jade-gui
cd jade-gui
flatpak-builder --user --install --install-deps-from=flathub --force-clean build-dir al.getcryst.jadegui.yml
flatpak run al.getcryst.jadegui
```

Building with meson
```sh
git clone https://github.com/crystal-linux/jade-gui
cd jade-gui
meson --prefix=/usr _build
ninja -C _build
cd _build
sudo ninja install
```
