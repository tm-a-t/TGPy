{
  description = "Run Python code right in your Telegram messages";

  inputs = {
    flake-parts.url = "github:hercules-ci/flake-parts";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    pyproject-nix = {
      url = "github:pyproject-nix/pyproject.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    treefmt-nix = {
      url = "github:numtide/treefmt-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    inputs@{ self, flake-parts, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } (
      { lib, ... }:
      {
        imports = [
          ./nix/treefmt.nix
        ];

        systems = [
          "x86_64-linux"
          "aarch64-linux"
          "x86_64-darwin"
          "aarch64-darwin"
        ];

        flake.lib.project = inputs.pyproject-nix.lib.project.loadPyproject {
          pyproject = lib.pipe ./pyproject.toml [
            lib.readFile
            (lib.replaceStrings [ "cryptg-anyos" ] [ "cryptg" ])
            builtins.fromTOML
          ];
        };

        perSystem =
          { config, pkgs, ... }:
          let
            python = pkgs.python3.override {
              packageOverrides = import ./nix/mkPackageOverrides.nix { inherit pkgs; };
            };
            packageAttrs = import ./nix/mkPackageAttrs.nix {
              inherit (self.lib) project;
              inherit pkgs python;
              rev = self.rev or null;
            };
          in
          {
            packages = {
              tgpy = python.pkgs.buildPythonPackage packageAttrs;
              default = config.packages.tgpy;
            };

            devShells.default = pkgs.mkShell {
              packages = [
                pkgs.poetry
                pkgs.black
                pkgs.isort
                (python.withPackages (self.lib.project.renderers.withPackages { inherit python; }))
              ];
            };
          };
      }
    );
}
