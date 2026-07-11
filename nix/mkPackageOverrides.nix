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
      rev = "9fac561eebab94c2452cf1fe0a25b4c04a33f8dd";
      hash = "sha256-w9H2I0sgaQ5ntYYGlGJC7YCt2w8FQpv4ad1Tf/S5z5s=";
    };
    build-system = [ super.hatchling ];
    patches = [ ];
    nativeCheckInputs = [ ];
  };
}
