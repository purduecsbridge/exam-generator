# Exam Generator

Generates a multiple choice exam using LaTeX. The generator grabs questions written as YAML files inside of the `questions/` folder and randomizes them each time the generator is executed. The exam and solution are placed in a `out/` folder inside of the working directory.

## Prerequisites
The easiest way to run this generator is using Docker. If you'd prefer not to use Docker (or you are using Windows 10 Home and can't use Docker), you'll need a full LaTeX installation, as well as Python3.

## Usage

### Docker
macOS & Linux:
```bash
make
```

Windows:
```powershell
docker-compose build && docker-compose up
```

### Python & LaTeX
```bash
python3 generate.py
```

## Adding Questions
Add questions to the `questions/` in the format given by the `example_question`. Text must be valid LaTeX in order to render properly. The order of questions does not matter, as it is randomized with each execution of the generator.

### Useful Commands
- `\code{...}` – Makes the text inside the braces monospaced to distinguish keywords and other code

- `\begin{java} ... \end{java}` – Highlights the text inside the tags as Java source code; keywords are bolded

- `\Ans` – Marks an option as the correct answer

## License
Licensed under the [MIT License](LICENSE).
