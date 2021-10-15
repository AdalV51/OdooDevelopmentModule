-- If you want to alter the default "internal code" or value
ALTER TABLE ONLY res_partner ALTER COLUMN genre_field SET DEFAULT 'other';
ALTER TABLE ONLY res_partner ALTER COLUMN zip_code SET DEFAULT '00000';
ALTER TABLE ONLY res_partner ALTER COLUMN language SET DEFAULT 'other';