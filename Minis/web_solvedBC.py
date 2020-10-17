import os
import csv

udemy_csv = os.path.join("..", "Resources", "web_starter.csv")

title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

with open(udemy_csv, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        
        course_title = row[1]
        course_price = row[4]
        course_subscribers = row[5]
        course_reviews = row[6]        

        title.append(course_title)

        price.append(course_price)

        subscribers.append(course_subscribers)

        reviews.append(course_reviews)

        percent = round(float(course_reviews) / float(course_subscribers), 2)
        review_percent.append(percent)

        new_length = row[9].split(" ")
        length.append(float(new_length[0]))

cleaned_csv = zip(title, price, subscribers, reviews, review_percent, length)

output_file = os.path.join("web_final.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])

    writer.writerows(cleaned_csv)
