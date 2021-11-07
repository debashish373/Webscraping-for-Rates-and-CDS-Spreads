from WebScraper import WebScraper
import argparse

def run_scraper(extract=None,name=None):
    scraper = WebScraper()
    if extract=='CDS': 
        data = scraper.cds_scrape()
        if name!=None:
            print('CDS:',data[data.Name==name].Name.iloc[-1],'Price:',data[data.Name==name].Price.iloc[-1],'bps')
        else:
            print(data)
    return data

if __name__=="__main__":
    
    parser=argparse.ArgumentParser()
    parser.add_argument("--extract",type=str)
    parser.add_argument("--name",type=str)
    args=parser.parse_args()
    
    data=run_scraper(
        extract=args.extract,
        name=args.name
        )


