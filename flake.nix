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

  outputs = { self, nixpkgs, flake-utils, poetry2nix }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
        buildTgpy = (pkgs: 
          let 
           inherit (poetry2nix.lib.mkPoetry2Nix { inherit pkgs; }) mkPoetryApplication;
          in mkPoetryApplication rec { 
            projectDir = ./.; 
            preferWheels = true;
          }
        );

        buildTgpyImage = (pkgs: pkgs.dockerTools.buildLayeredImage {
          name = "tgpy_image";
          contents = [ (buildTgpy pkgs) ];
          created = "now";
          config = {
            Cmd = [ "tgpy" ];
          };
        });
      in
      {
        packages = {
          tgpy = buildTgpy pkgs;      
          tgpyImage = buildTgpyImage pkgs;
          tgpyImage-aarch64Linux = buildTgpyImage pkgs.pkgsCross.aarch64-multiplatform;
          tgpyImage-x86_64Linux = buildTgpyImage pkgs.pkgsCross.gnu64;
          default = self.packages.${system}.tgpy;
        };

        devShells.default = pkgs.mkShell {
          inputsFrom = [ self.packages.${system}.tgpy ];
          packages = [ pkgs.poetry ];
        };
      });
}
