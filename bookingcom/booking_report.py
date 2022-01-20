#This file is going to include method that will parse
#The specific data that we need from each one of the deal boxes.
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class BookingReport:
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(
            By.CSS_SELECTOR,
            'div[data-testid="property-card"]'
        )

    def pull_deal_box_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            #Get hotels name
            hotel_name = deal_box.find_element(
                By.CSS_SELECTOR,
                'div[data-testid="title"]'
            ).get_attribute('innerHTML').strip()

            #Get hotels Price
            hotel_price = deal_box.find_element(
                By.CSS_SELECTOR,
                'span[class="fde444d7ef _e885fdc12"]'
            ).get_attribute('innerHTML').strip()

            #Get hotels Score
            hotel_score = deal_box.find_element(
                By.CSS_SELECTOR,
                'div[class="_9c5f726ff bd528f9ea6"]'
            ).get_attribute('innerHTML').strip()

            collection.append(
                [hotel_name, hotel_price, hotel_score]
            )
        return collection
