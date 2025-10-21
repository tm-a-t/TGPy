{
  pkgs,
  project,
  python,
  rev ? null,
}:
let
  postPatch = ''
    substituteInPlace pyproject.toml \
      --replace-fail "cryptg-anyos" "cryptg"
  ''
  + pkgs.lib.optionalString (rev != null) ''
    substituteInPlace tgpy/version.py \
      --replace-fail "COMMIT_HASH = None" "COMMIT_HASH = \"${rev}\""
  '';
  newAttrs = {
    src = ./..;
    inherit postPatch;
    pythonRelaxDeps = [
      "cryptg"
      "rich"
    ];
    meta = {
      license = pkgs.lib.licenses.mit;
      homepage = "https://tgpy.dev/";
      pythonImportsCheck = [ "tgpy" ];
    };
  };
in
(project.renderers.buildPythonPackage { inherit python; }) // newAttrs
