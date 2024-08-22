# Solar AI Multi-Tool App

This Streamlit app provides multiple AI-powered services using the Upstage Solar API, allowing users to generate content, translate text between languages, and get coding assistance. The app is designed to be flexible, allowing users to input their own API key for the Solar LLM and providing three distinct functionalities within a simple interface.

## Features

1. **Content Generation:**
   - Generates articles, product descriptions, marketing copy, or creative writing based on user input.
   
2. **Translation:**
   - Translates text between different languages efficiently by utilizing Solar's language capabilities.
   
3. **Coding Assistant:**
   - Assists developers with code generation, debugging suggestions, and explanations of programming concepts.

## Installation

### Prerequisites

Ensure you have Python 3.7+ installed on your machine. You will also need to have `streamlit` and `openai` installed in your Python environment.

1. Clone the repository or download the code:
   ```bash
   git clone https://github.com/yourusername/upstage-ai-hackathon.git
   cd solar-ai-multi-tool-app
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Dependencies

- `streamlit==1.20.0`
- `openai==0.27.0`

## Usage

1. **Run the Streamlit App:**
   To launch the app, run the following command in your terminal:
   ```bash
   streamlit run app.py
   ```

2. **Interface Options:**
   After running the app, you will be presented with the following options in the sidebar:
   - **Content Generation:** Generate creative content by providing a text prompt.
   - **Translation:** Translate text to a desired language by specifying both the text and target language.
   - **Coding Assistant:** Get help with coding by providing a query related to code snippets, debugging, or programming concepts.

3. **Enter Your API Key:**
   Upon launching the app, you will be prompted to enter your Solar API key via the sidebar. The API key is required to authenticate your requests to the Solar LLM.

4. **Provide Prompts:**
   Each service allows you to enter a prompt relevant to the selected functionality (e.g., content creation, translation, coding query). Once you enter a prompt and hit the corresponding button, the AI will process your request and display the response on the screen.

## Customization

You can customize the following components of the app:

- **API Key Input:** Allows users to input their Solar API key, ensuring privacy and flexibility.
- **Service Selection:** Users can toggle between different services (content generation, translation, coding assistant) via the sidebar.
- **Streamlit Feedback:** A star-based feedback widget allows users to rate their experience with the app.


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any feature suggestions or bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For questions or issues, contact us at:
- Email: `gimeialez@gmail.com`
- GitHub: [Gimmyalex](https://github.com/Gimmyalex)
