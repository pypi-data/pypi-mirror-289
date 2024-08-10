# SPDX-FileCopyrightText: Peter Pentchev <roam@ringlet.net>
# SPDX-License-Identifier: BSD-2-Clause

{ pkgs ? import <nixpkgs> { }
, py-ver ? "11"
}:
let
  python-name = "python3${py-ver}";
  python = builtins.getAttr python-name pkgs;
  python-pkgs = python.withPackages (p: with p; [ tox ]);
in
pkgs.mkShell {
  buildInputs = [
    pkgs.gitMinimal
    python-pkgs
  ];
  shellHook = ''
    set -e
    python3.${py-ver} -m tox run-parallel
    exit
  '';
}
