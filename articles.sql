CREATE TABLE articles (
	id INT PRIMARY KEY  NOT NULL,
	heading VARCHAR(255) NOT NULL,
	summary text,
	body text,
	url text,
	image_url text,
	entry_date text,
	category varchar(255),
	context_category varchar(12)
)