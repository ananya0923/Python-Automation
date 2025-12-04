# Login Page Automation Project

This project is a **Selenium-based web automation framework** built using **Python**, following industry-standard testing practices.  
It includes end-to-end login automation, Page Object Model implementation, unit testing, and HTML reporting.

---

##  Features Implemented

###  1. Simple Login Test
Automated a complete login flow using Selenium WebDriver.  
Validates UI interactions, input fields, and authentication behavior.

---

###  2. Unit Testing (unittest Framework)
Used Python’s built-in `unittest` framework to structure and manage test cases with:
- SetUp and TearDown methods  
- Assertions  
- Organized test execution  

---

###  3. Page Object Model (POM)
Implemented POM to improve:
- Reusability  
- Maintainability  
- Readability  

Each page has a dedicated class containing elements and actions.

---

###  4. Separation of Test Scripts and Page Objects
The project follows a clean folder structure:
- `tests/` → Test case scripts  
- `pages/` → Page classes  
- `locators/` → All element locators  
- `reports/` → HTML test reports  

This makes the framework modular and scalable.

---

###  5. Separate Locator Class
Created a dedicated locator class using:
- `By.ID`
- `By.NAME`
- `By.XPATH`
- `By.CSS_SELECTOR`

Useful for centralized maintenance of all page locators.

---

###  6. Run Tests from Command Line
Run all tests using:
```bash

python -m unittest
``` 
---

###  7. HTML Reports
Integrated an HTML Test Runner to generate detailed execution reports.  
The generated report includes:
- Test execution status (Pass/Fail)
- Error details and stack traces
- Execution time
- Step-by-step test breakdown

Reports are automatically stored inside the **reports/** directory.

Example command to run tests with HTML reporting:

```python
import unittest
from HtmlTestRunner import HTMLTestRunner

if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner(output='reports'))

