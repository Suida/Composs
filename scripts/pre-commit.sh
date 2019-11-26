#!/bin/sh

flake8 --install-hook git && git config --bool flake8.strict true
