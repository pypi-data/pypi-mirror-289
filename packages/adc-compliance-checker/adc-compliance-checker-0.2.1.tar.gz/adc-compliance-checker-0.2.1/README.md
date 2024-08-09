# ADC-compliance-checker
Arctic Data Centre compliance checker is a python based tool for those wanting to submit data to the Artic Data Centre. The python module can be used to check if files fullfill the metadata requirements listed [here](https://adc.met.no/node/4).

The compliance checker can be used in combination with CF and ACDD chekcers to enusre NetCDF files adhere to the FAIR principles for data management.

## Usage

### Command Line
```sh
adc-compliance-checker <file_path>
```

#### Output Example

The tool will provide feeback on the compliance status of the file:
```plaintext
Summary:
========
- File metadata has all required attributes and they are non-empty.

Result:
=======

✅ file.nc metadata is ADC compliant!

```
or
```plaintext
File metadata is missing or has empty the following required global attributes:
===============================================================================
  - id: Required if not hosted by MET   (MISSING)
  - naming_authority: Required if not hosted by MET   (MISSING)
  - summary: Required   (MISSING)
  - ...

Summary:
========
- 23 required global attributes are missing.
- Please refer to the ADC compliance documentation to resolve these issues:
  https://adc.met.no/node/4

Result:
=======

❌ file.nc metadata is not ADC compliant!

```
