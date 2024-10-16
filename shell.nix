{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    poetry
    python3Packages.pip
    python3Packages.setuptools
  ];

}
