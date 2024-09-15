{
  description = "Run Python code snippets within your Telegram messages";

  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    { self
    , nixpkgs
    , flake-utils
    , ...
    }@inputs:
    {
      lib.mkTgpy =
        { system ? null
        , pkgs ? import nixpkgs { inherit system; }
        , poetry2nix ? inputs.poetry2nix.lib.mkPoetry2Nix { inherit pkgs; }
        }: poetry2nix.mkPoetryApplication {
          projectDir = ./.;
          preferWheels = true;
        };
    } //
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
        poetry2nix = inputs.poetry2nix.lib.mkPoetry2Nix { inherit pkgs; };
      in
      {
        packages = rec {
          tgpy = self.lib.mkTgpy { inherit system; };
          default = tgpy;
        };

        devShells.default = (poetry2nix.mkPoetryEnv {
          projectDir = ./.;
          preferWheels = true;
        }).overrideAttrs (old: {
          nativeBuildInputs = with pkgs; [
            poetry
            python3Packages.python-lsp-server
          ];
        });
      }
    );
}
