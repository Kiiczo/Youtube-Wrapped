# Youtube Wrapped

**Youtube Wrapped** is a web application that analyzes your personal YouTube activity data for a given year and visualizes your watching habits with insightful statistics, highlights, and trends. Simply upload your exported YouTube history from Google Takeout as JSON, and get a clean, interactive dashboard summarizing your year on YouTube.

---

## Key Features

- **Easy Upload**: Drag and drop your YouTube JSON export to instantly visualize your data.
- **Comprehensive Stats**: See days without YouTube, average movies per day, active days, and total movies watched.
- **Content Breakdown**: Automatic classification of movies, shorts, and ads.
- **Personal Highlights**: Discover your top days, top videos, and favorite channels.
- **Temporal Analysis**: Interactive breakdowns by hour, day of the week, and month.
- **Summary Section**: Quick glance at your most active times, most-watched channel, and more.
- **Privacy First**: All analysis runs locally in your browser; your data is never uploaded or stored externally.

---

## Installation

No installation is required! Use the app directly via GitHub Pages:

➡️ **[Try Youtube Wrapped now on GitHub Pages](https://kiiczo.github.io/Youtube-Wrapped/)**

---

## Usage Example

1. **Export Your YouTube Data**:
   - Go to [Google Takeout](https://takeout.google.com/), select “YouTube and YouTube Music”, and export your activity.
   - Download and unzip your Takeout archive. Locate the relevant JSON file with your YouTube watch history.

2. **Run the App**:
   - Visit [the app](https://kiiczo.github.io/Youtube-Wrapped/).
   - Click “Upload a JSON” and select your YouTube activity JSON file.

3. **Explore Your Wrapped**:
   - Instantly see your key numbers, content breakdown, personal highlights, viewing patterns, and a year-in-review summary.
   - All processing happens in your browser for maximum privacy.

---

## How It Works (Technical Explanation)

- **Frontend**: The app is built with [stlite](https://github.com/whitphx/stlite), which enables Streamlit Python apps to run entirely in the browser using WebAssembly.
- **Data Processing**:
  - The uploaded JSON is processed with pandas in Python (via Pyodide in-browser).
  - The app filters your watch data to the selected year (default: 2024).
  - Videos are categorized as movies, shorts, or ads based on content.
  - Key metrics (days without YouTube, average movies per day, etc.) are computed.
  - Top days, top videos, and favorite channels are identified.
  - Temporal trends are calculated and visualized (by hour, weekday, month).
- **Visualization**: All charts and tables are rendered interactively with Streamlit components in your browser.
- **Privacy**: No data leaves your browser; everything is analyzed client-side.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

**Kiiczo**

- GitHub: [Kiiczo](https://github.com/Kiiczo)
- For questions, suggestions, or contributions, feel free to open an issue or pull request.

---