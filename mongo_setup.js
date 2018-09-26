use AdventureUs_db;
db.createUser({
  user: "test_user",
  pwd: "test_user_pwd",
  roles: [
    { role: "readWrite", db: "AdventureUs_db"}
  ]
});

db.createCollection("cities"
