# Projektowanie Baz Danych - Project 1 (sklep internetowy)

Project build with framework Express (Node.js) with MongoDB database.

### How to run

 - Install Node.js platform and MongoDB.
 - Download this repo with `git clone`.
 - Run `npm install` to install all dependencies.
 - Run `npn start` to run a local server.

##### Seeders

To work with fake data write your own seeder in `seeds` folder.

##### Mongo Schemas

```
Users:
 - _id          :ObjectId
 - username     :String
 - email        :String
 - password     :String
 - role         :Number
```

```
Product:
 - _id          :ObjectId
 - title        :String
 - description  :String
 - price        :Number
 - images       :Array
 - category_id  :ObjectId
```

```
Transactions:
 - _id          :ObjectId
 - user_id      :ObjectId
 - product_id   :ObjectId
 - count        :Number
 - status       :String
```

```
Categories:
 - _id          :ObjectId
 - name         :String
 - description  :String
```

```
Rating:
 - _id          :ObjectId
 - user_id      :ObjectId
 - product_id   :ObjectId
 - stars        :Number
```

```
Inventory:
 - _id          :ObjectId
 - product_id   :ObjectId
 - count        :Number
```
