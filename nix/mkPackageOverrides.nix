{ pkgs }:
self: super: {
  telethon-v1-24 = super.telethon.overridePythonAttrs (old: rec {
    version = "1.24.21";
    pname = "telethon_v1_24";
    src = pkgs.fetchPypi {
      inherit version pname;
      hash = "sha256-/RIWWawU4lp/fYmHq0KOU17XmllNSMos9pOb7A9FhHA=";
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
