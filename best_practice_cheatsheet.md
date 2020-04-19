# Short guide to scientific computational projects
**Core guiding principle:** Someone unfamiliar with your project (including you, some months later) should be able to look at your files, understand what you did and why, and easily repeat it.

**Murphy’s Law for computational projects:** For anything you do, you will probably have to repeat it again later (new data, new parameters, fixing bugs).

**General idea:** Breaking a lengthy workflow into pieces makes it easier to understand, share, describe, and modify. Make your project modular, and the modules transparent and reproducible. This is important **for you and for others**.

**Fun fact:** Sticking to good practices in a scientific computational project can save you a lot of time later, and make you (and others) a much happier person.


# Organization of files and directories
Stick to a standardized and self-explanatory directory structure. Ideally, all essential text files should be managed by a version control system (Git). Suggested organization:
![organization](Pictures/organization.png)

<span style="color:darkblue">Suggested project structure for computational projects (compare to Noble 2009)</span>

Note: This structure is a suggestion, which has *proven useful*. It should be your starting point.

* *notes.txt* (project notes/lab notebook):
    *chronologically organized; also useful for meetings/progress reports
    *simple text file is often good enough, but can be another format
* *doc/:* has subfolders like doc/manuscript1/ for manuscript-related stuff
* *bin/:* contains all code required to reproduce the project
    *there may be multiple bin/ folders that reside in experiment-specific subfolders (if this is more convenient)
