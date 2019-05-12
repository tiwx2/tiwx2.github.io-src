#!/bin/bash
rm -rf output/*
pelican-themes --remove $1
pelican-themes --install "themes/$1"
pelican content