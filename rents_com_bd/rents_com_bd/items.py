# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RentsComBdItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    purpose = scrapy.Field()
    property_type = scrapy.Field()
    size = scrapy.Field()
    bed = scrapy.Field()
    bath = scrapy.Field()
    balcony = scrapy.Field()
    parking = scrapy.Field()
    lift = scrapy.Field()
    floor = scrapy.Field()
    unit = scrapy.Field()
    unit_per_floor = scrapy.Field()
    total_units = scrapy.Field()
    price = scrapy.Field()
    service_charge = scrapy.Field()
    year_built = scrapy.Field()
    garage_size = scrapy.Field()
    interior = scrapy.Field()
    basement = scrapy.Field()
    building_registration_type = scrapy.Field()
    house_rules = scrapy.Field()
    front_road_size = scrapy.Field()
    common_area_size = scrapy.Field()
    nearby_landmark = scrapy.Field()
    preferred_tenant = scrapy.Field()
    gas = scrapy.Field()
    servant_room = scrapy.Field()
    servant_washroom = scrapy.Field()
    apartment_facing = scrapy.Field()
    building_facing = scrapy.Field()
    property_url = scrapy.Field()
    address = scrapy.Field()
    features = scrapy.Field()

