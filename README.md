# 🧠 Feature Engineering Playground

An interactive Streamlit demo app for exploring and applying common feature engineering techniques on tabular datasets. Ideal for data scientists, students, and educators looking to understand the impact of preprocessing on data and model performance.

## 🚀 Features

- 📁 Upload your own CSV dataset or use a default Titanic dataset.
- 🧹 Select one preprocessing technique at a time:
  - Fill missing values
  - Encode categorical variables
  - Scale numerical features
- 📊 View the dataset before and after transformation.
- ⚙️ Easily expandable for additional feature engineering steps or machine learning integration.

## 🖼️ Demo

![Screenshot](screenshot.png) <!-- Add a screenshot if available -->

## 🛠️ Installation

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
streamlit run app.py
```

## 📦 Requirements

- Python 3.7+
- pandas
- streamlit
- scikit-learn

Install all dependencies with:

```bash
pip install -r requirements.txt
```

## 📊 Usage

1. Launch the app with `streamlit run app.py`
2. Upload your dataset or use the default one.
3. Choose a preprocessing technique from the sidebar.
4. View the transformed dataset.

## 📌 To-Do

- [ ] Add support for chaining multiple preprocessing steps
- [ ] Integrate basic ML models for performance testing
- [ ] Allow visualizations of feature distributions
- [ ] Add feature selection options

## 🧪 Example Datasets

Uses the Titanic dataset by default from [Data Science Dojo](https://github.com/datasciencedojo/datasets).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ using [Streamlit](https://streamlit.io/)

