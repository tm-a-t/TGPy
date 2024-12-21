{ pkgs }:
let
  poetry-core = pkgs.python3Packages.poetry-core.overrideAttrs (old: {
    version = "2.0.0.dev0";
    src = pkgs.fetchFromGitHub {
      owner = "python-poetry";
      repo = "poetry-core";
      rev = "4749d63c822147b0dbaa82033c02628f92c97200";
      hash = "sha256-who4WpQXaA83e+Z6TN73bDSkPpNaFsjn1DIqYIVUEqk=";
    };

    doCheck = false;
    pytestCheckPhase = ''true'';
  });
in
pkgs.poetry.overridePythonAttrs (old: {
  version = "2.0.0.dev0";

  src = pkgs.fetchFromGitHub {
    owner = "python-poetry";
    repo = "poetry";
    rev = "625f42ef96f8321f4e1649f38e39e71cd2b09f3e";
    hash = "sha256-tBim3dlKdkcvWWGavHpv52HAZX1FvPh2S+FTKPMrZVs=";
  };

  dependencies = builtins.map (
    x: if x.pname or "" == "poetry-core" then poetry-core else x
  ) old.dependencies;

  pythonRelaxDeps = [
    "dulwich"
    "keyring"
    "virtualenv"
    "pkginfo"
  ];

  doCheck = false;
  postInstall = null;
})
