{
  description = "Run Python code right in your Telegram messages";

  inputs = {
    flake-parts.url = "github:hercules-ci/flake-parts";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    pyproject-nix = {
      url = "github:pyproject-nix/pyproject.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    inputs@{ flake-parts, pyproject-nix, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "aarch64-darwin"
        "x86_64-darwin"
      ];

      perSystem =
        { config, pkgs, ... }:
        let
          project = pyproject-nix.lib.project.loadPyproject {
            projectRoot = ./.;
          };
          python = pkgs.python3.override {
            packageOverrides = import ./nix/mkPackageOverrides.nix { inherit pkgs; };
          };
          packageAttrs = project.renderers.buildPythonPackage { inherit python; };
        in
        {
          packages = {
            tgpy = python.pkgs.buildPythonPackage (
              packageAttrs
              // {
                meta = {
                  license = pkgs.lib.licenses.mit;
                  homepage = "https://tgpy.tmat.me/";
                  pythonImportsCheck = [ "tgpy" ];
                };
              }
            );
            default = config.packages.tgpy;
          };

          devShells.default = pkgs.mkShell {
            packages = [
              (pkgs.callPackage ./nix/poetry-master.nix { })
              (python.withPackages (
                project.renderers.withPackages {
                  inherit python;
                  groups = [
                    "dev"
                    "guide"
                  ];
                }
              ))
            ];
          };

          formatter = pkgs.nixfmt-rfc-style;
        };
    };
}
