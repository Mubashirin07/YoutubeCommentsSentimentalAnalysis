from flask import Flask, render_template, request


import scraping, new ,deleteafter
import pandas as pd

if __name__ == "__main__":
    #url = input("Enter the url: ")
    url = 'https://youtu.be/XZl_YMqMeSA?si=AK4dPPBp2RmtyxLS'
    scraping.scrapfyt(url)
    summary = new.analyze_comments()
    print(summary)
    # deleteafter.file_delete()


    # return render_template("index.html",after_complete_message = after_complete_message, title = video_title,
    #                        owner = video_owner, comment_w_replies = video_comment_with_replies,
    #                        comment_wo_replies = video_comment_without_replies,
    #                        positive_comment = video_posive_comments, negative_comment = video_negative_comments,
    #                        pos_comments_csv = [pos_comments_csv.to_html()], neg_comments_csv = [neg_comments_csv.to_html()])


    