# main

- Update this section with summaries of any changes from recent merge requests

## 1.0.18 / 2024-08-08
    - Bugfix in kml coremod to allow 0.6 sec data; cleanup of kml.pm.

## 1.0.17 / 2024-07-16
    - Update model to use new true_grid method of FFSimmer when constraints are specified.
    - Modify ffsim_ constraints to include ztor; other fixes.

## 1.0.16 / 2024-07-08
    - Remove numpy from dependencies: is included by shakelib.
    - FIX: Use the preferred source when source is not specified.
    - Change gitlab runner tag to build
    - Force numpy to be less than v2.0
    - Updating smclone to prefer atlas, then us, then preferred network ShakeMap...

## 1.0.15 / 2024-06-05
    - Refactor to use latest FFSimmer; add configs for FFSimmer simulations; 
      reduce default number of simulations to 50; fix bug in shape module.

## 1.0.14 / 2024-05-28
    - Fix shape.py to only make shapefile of the original ShakeMap IMTs; fix model.py
      to work with the latest changes in shakelib.

## 1.0.13 / 2024-05-20
    - No-op.

## 1.0.12 / 2024-05-20
    - Fix bug in stddev types in _derive_imts_from_mmi.

## 1.0.11 / 2024-05-13
    - Clean up model.py.
    - Fix bug that occurred when GMM only has total stddev.
    - Clean up the CLI functions.

## 1.0.10 / 2024-04-23
    - Modify model to use FFSimmer; fix tests.

## 1.0.9 / 2024-02-05
    - Fix bug: wrong gmice library in modules.conf.

## 1.0.8 / ---?
    - smclone stuff.

## 1.0.7 / 2023-12-21

    - Changes to support running scenarios with and without finite faults.
    - Add --points argument back into assemble module.

## 1.0.6 / 2023-12-18

    - Re-add cont_mi.json to outputs to make USGS website happy.

## 1.0.5 / 2023-12-8

    - Fix transfer_email to work with encrypted servers.

## 1.0.4 / 2023-12-5

    - Fix bug in transfer_base.py.

## 1.0.3 / 2023-11-28

    - Remove the openquake.engine dependencies since it is included in the shakelib install.

## 1.0.2 / 2023-11-27

    - Add versioning to model module

## 1.0.1 / 2023-11-2

    - Fix imports for makecsv.py
    - Add coverage report generation and artifact upload to CI
    - Add badges to repository for latest release version, pipeline tests and coverage

## 1.0.0 / 2023-10-31

    - Initial repository setup
    - Update CI file for testing and deployment
    - Add points fixes 
    - Improve test cleanup
    - Make test data paths relative to tests rather than install location
    - Bring esi-utils-cartopy functionality into this repository, remove as dep
    - Test deployment and path fix for .whl installations
