{ pkgs, ... }:
self: super: {
  mkdocs-git-revision-date-localized-plugin =
    super.mkdocs-git-revision-date-localized-plugin.overrideAttrs
      (old: {
        pyproject = true;
        format = null;

        dependencies = old.propagatedBuildInputs ++ [ super.setuptools-scm ];
      });
  telethon =
    super.telethon.overridePythonAttrs
      (_: {
        src = pkgs.fetchFromCodeberg {
          owner = "Lonami";
          repo = "Telethon";
          rev = "09ef697621aac7cf9e80b538063b2ca378eb2997";
          hash = "sha256-m55X17mIHmInDun+0685fWWFdPySt/4Ar4z+gl6blek=";
        };
      });
}
