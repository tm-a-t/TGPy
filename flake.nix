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
      flake = rec {
        lib.mkPackageRequirements =
          { overrides, requirements }:
          overrides.extend (final: prev:
            builtins.mapAttrs (package: reqs:
              (builtins.getAttr package prev).overridePythonAttrs (old: {
                buildInputs = (old.buildInputs or [ ]) ++ (builtins.map (pkg: prev.${pkg}) reqs);
              })
            ) requirements
          );
        lib.mkTgpy =
          { system ? null
          , pkgs ? import nixpkgs { inherit system; }
          , poetry2nix ? inputs.poetry2nix.lib.mkPoetry2Nix { inherit pkgs; }
          }: poetry2nix.mkPoetryApplication {
            projectDir = ./.;
            preferWheels = false;
            meta = readMetadata { lib = pkgs.lib; };
            overrides = lib.mkPackageRequirements {
              overrides = poetry2nix.defaultPoetryOverrides.extend (self: super: {
                cryptg-anyos = super.cryptg-anyos.override {
                  preferWheel = true;
                };
                nh3 = import ./nix/nh3overrides.nix { inherit self super pkgs; };
              });
              requirements = {
                telethon-v1-24 = [ "setuptools" ];
                pipreqs = [ "setuptools" ];
                python-semantic-release = [ "setuptools" ];
              };
            };
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
            groups = [ "dev" ];
          }).overrideAttrs (old: {
            nativeBuildInputs = with pkgs; [
              poetry
              python3Packages.python-lsp-server
            ] ++ (with pkgs.python3Packages; [
              mkdocs
              mkdocs-material
              mkdocs-redirects
              mkdocs-git-revision-date-localized-plugin
              cairosvg
              pillow
            ]);
          });

        formatter = pkgs.nixpkgs-fmt;
      };
    };
}
