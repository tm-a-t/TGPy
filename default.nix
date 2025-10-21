{
  system ? builtins.currentSystem,
  inputs ? import ./nix/mkInputs.nix { },

  pkgs ? import inputs.nixpkgs { inherit system; },
  lib ? pkgs.lib,
  pyproject-nix ? import inputs.pyproject-nix { inherit lib; },
  project ? pyproject-nix.lib.project.loadPyproject {
    pyproject = lib.pipe ./pyproject.toml [
      lib.readFile
      (lib.replaceStrings [ "cryptg-anyos" ] [ "cryptg" ])
      builtins.fromTOML
    ];
  },
}:
let
  python = pkgs.python3.override {
    packageOverrides = import ./nix/mkPackageOverrides.nix { inherit pkgs; };
  };
  packageAttrs = import ./nix/mkPackageAttrs.nix {
    inherit project;
    inherit pkgs python;
  };
in
{
  package = python.pkgs.buildPythonPackage packageAttrs;
  shell = pkgs.mkShellNoCC {
    packages = [
      pkgs.poetry
      pkgs.ruff
      pkgs.isort
      (python.withPackages (project.renderers.withPackages { inherit python; }))
    ];
  };
}
