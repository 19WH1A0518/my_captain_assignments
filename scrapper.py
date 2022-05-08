import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect


parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="Entetr the number of pages to parse", type=int)
parser.add_argument("--dbname", help="Entetr the number of pages to parse", type=int)
args = parser.parse_args()

oyo_url = "https://wwww.oyorooms.com/hotels-in-bangalore/?page="
page_num_MAX == args.page_num_max
scraped_info_lists = []
connect.connect(args.dbname)


for page_num in range(1, page_num_MAX):
  req = requsts.get(oyo_url +str(page_num))
  content = req.content

  soup = BeautifulSoup(content, "html.parser")

  all_hotels = soup.find_all("div", {"class": "hotelCardListing"})

  for hotel in all_hotels:
    hotel_dict = {}
    hotel_dict["name"] = hotel.find("h3", {"class": "listingHotelDescription__hotelNmae"}).text
    hotel_dict["address"] = hotel.find("span", {"itemprop": "streetAdress"}).text
    hotel_dict["price"] = hotel.find("span", {"class": "listingPrice__finalprice"}).text
    # try ...... except

    try:
      hotel_dict["rating"] = hotel.find("span", {"class": "hotelRting__ratingSummary"}).text
    except AttributeError:
      pass  

    parent_aminities_element = hotel.find("div",{"class": "amenityWrapper"})

    aminities_list = []
    for amenity in parent_aminities_element.find_all("div", {"class": "amenityWrapper__amenity"}):
        amenity_list.append(amenity.find("span", {"class": "d-body-sm"}).text.strip())

    hotel_dict["amenities"] = " ,".join(amenities_list[:-1])

    scraped_info_list.append(hotel_dict)    
    connect.insert_into_table(args.dbname, tuple(hotel_dict.values())

    #print(hotel_name,hotel_address,hotel_price,hotel_rating,amenities_list)

dataFrame = pandas.DataFrame(scraped_info_list)
dataFrame.to_csv("Oyo.csv")
connect.get_hotel_info(args.dbname)
