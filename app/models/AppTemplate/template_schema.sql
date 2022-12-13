CREATE TABLE IF NOT EXISTS template_db 
(
  created TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  name_ TEXT  NOT NULL,
  account TEXT  NOT NULL,
  password_ TEXT  NOT NULL,
  admin_ boolean NOT NULL DEFAULT false,
  pictureURL TEXT,
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  last_modify_date TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  is_delete boolean NOT NULL DEFAULT false
);