# The Regex Toolbox: Python Scripts for Seamless Data Processing

## Overview
This documentation covers several Python projects utilizing regular expressions (regexes) for various text-processing tasks. Each project demonstrates practical applications of regex for validation, parsing, and transformation.

## Projects

### 1. **Email Validator (`response.py`)**
#### **Purpose:**
Validates email addresses based on the `validator-collection` package.

#### **Usage:**
Run the script and enter an email when prompted:

    ```sh
    python response.py

**Example:**

    ```sh
    What's your email address? example@test.com
    ```

**Output:**

    ```sh
        Valid email address
    ```

**Regex Explanation:**
This project utilizes the validator-collection package instead of direct regex for validation.

**Edge Cases Considered:**
    Empty input

    Incorrectly formatted emails

    Non-email text input

### 2. **UM Counter (um.py)**
#### **Purpose:**
Counts occurrences of the word "um" in a given text while ensuring it is not part of another word.

#### **Usage:**
Run the script and provide text input:

    ```sh
    python um.py

Example:

    sh
    Text: Um... I was thinking, um, we should go.


**Output:**

    ```sh
    Number of "um": 2
    ```


**Regex Explanation:**

Pattern:

    ```regex
    \b um \b
    ```

\b ensures "um" is captured as a standalone word, avoiding cases like "yummy".

re.IGNORECASE ensures case insensitivity.

**Edge Cases Considered:**

    Variations like "Um", "UM", "um..." are correctly captured.

    Words containing "um" as a substring are ignored.

### 3. **Working Hours Converter (`working.py`)**
#### **Purpose:**
Converts a time range (e.g., "9 AM to 5 PM") into 24-hour format ("09:00 to 17:00").

#### **Usage:**
Run the script and input the time range:

    ```sh
    python working.py

**Example:**

    ```sh
    Hours: 10:30 PM to 8 AM
    22:30 to 08:00
    ```

**Regex Explanation:**

Pattern:

    ```regex
    ^(\d{1,2}):?(\d{2})?\s?(AM|PM)\s(?:to)\s(\d{1,2}):?(\d{2})?\s?(AM|PM)?$
    ```

Captures hours, optional minutes, and AM/PM indicators.

Ensures correct "to" separation.

**Edge Cases Considered:**

    Handles missing minutes ("9 AM to 5 PM" vs "9:30 AM to 5:45 PM").

    Handling "12 AM" (midnight conversion to 00:00).

    Variations in spacing and input formats.

### 4. **YouTube Link Parser (`watch.py`)**
#### **Purpose:**
Extracts video IDs from YouTube embed links and converts them to shortened URLs (youtu.be/...).

#### **Usage:**
Run the script and input an HTML snippet containing an iframe:

    sh
    python watch.py

**Example:**

    ```sh
    HTML: <iframe src="https://www.youtube.com/embed/abc123"></iframe>

**Output:**

    ```sh
    https://youtu.be/abc123
    ```

**Regex Explanation:**

Pattern:

    ```regex
    src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9?=_-]+)"
    ```

Captures embedded YouTube video ID from the iframe src attribute.

**Edge Cases Considered:**

    Properly extracts only valid YouTube links.

    Ignores unrelated HTML elements.

### 5. **IPv4 Validator (`numb3rs.py`)**
#### **Purpose:**
Validates whether a given input is a correctly formatted IPv4 address.

#### **Usage:**
Run the script and enter an IP address:

    ```sh
    python numb3rs.py
    ```

**Example:**

    ```sh
    IPv4 Address: 192.168.1.1
    ```

**Output:**

    ```sh
    True
    ```

**Regex Explanation:**

Pattern:

    ```regex
    ^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$
    ```

Matches four groups of numbers separated by dots.

Validation ensures each octet is within 0-255.

**Edge Cases Considered:**

    Invalid octets (256.5.6.0 fails).

    Incorrect formats ("my ip is 192.168.1.1" fails).

### Testing
Most of the projects include unit tests using pytest to ensure correctness. Run tests with:

    ```sh
    pytest test_project.py
    ```

These projects highlight regex in real-world applications for validation and transformation. Feel free to modify and extend them!