{ pkgs, project, python }:
(project.renderers.buildPythonPackage { inherit python; }) // {
  src = ./..;
  postPatch = ''
    substituteInPlace pyproject.toml \
      --replace-fail "cryptg-anyos" "cryptg"
  '';
  pythonRelaxDeps = [
    "cryptg"
  ];
  meta = {
    license = pkgs.lib.licenses.mit;
    homepage = "https://tgpy.tmat.me/";
    pythonImportsCheck = [ "tgpy" ];
  };
}
