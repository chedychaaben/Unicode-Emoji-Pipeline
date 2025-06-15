# Emoji Data Downloader & Website Filler

This project is designed to populate a website for our upcoming company using emoji image data previously collected from [unicode.org](https://unicode.org), specifically from the **Full Emoji List, v16.0** available at:

📄 https://unicode.org/emoji/charts/full-emoji-list.html

## 🔍 Project Purpose

The goal is to automate the downloading of emoji images and structure the data in a way that can be easily integrated into a web platform. This project handles:

- Parsing structured emoji data
- Extracting and decoding Base64 image data
- Downloading images across multiple platforms (e.g. Apple, Google, Twitter)
- Ensuring compatibility across platforms and operating systems

## 📁 Data Structure

The emoji dataset is in CSV format, where each row includes the following fields:

```
UID, Number, Code, Emoji, Parent, Rank 2019, Rank 2021, Child, CLDR, 
AppleSVG, GoogleSVG, FacebookSVG, WindSVG, TwitterSVG, JoySVG, 
SamsungSVG, GmailSVG, SbSVG, DcmSVG, KddiSVG
```

Each `*SVG` field contains the Base64-encoded image string for the emoji as rendered by that platform.

### Example Row:

```
56d7ccb9,1,U+1F600,😀,Smileys & Emotion,54.0,61.0,face-smiling,grinning face,
"data:image/png;base64,iVBORw0KGgoAAAANSUhEU..."
```

## ⚙️ Platform Compatibility

- The script is built to be compatible with multiple operating systems (Linux, macOS, Windows).
- It uses standard Python libraries to ensure broad support and easy setup.

## 📦 Requirements

- Python 3.x
- A CSV file in the specified format with Base64-encoded image data

Install requirements (if any are added in the future) using:

```bash
pip install -r requirements.txt
```

## 🔄 Future Plans

- Add web interface for uploading and visualizing emoji datasets
- Extend support for SVG rendering (if raw SVG strings are used)
- Include metadata filtering (by category, popularity, etc.)

## 📜 License

This project uses publicly available data from [unicode.org](https://unicode.org). Make sure to respect Unicode's licensing and usage guidelines if redistributing or repurposing the data.

## 📬 Contact

For questions, suggestions, or contributions, feel free to contact:

**Chedy Chaaben**  
📧 chedychaaben@gmail.com
