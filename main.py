import pandas as pd 
import requests, base64, svgwrite, os


df = pd.read_csv('full-emoji-list-and-skincolors-ranked-2019-2021&UID&GOODCLDR.csv')



def download_image(cldr, source, data):
    if str(data) != 'nan':
        base64_data = data
        decoded_data = base64.b64decode(base64_data.split(',')[1])
        filename = os.path.join("assets/png/", f"{cldr}_{source}.png")
        with open(filename, "wb") as f:
            f.write(decoded_data)
            print(f"Image saved to {filename}")
        return None



for i, r in df.iterrows():
    # AppleSVG GoogleSVG FacebookSVG WindSVG TwitterSVG JoySVG SamsungSVG GmailSVG SbSVG DcmSVG KddiSVG
    cldr = r['Code']
    download_image(cldr, 'Apple', r['AppleSVG'])
    download_image(cldr, 'Google', r['GoogleSVG'])
    download_image(cldr, 'Facebook', r['FacebookSVG'])
    download_image(cldr, 'Wind', r['WindSVG'])
    download_image(cldr, 'Twitter', r['TwitterSVG'])
    download_image(cldr, 'Joy', r['JoySVG'])
    download_image(cldr, 'Samsung', r['SamsungSVG'])
    download_image(cldr, 'Gmail', r['GmailSVG'])
    download_image(cldr, 'Sb', r['SbSVG'])
    download_image(cldr, 'Dcm', r['DcmSVG'])
    download_image(cldr, 'Kddi', r['KddiSVG'])