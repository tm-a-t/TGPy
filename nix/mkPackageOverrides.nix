{ pkgs, ... }:
self: super: {
  mkdocs-git-revision-date-localized-plugin =
    super.mkdocs-git-revision-date-localized-plugin.overrideAttrs
      (old: {
        pyproject = true;
        format = null;

        dependencies = old.propagatedBuildInputs ++ [ super.setuptools-scm ];
      });
  telethon = super.telethon.overridePythonAttrs {
    version = "1.44.0-dev";
    src = pkgs.fetchFromCodeberg {
      owner = "Lonami";
      repo = "Telethon";
      rev = "5498ab9a9edb37cb1e86e838cca4f1f5ba611371";
      hash = "sha256-JBemqYi6t868945C+eGOdBE8Z+SM/iJHJK+gI/GNFmM=";
    };
    build-system = [ super.hatchling ];
    patches = [ ];
    nativeCheckInputs = [ ];
  };
}
