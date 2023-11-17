{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  nativeBuildInputs = with pkgs; [
    cmake
    poetry
  ];

  buildInputs = with pkgs; [
    python311Packages.pip
    python311Packages.debugpy
  ];

  packages = with pkgs; [
    git
    neovim
    python311
  ];

  GIT_EDITOR = "${pkgs.neovim}/bin/nvim";

  shellHook = ''
    git status
  '';
}
