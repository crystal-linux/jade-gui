#!/usr/bin/bash
#echo $1
flatpak-spawn --host bash -c "echo $1 > /tmp/jade.json"