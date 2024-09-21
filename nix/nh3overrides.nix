{ self, super, pkgs }:
super.nh3.overridePythonAttrs (old: {
  cargoDeps = pkgs.rustPlatform.fetchCargoTarball {
    inherit (old) src;
    name = "${old.pname}-${old.version}";
    sha256 = "sha256-fetAE3cj9hh4SoPE72Bqco5ytUMiDqbazeS2MHdUibM=";
  };
  buildInputs = old.buildInputs or [ ] ++ (pkgs.lib.optionals super.stdenv.isDarwin [
    pkgs.libiconv
  ]);
  nativeBuildInputs = old.nativeBuildInputs or [ ] ++ [
    self.setuptools-rust
  ] ++ (with pkgs.rustPlatform; [
    cargoSetupHook
    maturinBuildHook
    pkgs.cargo
    pkgs.rustc
  ]);
})
