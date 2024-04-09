**Noun Phrase Chunking Parser**

This Python script utilizes NLTK (Natural Language Toolkit) to perform noun phrase chunking on input sentences. Noun phrase chunking involves identifying and extracting noun phrases from sentences, which can be useful in various natural language processing tasks such as information extraction, text analysis, and syntactic parsing.

### Usage:

1. **Installation:**

   Make sure you have NLTK installed in your Python environment. You can install NLTK via pip:

   ```
   pip install nltk
   ```

2. **Execution:**

   Run the script by executing the following command in your terminal:

   ```
   python parser.py
   ```

   If you want to parse a sentence from a file, you can provide the filename as an argument:

   ```
   python parser.py <filename>
   ```

   If no filename is provided, the script will prompt you to input a sentence.

3. **Input:**

   The script accepts sentences as input. It preprocesses the input by converting all characters to lowercase and removing any words that do not contain at least one alphabetic character.

4. **Output:**

   The script parses the input sentence(s) using a predefined context-free grammar and prints the parse trees along with the identified noun phrase chunks for each sentence.

5. **Algorithm:**

   - The script utilizes a recursive algorithm to traverse the parse tree and identify noun phrase chunks.
   - A noun phrase chunk is defined as any subtree of the sentence whose label is "NP" and does not contain any other noun phrases as subtrees.

6. **Dependencies:**

   - Python 3.x
   - NLTK (Natural Language Toolkit)

7. **Grammar Rules:**

   The script defines its own context-free grammar rules for parsing sentences. These rules are specified in the `TERMINALS` and `NONTERMINALS` variables within the script.

