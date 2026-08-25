# DataCleaner

A simple web app for cleaning up CSV files — upload one or more CSVs, strip out empty and duplicate rows, and download the result. Built with [Streamlit](https://streamlit.io/) and [Pandas](https://pandas.pydata.org/).

## Features

- **Upload multiple CSV files at once** — files are combined into a single table
- **Remove empty rows** — clears out blank/whitespace-only cells and drops resulting empty columns
- **Remove duplicate rows** — deduplicates the combined dataset
- **Preview before download** — see the cleaned data right in the browser
- **One-click download** — export the cleaned result back to CSV

## Demo

1. Upload one or more `.csv` files
2. Check the boxes for the cleaning options you want (remove empty rows, remove duplicates)
3. Hit **Submit** to preview the cleaned table
4. Pick a filename and hit **Download CSV**

## Installation

```bash
git clone https://github.com/HYYH130613/DataCleaner.git
cd DataCleaner
pip install streamlit pandas numpy
```

## Usage

```bash
streamlit run data_cleaner.py
```

This opens the app in your default browser (typically at `http://localhost:8501`).

## How it works

- Uploaded CSVs are each read into a Pandas DataFrame, then concatenated into one combined DataFrame.
- **Remove empty rows** replaces blank/whitespace-only values with `NaN` and drops any resulting empty columns.
- **Remove duplicate rows** calls `drop_duplicates()` on the combined data.
- The cleaned DataFrame is rendered as a preview table and made available as a downloadable CSV.

## Requirements

- Python 3.8+
- streamlit
- pandas
- numpy

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