* sometimes, there might be a src/ folder for source code (in this case, bin/ contains actual [binaries](https://unix.stackexchange.com/a/372875))
* *runall.sh:* some people use a universal driver script that runs all other scripts and generates all results; this can be useful, but less flexible than separate experiments with their own driver scripts
* *data/* contains raw input data; possible naming schemes:
    *e.g. data/sample1/ (logical organization) or data/20180130/ (chronological)
    *data/sample2/ or data/20180131/ etc.
* If Git is used: *.gitignore file*, used to place [only relevant files](https://stackoverflow.com/a/9227991/) (*.py, *.txt, *.sh, *.R, *.md, ...) under version control

# Driver script
* Often combines calls to shell commands, Python scripts, R scripts (using [Rscript](https://stackoverflow.com/a/18306656/), also see [Rstudio docs](https://support.rstudio.com/hc/en-us/articles/218012917-How-to-run-R-scripts-from-the-command-line)) and precompiled programs
* **Automates every data processing step** like creating the required directory structure
* **Records every performed operation** (beware of manual editing of output files)
* Contains many **informative comments** that explain what's going on
* Contains **all relevant information** like file and directory names and passes them as arguments to other scripts/programs
* Stores paths and constants as **variables in a separate section** in the beginning, which makes overview and modifications easier
* Uses **relative paths** (if project folder is transferred to another location, it still works)
* Uses `set -euxo pipefail` options (or some of them) for [safer scripting](https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/)
* **Checks data consistency/plausibility** frequently to make sure that nothing unexpected happened (and the results make sense)
* Uses `if (output_file does not exist), then <perform operation>` constructs to **easily repeat parts** of the experiment (after deletion of the respective output files)
* **The environment** in which the driver script operates should be clearly defined (required tools/databases and their versions); make sure that everything actually works if run in the defined environment!

# Alternative: Notebooks
* Jupyter notebooks or [R notebooks](https://bookdown.org/yihui/rmarkdown/notebook.html) (R notebooks do have [some advantages](https://minimaxir.com/2017/06/r-notebooks/), including easier version control; Jupyter notebooks have other advantages, and can be enhanced by plugins)
* Notebooks combine code, explanatory text and results. They are great for [data exploration](https://www.nature.com/articles/d41586-018-07196-1), less great for code development or complex workflows involving different programs.
* Notebooks are a useful data science tool if used properly: should be well named, clearly structured, informatively commented.
* Great for sharing reproducible workflows and results with other people.

# Scripts in general
* Start your design with **pseudocode** (or flowchart) that outlines the script logic; this is extremely helpful even for simple scripts
* Adopt **iterative and incremental development**: start with a minimalistic working version, keep changes small, test frequently
* Write modular code, i.e., **short, single-purpose functions/scripts** with clearly defined inputs and outputs → readable, reusable, and testable; avoid “swiss-army-knife” scripts that do many different things
* Provide **skeletal documentation** (e.g. brief comment section in the beginning) for every script, no matter how short. Otherwise, even short scripts can (and will) be really obscure.
    *simple test cases and usage information will be extremely helpful for you and for others
    *the same applies to every function: describe every argument and the return value in the beginning ([examples](https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings))
* Scripts should **break immediately if something is wrong**: check data consistency as often as possible (`assert` in Python), e.g. input arguments, non-empty files, consistent results, ...
* Provide **simple examples**/test data to make sure that the script works as expected
* **Avoid code duplication** (copying/pasting code is a BAD sign)
* Look for **well-maintained libraries** that help you do what you’re trying to do *before starting to write code*
* Stick to **best practices** for writing code: respect language-specific **style guidelines** (Python: [PEP8](https://realpython.com/python-pep8/)) and use **code checkers** (Python: [Flake8](https://realpython.com/python-code-quality/#linters) and [pylint](https://www.reddit.com/r/Python/comments/82hgzm/any_advantages_of_flake8_over_pylint/) to prevent bugs
    *running code checkers and testing is annoying, but probably better than [retracting a publication because of a bug](https://arstechnica.com/information-technology/2019/10/chemists-discover-cross-platform-python-scripts-not-so-cross-platform/)([ivory blog](http://ivory.idyll.org/blog/automated-testing-and-research-software.html))
    *many IDEs (like [Spyder](https://stackoverflow.com/a/51467284/)) provide built-in code analysis
    *always assume that you might have to share your scripts later with other people ([ivory blog](http://ivory.idyll.org/blog/2015-how-should-we-think-about-research-software.html))
* Get to know your [IDE](https://www.datacamp.com/community/tutorials/data-science-python-ide) to improve productivity (e.g. Spyder, PyCharm, Visual Studio, Atom + Hydrogen, vim [+ plugins](https://realpython.com/vim-and-python-a-match-made-in-heaven/); Jupyter + plugins is great for data analysis, but not for code development)

![style](Pictures/styleguide.png)
[Style guide (xkcd.com/1513)](https://xkcd.com/1513/)

# Code development and version control
* A version control system (VCS) stores snapshots of a project’s files in a repository. This has advantages like:
    1. Provides **backup**
    2. Keeps track of **changes** (versions/tags), so you don’t need files with names like *script_v1.py, script_v1_v2.py, script_final.py, script_really_final.py, script_absolutely_final.py* etc.
    3. Allows code **modifications** (branches) without breaking existing functionality, facilitates conflict resolution
* If you **collaborate with others**, you definitely want VCS
* If you **work on a larger codebase**, you definitely want VCS
* Really, just use VCS. It’s really cool, and helps with all kinds of stuff. My suggestion is Git + GitHub.
* A VCS is intended for use with text files that are essential to reproduce your project:
    * Most importantly, all your data processing scripts (e.g. Python, R, Bash), scientific notes and related text files. Put them under version control, do it now.
    *Large and/or binary files are NOT intended for use with VCS:
        * Raw data and, in general, large files and binary files (raw data should be backed up elsewhere)
        * Automatically generated files like intermediate and result files (can be re-calculated if required)
* References:
    * "A Quick Introduction to Version Control with Git and GitHub" ([Blischak et al., 2016](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004668))
    * "Ten Simple Rules for Taking Advantage of Git and GitHub" ([Perez-Riverol et al., 2016](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004947))
    * [Stackoverflow](https://stackoverflow.com/questions/2712421/r-and-version-control-for-the-solo-data-analyst), [Datascience-Stackexchange](https://datascience.stackexchange.com/questions/5178/how-to-deal-with-version-control-of-large-amounts-of-binary-data), [Bioinformatics-Stackexchange](https://bioinformatics.stackexchange.com/questions/112/how-to-version-the-code-and-the-data-during-the-analysis)
    
# Collaborating on computational projects
* Decide early on methods for communication/information exchange
* Use a VCS like Git to manage changes to a project
* Keep changes small (= group of edits that you might want to undo in one step)
* Share changes frequently (synchronize your progress with the progress of others)
* Use an additional checklist (log file) for keeping track of and sharing changes to the project
* Store each project in a folder that is daily mirrored to Dropbox or a remote repository such as GitHub (and/or use some automated daily backup system)

# Basic data management
* Save **raw data in a separate directory** (data/ or raw_data/) and make it read-only
* Do not duplicate (data) files unless necessary, **use symbolic links instead**
* Keep **large files compressed** (gzip)
* **Back up crucial files** like raw data files, scripts and notes/documentation in at least two spatially distinct locations (external drive next to the computer is not good enough, e.g. in case of fire/theft/alien attack/etc.); use a backup tool like [Borg backup](https://akito.ooo/index.php/2019/10/11/borg/) ([official documentation](https://borgbackup.readthedocs.io/en/stable/)) that provides deduplication (save identical files only once), compression and encryption
* **Make data analysis-friendly:**
    * convert to open, non-proprietary, standardized formats that can be easily re-used later
    * modify cryptic variable names and file names to make them more informative
    * [tidy up the data](http://garrettgman.github.io/tidying/)
* **Directory names:**
    * *chronological*: name is a date, e.g. 2018_03_15 (YYYY-MM-DD naming scheme for better sorting); useful if you have many experiments of the same type differing by date
    * *logical*: name is an abstraction of the content, e.g. assembly_first
    * *semi-logical* (often best option): name starts with number or date → sequence of steps (e.g. *01_filter, 02_parse, 03_visualization,* etc.)
* **Name files to reflect their function or content** in chronological order, e.g. a file name like dna_sample1.trimmed.filtered.assembled.filtered.fasta tells you exactly what happened to the data (what did happen to the data?)
* **Temporary file names** should be distinct from permanent file names, so you know which files are incomplete or irrelevant
    * you can rename files in a separate step; e.g. while writing to a file, call it *result_file_1.txt.tmp*, and rename it afterwards: `mv result_file_1.txt.tmp result_file_1.txt`
* **Delete unnecessary files**, especially if they can be easily recalculated (time/storage tradeoff) – keep your workspace clean
    * e.g. intermediate/temporary files, or experimental files after trying something out
    * do it as soon as possible, will be harder later on
* **Archive inactive projects** in a separate archive directory, packed as .tar.gz
* **Share your data** using scientific online repositories

<span style="color:blue">A developer's perfect date</span>
![date](Pictures/date.png)

# Basic project management
* Define **project goals**
* Outline the **milestones** necessary to reach the goals – each milestone should correspond to results (deliverables) that can be presented in form of a progress report/short presentation
* Outline the steps (**work packages**) required to reach each milestone
* Assess the **time and resources** required to complete each work package
    * Each work package should be disassembled into single steps, as fine-grained as possible (remember the algorithmic exercise about planning a city trip)
    * Think about possible difficulties in advance and how you can overcome them (risk analysis)
* **Reserve time for work packages in a (online) calendar in advance**
* **Use the reserved time** to complete the work packages
    * Introduce changes into the planning if required
* The current project status should be transparent to your PI and your collaborators

# Basic manuscript management
* Agree with all authors on the workflow before the writing starts
* Keep a **single master document online** which allows to track changes and is available to all co-authors, using a platform such as Google Docs
* Alternatively, keep the manuscript in plain text format under version control, using **LaTeX** or **Markdown**
* Keep supplementary materials in separate text-format files for easier re-use by others

# Beware of ...
* **Manual modification** of output files
    * Workflow becomes non-reproducible
    * You WILL forget later what you did
* **Messy workspace**
    * with lots of different files lying around, taking up space and making you nervous (sounds funny, but this is what actually happens)
* **Poorly tested/unjustified analysis steps**
    * Using non-default parameters, unpublished tools or untested workflows without very good reason → this will be much, much harder to publish
* **“Overfitting”**
    * Fine-tuning the workflow (e.g. tool parameters) to achieve the “desired” results
    * The results may become slightly better, but less reproducible and harder to publish
* **Confirmation bias** (human tendency to handle information in a way that confirms one’s preexisting beliefs or hypotheses)
    * Don’t “adapt” the analysis to your ideas about what the results should be; this might give seemingly better results short-term, but will cause more problems long-term
    * This is not the same as optimizing the workflow by identifying the tools/approaches best-suited for your data to obtain good results :)
    * *Rule of thumb*: A good result is often stable towards changes in parameters and even analysis methods. If it is not, it might not be a reliable result.
    
# Links
* **[The Carpentries](https://carpentries.org/)**: [Software Carpentry](https://software-carpentry.org/), [Data Carpentry](https://datacarpentry.org/)
* Noble WS. 2009. A Quick Guide to Organizing Computational Biology Projects. PLOS Computational Biology. 5(7):e1000424. [doi:10.1371/journal.pcbi.1000424.](https://doi.org/10.1371/journal.pcbi.1000424)
* Wilson G et al. 2017. Good enough practices in scientific computing. PLOS Computational Biology. 13(6):e1005510. [doi:10.1371/journal.pcbi.1005510.](https://doi.org/10.1371/journal.pcbi.1005510)
* Blischak JD et al. 2016. A Quick Introduction to Version Control with Git and GitHub. PLOS Computational Biology. 12(1):e1004668. [doi:10.1371/journal.pcbi.1004668.](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004668)

![end](Pictures/end.png)



