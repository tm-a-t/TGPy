{ inputs, ... }:
{
  imports = [ inputs.treefmt-nix.flakeModule ];

  perSystem =
    { pkgs, lib, ... }:
    {
      treefmt = {
        projectRootFile = "flake.nix";
        programs = {
          ruff = {
            check = true;
            format = true;
          };

          nixfmt.enable = true;
          shfmt.enable = true;

          # taplo crashes `nix flake check` on darwin
          taplo.enable = pkgs.stdenv.hostPlatform.isLinux;

          yamlfmt.enable = true;

          prettier.enable = true;
        };

        settings.formatter = {
          ruff-check.priority = 1;
          ruff-format.priority = 2;
        };

        settings.excludes =
          [
            "*.md"

            "*.png"
            "*.jpg"
            "*.mp4"

            "LICENSE"

            "Dockerfile"
            ".dockerignore"

            ".gitignore"
            "*.lock"
          ]
          ++ lib.optionals pkgs.stdenv.hostPlatform.isDarwin [
            "*.toml"
          ];
      };
    };
}
