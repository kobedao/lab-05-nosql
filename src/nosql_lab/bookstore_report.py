#!/usr/bin/env python3
import os
import logging
import pymongo 
from pymongo import MongoClient

MONGODB_ATLAS_URL = os.environ.get('MONGODB_ATLAS_URL')
MONGODB_ATLAS_USER = os.environ.get('MONGODB_ATLAS_USER')
MONGODB_ATLAS_PWD = os.environ.get('MONGODB_ATLAS_PWD')

def main():
	"""Connects to MongoDB to print out total number of authors and for each author, their name, associated books, and associated publication year"""
	try:
		logging.info("Connecting to MongoDB")
		#Connects to MongoDB
		client = MongoClient(MONGODB_ATLAS_URL, username=MONGODB_ATLAS_USER, password=MONGODB_ATLAS_PWD)
		logging.info('Succesfully connected.')

		#Selects bookstore database and authors and books collections
		db = client['bookstore']
		authors = db['authors']
		books = db['books']
		logging.info('Successfully collected databases and collections')

		#list of author ids to find
		author_ids = ['author_001', 'author_004']

		#finds matching author ids
		matched = db.authors.find({ '_id': { '$in': author_ids } })

		#creates a list of matches and prints out the length
		matched_list = list(matched)
		print(f"Authors: {len(matched_list)}\n")

		#Print every authors name and their linked books with publication year
		for author in matched_list:
			print(f"{author.get('name')}")
			author_books = books.find({ 'author_ids': author['_id'] })
			#Prints our book title and year
			for book in author_books:
				print(f"\t{book.get('title')} ({book.get('published_year')})")

		#Exits connection
		client.close()
		logging.info("Exited MongoDB.")
	except Exception as e:
		logging.info("Failure to connect and use MongoDB")
		print(e)

if __name__ == "__main__":
    # Runs only when file is executed directly.
    main()
