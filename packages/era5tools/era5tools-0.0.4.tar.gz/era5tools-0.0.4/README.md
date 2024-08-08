# era5tools
Functions to simplify the downloading and data conversion of ECMWF ERA5 reanalysis, compatible with the new Climate Data Store Beta (CDS-Beta). Currently only supports monthly means of SST, total precip and 2m temperature.

In order to use this package, you need
- an API key compatible with CDS-Beta
- the `eccodes` library installed on your system (the pip-installed `eccodes` package is just the Python bindings). General installation instructions for `eccodes`: https://confluence.ecmwf.int/display/ECC/ecCodes+Home
- Details for different systems are below:
  - Linux: https://gist.github.com/MHBalsmeier/a01ad4e07ecf467c90fad2ac7719844a
  - Mac: using HomeBrew, run `$ brew install eccodes`