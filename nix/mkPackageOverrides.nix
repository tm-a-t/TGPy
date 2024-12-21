{ pkgs }:
self: super: {
  telethon-v1-24 = super.telethon.overridePythonAttrs (old: rec {
    version = "1.24.18";
    pname = "Telethon-v1.24";
    src = pkgs.fetchPypi {
      inherit version pname;
      hash = "sha256-rVgunqMHpOLjRhIZ7RfugTrrv136YtTlqa9CvWOyElY=";
    };
    doCheck = false;
  });
  mkdocs-git-revision-date-localized-plugin = super.mkdocs-git-revision-date-localized-plugin.overridePythonAttrs (old: {
    pyproject = true;
    format = null;

    dependencies = old.propagatedBuildInputs ++ [ super.setuptools-scm ];
  });
}
