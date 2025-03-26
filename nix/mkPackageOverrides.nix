{ pkgs }:
self: super: {
  telethon-v1-24 = super.telethon.overridePythonAttrs (old: rec {
    version = "1.24.19";
    pname = "telethon_v1_24";
    src = pkgs.fetchPypi {
      inherit version pname;
      hash = "sha256-kO/7R8xGMiCjDHnixLKS6GDxP327HA4lnx/dlD3Q8Eo=";
    };
    doCheck = false;
  });
  mkdocs-git-revision-date-localized-plugin =
    super.mkdocs-git-revision-date-localized-plugin.overridePythonAttrs
      (old: {
        pyproject = true;
        format = null;

        dependencies = old.propagatedBuildInputs ++ [ super.setuptools-scm ];
      });
}
