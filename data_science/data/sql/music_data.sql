INSERT INTO Album (AlbumID, Title, ReleaseDate, Genre, Artwork, RecordLabel) VALUES
(1, 'The Wall', '1979-11-30', 'Progressive rock', 'https://example.com/thewall.jpg', 'Harvest'),
(2, 'The Final Frontier', '2010-08-13', 'Heavy metal', 'https://example.com/thefinalfrontier.jpg', 'EMI'),
(3, 'Thriller', '1982-11-30', 'Pop', 'https://example.com/thriller.jpg', 'Epic');

INSERT INTO Artist (ArtistID, ArtistName) VALUES
(1, 'Pink Floyd'),
(2, 'Iron Maiden'),
(3, 'Michael Jackson');

INSERT INTO Album_Artist (AlbumID, ArtistID) VALUES
(1, 1),
(2, 2),
(3, 3);

INSERT INTO Track (TrackID, Title, TrackNo, TrackLength, AlbumID) VALUES
(1, 'In the Flesh?', 1, '3:19', 1),
(2, 'Another Brick in the Wall (Part 1)', 2, '3:12', 1),
(3, 'Another Brick in the Wall (Part 2)', 3, '4:01', 1),
(4, 'The Happiest Days of Our Lives', 4, '1:46', 1),
(5, 'Another Brick in the Wall (Part 3)', 5, '1:14', 1),
(6, 'The Final Frontier', 1, '4:12', 2),
(7, 'El Dorado', 2, '6:49', 2),
(8, 'Mother of Mercy', 3, '5:20', 2),
(9, 'Thriller', 1, '5:57', 3),
(10, 'Beat It', 2, '4:17', 3),
(11, 'Billie Jean', 3, '4:54', 3);