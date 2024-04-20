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
    {
      self,
      nixpkgs,
      flake-utils,
      poetry2nix,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
        p2n = poetry2nix.lib.mkPoetry2Nix { inherit pkgs; };

        buildTgpy =
          pkgs:
          dev:
          builtins.trace "Not all features are supported due to the nature of nix" p2n.mkPoetryApplication {
            projectDir = ./.;
            preferWheels = true;
            groups = if dev then [ "dev" "guide" ] else [];
          };

        buildTgpyImage =
          pkgs:
          pkgs.dockerTools.buildLayeredImage {
            name = "tgpy_image";
            contents = [ (buildTgpy pkgs false) ];
            created = "now";
            config = {
              Cmd = [ "tgpy" ];
            };
          };
      in
      {
        packages = {
          tgpy = buildTgpy pkgs false;
          tgpyImage = buildTgpyImage pkgs;
          tgpyImage-aarch64Linux = buildTgpyImage pkgs.pkgsCross.aarch64-multiplatform;
          tgpyImage-x86_64Linux = buildTgpyImage pkgs.pkgsCross.gnu64;
          default = self.packages.${system}.tgpy;
        };

        devShells.default = pkgs.mkShell {
          inputsFrom = [ (buildTgpy pkgs true) ];
          packages = [ pkgs.poetry ];
        };
      }
    );
}
