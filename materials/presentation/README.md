# “The Presentation”

## Overview

## Mon Nov 27

**Agenda**
- Discussion of individual presentations (10 min ea).
- Tips & tricks for slideshow presenting.

- Set computers up for miniconda.
    - Windows WSL https://learn.microsoft.com/en-us/windows/wsl/install 
    - Miniconda: https://docs.conda.io/projects/miniconda/en/latest/

    - Brief introduction to virtual environments.

    contrib/camriddell/generic-environment.yml
    ```
    name: as.180.369
    channels:
    - conda-forge
    dependencies:
    - python=3.10
    - matplotlib=3.7.2
    - pandas=2.0.2
    - statsmodels=0.14
    - seaborn=0.12
    - pip
    - pip:
      - fredapi==0.5.1
    ```

    To download the above file run the following command:

    ```
    curl -o environment.yml https://raw.githubusercontent.com/llorracc/as.180.369/main/contrib/camriddell/generic-environment.yml
    ```

    Then run

    ```
    conda env update -f environment.yml
    ```

- Clone repository to local machine.
    - Learn proper discipline for git repositories.
    ```
    mkdir {github_id}
    cd {github_id}
    gh auth status # verify you are logged in
    gh auth login  # if not logged in
    gh repo clone {github_repository}
    ```

- Launch Jupyter Lab and view paper & presentation draft locally.

## Mon Dec 4

**Agenda**
- Presentations
    - Students will present (15 mins.) on their papers.
    - Include polished visuals to help convey your assertions.
    - 10 minutes per student + 5 min Q&A + 5 min allocation (×7 students = 140 min)


