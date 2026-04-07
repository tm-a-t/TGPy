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
  withPackages ? ps: [ ],
}:
let
  python = pkgs.python3.override {
    packageOverrides = import ./nix/mkPackageOverrides.nix { inherit pkgs; };
  };
  packageAttrsNoPackages = import ./nix/mkPackageAttrs.nix {
    inherit project;
    inherit pkgs python;
  };
  packageAttrs = packageAttrsNoPackages // {
    propagatedBuildInputs =
      (packageAttrsNoPackages.propagatedBuildInputs or [ ]) ++ (withPackages pkgs.python3Packages);
  };
in
{
  package = python.pkgs.buildPythonPackage packageAttrs;
  shell = pkgs.mkShellNoCC {
    packages = [
      pkgs.uv
      pkgs.ruff
      pkgs.isort
      (python.withPackages (project.renderers.withPackages { inherit python; }))
    ];
  };
}
