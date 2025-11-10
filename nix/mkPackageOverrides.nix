{ ... }:
self: super: {
  mkdocs-git-revision-date-localized-plugin =
    super.mkdocs-git-revision-date-localized-plugin.overrideAttrs
      (old: {
        pyproject = true;
        format = null;

        dependencies = old.propagatedBuildInputs ++ [ super.setuptools-scm ];
      });
}
