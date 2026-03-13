-- Using MySQL, design a database whose name is IMDB. Create a proper MySQL Tables, Primary key, Foreign Key, add data into the MySQL tables
-- and do the following as given below:-
-- 1) Movie should have multiple media (video or image)alter
-- 2) Movie can belongs to multiple Genre
-- 3) Movie can be Multiple reviews and review can belongs to a user
-- 4) Artists can have multiple skills
-- 5) Artists can perform multiple role in a single film

-- Creating the IMDB database
Create database IMDB;
-- Selecting the database to work with
use IMDB;

-- Table to store movie details
-- movie_Id is the primary key
create table movies (
	movie_Id int Auto_Increment primary key,
    movie_Title varchar(255),
    release_Year int
);

-- Table to store media related to movies (images or videos)
-- One movie can have multiple media files
create table media (
media_Id int Auto_Increment primary key,
movie_Id int,
media_type varchar(50),
media_url varchar(255),
foreign key (movie_Id) references movies(movie_Id)
);

-- Table to store different genres
create table genres (
genre_Id int auto_increment primary key,
genre_name varchar(150)
);

-- Junction table to connect movies and genres
-- A movie can belong to multiple genres
create table movie_genre(
movie_Id int,
genre_Id int,
primary key (movie_Id, genre_Id),
foreign key (movie_Id) references movies(movie_Id),
foreign key (genre_Id) references genres(genre_Id)
);

-- Table to store user information
create table users(
user_Id int auto_increment primary key,
username varchar(50)
);

-- Table to store movie reviews
-- Each review belongs to a movie and a user
create table reviews(
review_Id int auto_increment primary key,
movie_Id int,
user_Id int,
rating int,
user_review varchar (250),
foreign key (movie_Id) references movies(movie_Id),
foreign key (user_Id) references users(user_Id)
);

-- Table to store artist details
create table artists (
artist_Id int auto_increment primary key,
artist_name varchar (75)
);

-- Table to store different skills an artist can have
create table skills (
skills_Id int auto_increment primary key,
skills_name varchar(100)
);

-- Junction table to connect artists and skills
-- An artist can have multiple skills
create table artist_skills(
artist_Id int,
skills_Id int,
primary key (artist_Id, skills_Id),
foreign key (artist_Id) references artists(artist_Id),
foreign key (skills_Id) references skills(skills_Id)
);

-- Table to define roles in a movie
create table roles (
role_Id int auto_increment primary key,
role_name varchar (20)
);

-- Junction table connecting movies, artists, and roles
-- This allows an artist to perform multiple roles in a movie
create table movie_artist_roles(
movie_Id int,
artist_Id int,
role_Id int,
primary key (movie_Id, artist_Id, role_Id),
foreign key (movie_Id) references movies(movie_Id),
foreign key (artist_Id) references artists(artist_Id),
foreign key (role_Id) references roles(role_Id)
);

-- Inserting sample movies
INSERT INTO movies (movie_Title, release_Year)
VALUES
('Inception', 2010),
('The Dark Knight', 2008),
('Interstellar', 2014);

-- Adding media files related to movies
INSERT INTO media (movie_id, media_type, media_url)
VALUES
(1, 'image', 'inception_poster.jpg'),
(1, 'video', 'inception_trailer.mp4'),
(2, 'image', 'dark_knight_poster.jpg'),
(3, 'video', 'interstellar_trailer.mp4');

-- Adding different movie genres
INSERT INTO genres (genre_name)
VALUES
('Action'),
('Sci-Fi'),
('Drama'),
('Adventure');

-- Connecting movies with their genres
INSERT INTO movie_genre (movie_id, genre_id)
VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 3),
(3, 2),
(3, 4);

-- Adding users who can review movies
INSERT INTO users (username)
VALUES
('john_doe'),
('alice_smith'),
('movie_fan');

-- Adding reviews given by users for movies
INSERT INTO reviews (movie_id, user_id, rating, user_review)
VALUES
(1, 1, 5, 'Amazing movie with great visuals'),
(1, 2, 4, 'Very complex but enjoyable'),
(2, 3, 5, 'Best superhero movie ever'),
(3, 2, 5, 'Beautiful story and science');

-- Adding artists who worked in movies
INSERT INTO artists (artist_name)
VALUES
('Leonardo DiCaprio'),
('Christian Bale'),
('Matthew McConaughey'),
('Christopher Nolan');

-- Adding skills that artists can have
INSERT INTO skills (skills_name)
VALUES
('Acting'),
('Directing'),
('Producing');

-- Assigning skills to artists
INSERT INTO artist_skills (artist_id, skills_Id)
VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 2),
(4, 3);

-- Adding possible roles in movies
INSERT INTO roles (role_name)
VALUES
('Actor'),
('Director'),
('Producer');

-- Linking artists with movies and their roles
INSERT INTO movie_artist_roles (movie_id, artist_id, role_id)
VALUES
(1, 1, 1),
(1, 4, 2),
(2, 2, 1),
(2, 4, 2),
(3, 3, 1),
(3, 4, 2);

-- Displaying data from tables to verify records
SELECT * FROM movies;
SELECT * FROM media;
SELECT * FROM genres;
SELECT * FROM movie_genre;
SELECT * FROM reviews;
SELECT * FROM artists;