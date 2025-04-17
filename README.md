### Issues Identified

- **Issue 1-** The original code didn’t allow the user to input their own topic, making it rigid and less interactive.
- **Issue 2-** There was no fallback in case of short or invalid input, which could break the program or lead to irrelevant results.
- **Issue 3-** Reference .txt files were saved in the root directory, causing clutter and making file management harder.
- **Issue 4-** Logic for all three execution methods (sequential, threads, processes) was repetitive instead of modular.

###  Task Breakdonwn

| Task # | Description                                     | Assignment        | Solution                                                                 |
|--------|-------------------------------------------------|-------------------|--------------------------------------------------------------------------|
| 1      | Add user input for search topic                 | Rohini            | Used input() and added fallback check for short entries                |
| 2      | Add default fallback topic                      | Rhett             | Defaulted to "generative artificial intelligence" if input < 4 characters |
| 3      | Organize output into a directory                | Tracy             | Used os.makedirs() to create a wiki_dl folder                        |
| 4      | Make download logic reusable                    | Charlize          | Created download_and_save() helper function                            |
| 5      | Improve error handling                          | Rohini            | Added try-except blocks around page access and file writing              |
| 6      | Refactor methods for better structure           | Stephen           | Kept original structure but made each cleaner and modular                |
| 7      | Test sequential/thread/process functionality    | All               | Verified files were created correctly in wiki_dl/                      |
| 8      | Write up issues, tasks, and README documentation| All           | Finalized README and completed all team documentation                    |
