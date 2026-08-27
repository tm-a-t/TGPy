{ pkgs, ... }:
self: super: {
  mkdocs-git-revision-date-localized-plugin =
    super.mkdocs-git-revision-date-localized-plugin.overrideAttrs
      (old: {
        pyproject = true;
        format = null;

        dependencies = old.propagatedBuildInputs ++ [ super.setuptools-scm ];
      });
  telethon = super.telethon.overridePythonAttrs (
    old:
    let
      version = "1.44.1.dev1";
    in
    {
      inherit version;
      src = pkgs.fetchFromCodeberg {
        owner = "Lonami";
        repo = "Telethon";
        rev = "7df274b72e489eab74895a8c574b865873170411";
        hash = "sha256-XAGE0pQyWDmrdAOrJUTE7DM/PyYhV+3lmhfTThh3ZSw=";
      };
      build-system = [ super.hatchling ];
      patches = [ ];
      postPatch = old.postPatch or "" + ''
        substituteInPlace telethon/version.py --replace-fail \
          "__version__ = '1.44.0'" "__version__ = '${version}'"
      '';
      nativeCheckInputs = [ ];
    }
  );
}
