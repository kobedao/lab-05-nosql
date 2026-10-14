// Step 2: 
// use bookstore 
db = db.getSiblingDB("bookstore")

// Step 3: load authors.json
// paste your drop and insertMany commands here
db.authors.drop()
doc = JSON.parse(fs.readFileSync("authors.json", "utf8"))
db.authors.insertMany(doc)
// Step 4: load books.json
// paste your drop and insertMany commands here
db.books.drop()
doc = JSON.parse(fs.readFileSync("books.json", "utf8"))
db.books.insertMany(doc)
// Step 5: list authors and books
// paste your find commands here
db.authors.find()
db.books.find()
// Step 6: insert two new books
// paste your insert commands here
db.books.insertOne({title: 'book4', published_year: 2026, author_ids: ['author_004']});
db.books.insertOne({title: 'book5', published_year: 2027, author_ids: ['author_003', 'author_004']});
// Step 7: add missing authors
// paste your insert commands here
db.authors.insertMany([ {_id: 'author_004', name:'kobe dao', nationality: 'vietnamese', bio: {short: 'An American student and freelancer.', long:'He was a student at the University of Virginia and a freelance writer'}}]);
// Step 8: filter books by a list of authors
// paste your find command here
db.books.find({ author_ids: { $in: ["author_001", "author_004"] } })
