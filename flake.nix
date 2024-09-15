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
    , poetry2nix
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
        p2n = poetry2nix.lib.mkPoetry2Nix { inherit pkgs; };
      in
      {
        packages = rec {
          tgpy = p2n.mkPoetryApplication {
            projectDir = ./.;
            preferWheels = true;
          };
          default = tgpy;
        };

        devShells.default = (p2n.mkPoetryEnv {
          projectDir = ./.;
          preferWheels = true;
        }).overrideAttrs (old: {
          nativeBuildInputs = [ pkgs.poetry ];
        });
      }
    );
}
