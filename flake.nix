{
  description = "Run Python code right in your Telegram messages";

  inputs = {
    flake-parts.url = "github:hercules-ci/flake-parts";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = inputs@{ nixpkgs, flake-parts, ... }:
    let
      readMetadata = { lib }: (
        let
          pyproject = builtins.fromTOML (
            builtins.readFile ./pyproject.toml
          );
        in
        (with pyproject.tool.poetry; {
          inherit description;
          homepage = documentation;
          license = lib.meta.getLicenseFromSpdxId license;
        })
      );
    in
    flake-parts.lib.mkFlake { inherit inputs; } rec {
      flake = {
        lib.mkTgpy =
          { system ? null
          , pkgs ? import nixpkgs { inherit system; }
          , poetry2nix ? inputs.poetry2nix.lib.mkPoetry2Nix { inherit pkgs; }
          }: poetry2nix.mkPoetryApplication {
            projectDir = ./.;
            preferWheels = true;
            meta = readMetadata { lib = pkgs.lib; };
          };
      };

      systems = [ "x86_64-linux" "aarch64-linux" "aarch64-darwin" "x86_64-darwin" ];
      perSystem = { self', pkgs, ... }: {
        packages = {
          tgpy = flake.lib.mkTgpy {
            inherit pkgs;
          };
          default = self'.packages.tgpy;
        };

        devShells.default =
          let
            poetry2nix = inputs.poetry2nix.lib.mkPoetry2Nix { inherit pkgs; };
          in
          (poetry2nix.mkPoetryEnv {
            projectDir = ./.;
            preferWheels = true;
            groups = [ "dev" "guide" ];
            overrides = poetry2nix.overrides.withDefaults (final: prev: {
              cairocffi = pkgs.python3Packages.cairocffi;
              mkdocs-material = pkgs.python3Packages.mkdocs-material;
            });
          }).overrideAttrs (old: {
            nativeBuildInputs = with pkgs; [
              poetry
              python3Packages.python-lsp-server
              python3Packages.mkdocs
            ];
          });

        formatter = pkgs.nixpkgs-fmt;
      };
    };
}
